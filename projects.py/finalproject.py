from flask import *
import pymysql

db=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="pymysql_new"
    )

cursor=db.cursor()
app =Flask(__name__)


@app.route("/")
def index():
    return render_template("index3.html")


@app.route("/about")
def about():
 return render_template("about3.html")             


@app.route("/contact")
def contact():
    return render_template("contact3.html")          

@app.route("/allusers")
def allusers():
    cursor.execute("select * from medlineplus")
    data=cursor.fetchall()
    return render_template("allusers3.html",userdata=data)    

@app.route("/create",methods=["POST"])
def create():
    uname=request.form.get('uname')
    pwd=request.form.get('pwd')
    available_stock=request.form.get('available_stock')
    insq="insert into medlineplus(medicine_name,price,available_stocks)values('{}','{}','{}')".format(uname,pwd,available_stock)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in Querry"

@app.route("/delete")
def delete():
    id=request.args.get('id')
    delq="Delete from medlineplus where id={}".format(id)
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in Querry"

@app.route("/edit")
def edit():
    id=request.args.get('id')
    selq="select * from medlineplus where id ={}".format(id)
    cursor.execute(selq)
    data=cursor.fetchone()
    return render_template("edit3.html",row=data)

    
@app.route("/update",methods=["POST"])
def update():
    uname=request.form.get('uname')
    pwd=request.form.get('pwd')
    available_stocks=request.form.get('available_stocks')
    uid=request.form.get('uid')
    isq="update medlineplus set medicine_name='{}',price='{}',available_stocks='{}' where id='{}'".format(uname,pwd,available_stocks,uid)
    try:
        cursor.execute(isq)
        db.commit()
        return redirect(url_for("allusers"))
    except:
        db.rollback()
        return "Error in Querry"

@app.route("/search")
def search():    
    return render_template("search4.html")

@app.route("/getdata",methods =["POST"])
def getdata():
    uname=request.form.get('uname')
    selq = "select * from medlineplus where medicine_name='{}'".format(uname)

    cursor.execute(selq)
    data = cursor.fetchone()
    return render_template("search4.html",row=data)
    
                             
if __name__=='__main__':
    app.run(debug=True,port=1000)     
    
