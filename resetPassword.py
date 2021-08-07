from home import home
from startup import startup as st

class Reset:
    def resetPassword(self, ch):
        flag = 0
        flag2 = 0
        flag3 = 0
        if ch == 0:
            r = home.mic("", "Please say username")
            print("You said, " + r + " is this correct?")
            r2 = home.mic("", "You said, " + r + " is this correct?")
            if r2 == "yes" or r2 == "s":
                flag = 1

            elif r2 == "no":
                s.resetPassword(0)
            else:
                home.talk("", "Sorry not recognized please say again")
                s.resetPassword(0)

        if flag == 1 or ch == 1:
            r3 = home.mic("", "Please say old password")
            print(r3)
            r4 = home.mic("", "You said, " + r3 + " is this correct?")
            if r4 == "yes" or r2 == "s":
                flag2 = 1
            elif r4 == "no":
                s.resetPassword(1)
            else:
                home.talk("", "Sorry not recognized please say again")
                s.resetPassword(1)
        if flag2 == 1 or ch == 2:
            r5 = home.mic("", "Please say new password")
            print(r5)
            r6 = home.mic("", "You said, " + r5 + " is this correct?")
            if r6 == "yes" or r6 == "s":
                flag3 = 1
            elif r6 == "no":
                s.resetPassword(2)
            else:
                home.talk("", "Sorry not recognized please say again")
                s.resetPassword(2)
        if flag3 == 1 or ch == 3:
            rr = home.mic("", "Do you want to change keyword? ")
            import connection
            mydb = connection.con()
            db = mydb.cursor()
            db.execute("select * from users where username = %s and password = %s", (r, r3))
            ll = db.fetchall()
            s.l = len(ll)
            number = ll[0][4]
            print(s.l)
            if rr == "yes" or rr == "s":
                r7 = home.mic("", "Please say keyword ")
                print(r7)
                r8 = home.mic("", "You said, " + r7 + " is this correct?")
                if r8 == "yes" or r8 == "s":
                    print("your details are Username: \n" + r + "\n Old Password: " + r3 + "\n New Password: " + r5 + "\n New Keyword: " + r7)
                    home.talk("", "your details are Username: " + r + "\n Old Password: " + r3 + "\n New Password: " + r5 + "\n New Keyword: " + r7)

                    if s.l == 0:
                        home.talk("", "Username or password is invalid!")
                        st.login("", 99)
                    elif s.l == 1:

                        db.execute("update users set password =%s, keyword=%s where username = %s and password = %s", (r5, r7, r, r3))
                        mydb.commit()
                        print("Successfully Changed Password and keyword")
                        home.talk("", "Successfully changed password and keyword")
                        import Sms
                        Sms.send_sms(number, "Successfully changed keyword and password.\n Password is " + r5 + "\n Keyword is " + r7)
                        st.login("", 99)
                elif r8 == "no":
                    s.resetPassword(3)
                else:
                    home.talk("", "Sorry not recognized please say again")
                    s.resetPassword(3)
            elif rr == "no":
                print("your details are:\n Username: " + r + "\n Old Password: " + r3 + "\n New Password: " + r5)
                home.talk("", "your details are Username: " + r + "\n Old Password: " + r3 + "\n New Password: " + r5)

                if s.l == 1:
                    db.execute("update users set password =%s where username = %s and password = %s", (r5, r, r3))
                    mydb.commit()
                    print("Successfully Changed Passwor")
                    home.talk("", "Successfully changed password")
                    import Sms
                    Sms.send_sms(number, "Successfully changed password.\n your New Password is " + r5)
                    st.login("", 99)
                elif s.l == 0:
                    home.talk("", "Username or password is invalid!")
                    st.login("", 99)
s = Reset()