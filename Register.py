from startup import startup as st
from home import home

class Register:
    flag = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    def register(self, cc):
            s.c = cc
            if s.c == 0:
                print("please say Email id without @Gmail.com")
                email = home.mic("", "please say Email id without @Gmail.com")
                em = email.replace(" ", "").lower()
                s.usermail = em + "@gmail.com"
                print("you said " + s.usermail + " is this correct?")
                verfy = home.mic("", "you said " + s.usermail + " is this correct?")
                s.vr = verfy
                if s.vr == "no":
                    s.register(0)
                elif s.vr == "yes":
                    import connection
                    mydb = connection.con()
                    db = mydb.cursor()
                    print(s.usermail)
                    db.execute("select * from users where email=%s", (s.usermail,))
                    check = db.fetchall()
                    mydb.commit()
                    vali = len(check)

                    if vali == 0:
                        s.flag = 1
                    else:
                        print("Email is already registered!")
                        home.talk("", "Email is already registered!")
                        st.login("", 99)

                else:
                    s.register(1)

            if s.c == 1 or s.flag == 1:
                print("please say the Email password")
                pwd = home.mic("", "please say the Email password")
                s.pw = pwd.replace(" ", "")
                print("you said " + s.pw + " is this correct?")
                cp = home.mic("", "you said " + s.pw + " is this correct?")
                if cp == "yes":
                    import smtplib as sm
                    server = sm.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    username = s.usermail
                    password = s.pw
                    try:
                        print(username, password)
                        server.login(username, password)
                        s.flag2 = 1
                    except:
                        print("Invalid Email or Password")
                        home.talk("", "Invalid Email or Password")
                        st.login("",99)



                elif cp == "no":
                    s.register(1)
                else:
                    s.register(1)
            if s.c == 6:
                import connection
                mydb = connection.con()
                db = mydb.cursor()
                db.execute("select * from newmails")
                data = db.fetchall()
                s.usermail = data[0][0]
                s.pw = data[0][1]
                print("Your new email id is, ", s.usermail)
                home.talk("", "Your new email id is, ")
                home.talk("", s.usermail)

            if s.c == 2 or s.flag2 == 1 or s.c == 6:
                print("please say username")
                s.username = home.mic("", "please say username")
                print("you said " + s.username + " is this correct?")
                verfy = home.mic("", "you said " + s.username + " is this correct?")
                s.vr = verfy
                if s.vr == "no":
                    s.register(2)
                elif s.vr == "yes":
                    s.flag3 = 1
                else:
                    s.register(2)

            if s.c == 3 or s.flag3 == 1:
                print("please say the password")
                pwd = home.mic("", "please say the password")
                s.password = pwd.replace(" ", "")
                print("you said " + s.password + " is this correct?")
                cp = home.mic("", "you said " + s.password + " is this correct?")
                if cp == "yes":
                    s.flag4 = 1
                elif cp == "no":

                    s.register(3)

                else:

                    s.register(3)
            if s.c == 4 or s.flag4 == 1:
                print("please say Your phone number.")
                pho = home.mic("", "please say Your phone number.")
                s.phone = pho.replace(" ", "")
                print("you said " + s.phone + " is this correct?")
                v = home.mic("", "you said " + s.phone + " is this correct?")
                if v == "yes":
                    s.flag5 = 1
                elif v == "no":
                    s.flag3 = 0
                    s.register(4)
                else:
                    s.flag3 = 0
                    s.register(4)

            if s.c == 5 or s.flag5 == 1:
                print("please say keyword to recover password if you forgot the password.")
                key = home.mic("", "please say keyword to recover password if you forgot the password.")
                s.keyword = key.replace(" ", "")
                print("you said " + s.keyword + " is this correct?")
                verfy = home.mic("", "you said " + s.keyword + " is this correct?")
                if verfy == "yes":
                    print("Your registration details are: \n"
                          "Email: " + s.usermail + "\nEmail password: " + s.pw + "\nusername: " + s.username + "\nPassword: " + s.password + "\n phone_no: " + s.phone + "\nkeyword:" + s.keyword)
                    home.talk("", "Your registration details are: "
                                  "Email: " + s.usermail + ",Email password: " + s.pw + ", username: " + s.username + ", Password: " + s.password + ", phone_no: " + s.phone + ", keyword:" + s.keyword)
                    import connection
                    mydb = connection.con()
                    db = mydb.cursor()
                    db.execute("insert into users(email,epassword,username,password,phone,keyword) values(%s,%s,%s,%s,%s,%s)",
                               (s.usermail, s.pw, s.username, s.password, s.phone, s.keyword))
                    mydb.commit()
                    if s.c == 6:
                        db.execute("delete from newmails where email=%s", (s.usermail,))
                        mydb.commit()
                    print("Successfully Registered.")
                    home.talk("", "Successfully Registered.")
                    import Sms
                    Sms.send_sms(s.phone,
                                 "You are successfully registered your \n Username is " + s.username + "\n password is " + s.password)

                    st.login("", 99)
                elif verfy == "no":
                    s.flag3 = 0
                    s.register(4)
                else:
                    s.flag3 = 0
                    s.register(4)
s = Register()