import os
from flask import *
from werkzeug.utils import secure_filename

from cnn import predictcnn
from db import *
app = Flask(__name__)
app.secret_key="12345"

@app.route('/')
def login():
    return render_template("index.html")

@app.route('/logincode', methods=['post'])
def logincode():
    username = request.form['UN']
    password = request.form['PWD']
    qry = "SELECT * from login where username=%s and password=%s"
    val=(username, password)
    res = selectone(qry,val)
    if res is not None:
        if res['type']=="rto":
            session['lid'] = res['id']
            return '''<script>alert("Welcome RTO");window.location='/indexrto'</script>'''
            # return redirect('/indexrto')
        elif res['type']=="User":
            session['lid']=res['id']
            return '''<script>alert("Welcome USER");window.location='/userhome'</script>'''
            # retur/n redirect('/userhome')
        elif res['type'] == "Scrapdealer":
            session['lid'] = res['id']
            return '''<script>alert("Welcome SCRAP DEALER");window.location='/scrapdealer_home'</script>'''
            # return redirect('/scrapdealer_home')
        else:
            return '''<script>alert("Invalid username or password");window.location="/"</script>'''
    else:
        return '''<script>alert("Invalid username or password");window.location="/"</script>'''


#============================================RTO===================================================

@app.route('/indexrto',methods=['get','post'])
def indexrto():
    return render_template("indexrto.html")

@app.route('/scrapdealerar',methods=['get','post'])
def scrapdealerar():
    q="SELECT `login`.*,`scrapdealer`.* FROM `login` JOIN `scrapdealer` ON `login`.`id`=`scrapdealer`.`loginid` WHERE `login`.`type`='pending'"
    res=selectall(q)
    return render_template("scrapdealerar.html", data=res)

@app.route('/acceptsd')
def acceptsd():
    id = request.args.get('id')
    qry = "update login set type='Scrapdealer' where id=%s"
    iud(qry, id)
    return '''<script>alert("Accepted");window.location="/scrapdealerar"</script>'''

@app.route('/rejectsd')
def rejectsd():
    id=request.args.get('id')
    qry = "update login set type='Rejected' where id=%s"
    iud(qry,id)
    return '''<script>alert("Rejected");window.location="/scrapdealerar"</script>'''



@app.route('/complaint', methods=['get', 'post'])
def complaint():
    q="SELECT `complaint`.*,`user`.* FROM `complaint` JOIN `user` ON `complaint`.`uid`=`user`.`loginid` "
    res=selectall(q)
    return render_template("complaint.html",data=res)

@app.route('/reply',methods=['get', 'post'])
def reply():
    cid = request.args.get('id')
    session['cid'] = cid
    return render_template("reply.html")

@app.route('/sendreply', methods=['post'])
def sendreply():
    msg = request.form['MSG']
    qry = "update complaint set reply=%s where cid=%s"
    val = (msg, str(session['cid']))
    iud(qry, val)
    return '''<script>alert("Submitted");window.location="/complaint"</script>'''

@app.route('/verifiedscrapdealer', methods=['get', 'post'])
def verifiedscrapdealer():
    q="SELECT `login`.*,`scrapdealer`.* FROM `login` JOIN `scrapdealer` ON `login`.`id`=`scrapdealer`.`loginid` WHERE `login`.`type`='Scrapdealer'"
    res=selectall(q)
    return render_template("verifiedscrapdealerar.html",data=res)

@app.route('/scraprequest',methods=['get','post'])
def scraprequest():
    qry = "SELECT `user`.`fname`,`lname`,`scrapdealer`.`sdname` ,`vehicle`.*,`userrequest`.status,`rid` FROM `userrequest` JOIN `vehicle` ON`vehicle`.`vid`=`userrequest`.`vid` JOIN `user` ON `user`.`loginid`=`vehicle`.`uid` JOIN `scrapdealer` ON `scrapdealer`.`loginid`=`userrequest`.`sdid`  WHERE `userrequest`.`status`='Forwarded' "
    res= selectall(qry)
    print(res)
    return render_template("scraprequest.html", data=res)

@app.route('/acceptrq')
def acceptrq():
    id = request.args.get('id')
    qry = "UPDATE `userrequest` SET `status`='Accepted' WHERE `rid`=%s"
    iud(qry, id)
    return '''<script>alert("Accepted");window.location="/scraprequest"</script>'''

@app.route('/rejectrq')
def rejectrq():
    id = request.args.get('id')
    qry = "UPDATE `userrequest` SET `status`='Rejected' WHERE `rid`=%s"
    iud(qry, id)
    return '''<script>alert("Rejected");window.location="/scraprequest"</script>'''

@app.route('/certificate', methods=['get', 'post'])
def certificate():
    return render_template("certificate.html")

#==============================================SCRAP DEALER===========================================

@app.route('/sdsignup',methods=['get','post'])
def sdsignup():
    return render_template("sdsignup.html")

@app.route('/sdreg', methods=['post'])
def sdreg():
    name = request.form['NAME']
    place = request.form['PLACE']
    post = request.form['POST']
    pin = request.form['PIN']
    phone = request.form['PHONE']
    mail = request.form['MAIL']
    proof = request.files['PROOF']
    fn=secure_filename(proof.filename)
    proof.save(os.path.join('static/proof', fn))
    username = request.form['UN']
    password = request.form['PWD']
    qry1 = "insert into login values(null, %s, %s, 'Pending')"
    val = (username, password)
    id = iud(qry1, val)
    qry2 = "insert into scrapdealer values(null, %s, %s, %s, %s, %s, %s, %s, %s)"
    val2 = (id, name, place, post, pin, phone, mail, fn)
    iud(qry2, val2)
    return '''<script>alert("Registered Successfully");window.location="/"</script>'''

@app.route('/scrapdealer_home',methods=['get','post'])
def scrapdealer_home():
    return render_template("scrapdealer_index.html")

@app.route('/changepwd', methods=['get', 'post'])
def changepwd():
    return render_template("changepwd.html")

@app.route('/rating', methods=['get', 'post'])
def rating():
    qry="SELECT `rating`.*,`user`.`fname`,`lname` FROM `rating` JOIN `user` ON `rating`.`uid`=`user`.`loginid`  WHERE `rating`.`sdid`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("rating.html",data=res)

@app.route('/userrequest', methods=['get', 'post'])
def userrequest():
    qry="SELECT `userrequest`.*, `vehicle`.* ,`user`.`fname`,`lname`FROM `userrequest` JOIN `vehicle` ON`vehicle`.`vid`=`userrequest`.`vid` JOIN `user` ON `user`.`loginid`=`vehicle`.`uid` WHERE `userrequest`.`sdid`=%s"
    res=selectall2(qry, session['lid'])
    return render_template("userrequest.html", data=res)

@app.route('/forwardrq')
def forwardrq():
    id = request.args.get('id')
    qry = "UPDATE `userrequest` SET `status`='Forwarded' WHERE `rid`=%s"
    iud(qry, id)
    return '''<script>alert("Forwarded");window.location="/userrequest"</script>'''

@app.route('/rjctrq')
def rjctrq():
    id = request.args.get('id')
    qry = "UPDATE `userrequest` SET `status`='Rejected' WHERE `rid`=%s"
    iud(qry, id)
    return '''<script>alert("Rejected");window.location="/userrequest"</script>'''


#=========================USER========================================

@app.route('/userhome',methods=['get','post'])
def userhome():
    return render_template("userhome.html")

@app.route('/usersignup',methods=['get','post'])
def usersignup():
    return render_template("usersignup.html")

@app.route('/userreg', methods=['post'])
def userreg():
    fname = request.form['FNAME']
    lname = request.form['LNAME']
    gender = request.form['GENDER']
    place = request.form['PLACE']
    post = request.form['POST']
    pin = request.form['PIN']
    phone = request.form['PHONE']
    mail = request.form['MAIL']
    username = request.form['UN']
    password = request.form['PWD']
    qry1 = "insert into login values(null, %s, %s, 'User')"
    val = (username, password)
    id = iud(qry1, val)
    qry2 = "insert into user values(null, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val2 = (id, fname, lname, gender, place, post, pin, mail, phone)
    iud(qry2, val2)
    return '''<script>alert("Registered Successfully");window.location="/"</script>'''

@app.route('/viewvehicle',methods=['get','post'])
def viewvehicle():
    q="SELECT * FROM `vehicle` WHERE `uid`=%s"
    res=selectall2(q,session['lid'])
    return render_template("viewvehicle.html",data=res)

@app.route('/addvehicle',methods=['get','post'])
def addvehicle():
    return render_template("addvehicle.html")

@app.route('/vehicleadd_post',methods=['post'])
def vehicleadd_post():
    import time
    model=request.form['textfield']

    rc=request.files['file']
    rn=time.strftime("%Y%m%d_%H%M%S")+".jpg"
    rc.save("static/rc/"+rn)

    fitness=request.files['file2']
    fn=time.strftime("%Y%m%d_%H%M%S")+".jpg"
    fitness.save("static/fitness/"+fn)

    q="INSERT INTO `vehicle` VALUES(NULL, %s, %s, %s,%s)"
    val=(session['lid'],model,rn,fn)
    iud(q,val)
    return '''<script>alert("Added Successfully");window.location="/viewvehicle"</script>'''

@app.route('/delete_vehicle')
def delete_vehicle():
    id=request.args.get('id')
    q="DELETE FROM `vehicle` WHERE `vid`=%s"
    iud(q,id)
    return '''<script>alert("Deleted Successfully");window.location="/viewvehicle"</script>'''

@app.route('/userstatus',methods=['get','post'])
def userstatus():
    q="SELECT `userrequest`.*, `vehicle`.* FROM `userrequest` JOIN `vehicle` ON `vehicle`.`vid`=`userrequest`.`vid` WHERE `vehicle`.`uid`=%s"
    res=selectall2(q,session['lid'])
    return render_template("userstatus.html", data=res)

@app.route('/dealerlist',methods=['get','post'])
def dealerlist():
    qry="SELECT `login`.*,`scrapdealer`.* FROM `login` JOIN `scrapdealer` ON `login`.`id`=`scrapdealer`.`loginid` WHERE `login`.`type`='Scrapdealer'"
    res=selectall(qry)
    return render_template("dealerlist.html", data=res)

@app.route('/sendrequest',methods=['get','post'])
def sendrequest():
    id=request.args.get('id')
    session['sid']=id
    q = "SELECT * FROM `vehicle` WHERE `uid`=%s"
    res=selectall2(q,session['lid'])
    return render_template("sendrequest.html", data=res)

@app.route('/snd_request',methods=['get','post'])
def snd_request():
    id=session['sid']
    vid=request.form['select']
    q = "INSERT INTO `userrequest` VALUES (NULL,%s,%s,CURDATE(),'pending')"
    val=(id,vid)
    iud(q,val)
    return '''<script>alert("Send Successfully");window.location="/dealerlist"</script>'''


@app.route('/usercomplaint',methods=['get','post'])
def usercomplaint():
    q="SELECT `complaint`.*,`scrapdealer`.`sdname` FROM `complaint` JOIN `scrapdealer` ON `complaint`.`dealer_id`=`scrapdealer`.`loginid`"
    res=selectall(q)
    return render_template("usercomplaint.html",data=res)

@app.route('/sendcomplaint', methods=['post'])
def sendcomplaint():
    q="SELECT * FROM `scrapdealer`"
    res=selectall(q)
    return render_template('send_complaint.html',data=res)

@app.route('/snd_complaint',methods=['post'])
def snd_complaint():
    s=request.form['select']
    complaint=request.form['textfield']
    q1="INSERT INTO `complaint` VALUES (NULL,%s,%s,%s,CURDATE(),'pending')"
    val = (session['lid'],s,complaint)
    iud(q1, val)
    return '''<script>alert("Send successfully");window.location='usercomplaint'</script>'''

@app.route('/userrating',methods=['get','post'])
def userrating():
    q = "SELECT * FROM `scrapdealer`"
    res = selectall(q)
    return render_template("userrating.html", data=res)

@app.route('/setrating', methods=['post'])
def setrating():
    dealer = request.form['select']
    rating = request.form['select1']
    qry = "INSERT INTO `rating` VALUES (NULL,%s,%s,%s)"
    val = (str(session['lid']),dealer,rating)
    iud(qry, val)
    return '''<script>alert("Done");window.location="/userrating"</script>'''

@app.route('/pre')
def pre():
    return render_template('predict_value.html')

@app.route('/predict',methods=['post'])
def predict():
    image=request.files['file']
    image.save(r'C:\Users\91956\PycharmProjects\scrapnet\src\static\1.jpg')
    result=predictcnn('static/1.jpg')
    res=int(result)
    return render_template('result.html',re=res)

app.run(debug=True)