import flask
import sqlite3
my_website=flask.Flask("__name__")

@my_website.route("/")
def my_index_page():
    return flask.render_template("index.html")

@my_website.route("/newUser")
def my_newUser_page():
    return flask.render_template("newUser.html")

@my_website.route("/registerUser", methods=['POST'])
def register_user():
    entered_username=flask.request.form.get("username")
    entered_password = flask.request.form.get("password")
    entered_email = flask.request.form.get("email")
    entered_mobile = flask.request.form.get("mobile")
    print(entered_username)
    print(entered_password)
    print(entered_email)
    print(entered_mobile)

    try:
        con=sqlite3.connect("my_database.sqlite3")
        print("Connected to database Successfully")
    except:
        print("Error occured while connecting to Database")

    cur=con.cursor()
    my_create_table = "create table if not exists userstable(name varchar(20),password varchar(15),email varchar(30),mobileno varchar(10))"
    cur.execute(my_create_table)
    select_query=f"select email from userstable where email='{entered_email}'"
    cur.execute(select_query)
    result=cur.fetchone()
    if result == None:
        insert_query = f"insert into userstable values('{entered_username}','{entered_password}','{entered_email}','{entered_mobile}')"
        cur.execute(insert_query)
        return "Registered Successfully"
    else:
        return "Email Already Exists....try with other email ID"

if __name__  == "__main__":
    my_website.run(debug=True)