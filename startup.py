from tkinter import *
from home import home
import mysql.connector


class startup:
    vr = 0
    flag = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    root = 0
    def exit(self):
        s.root.destroy()
    def start(this):
        s.login(99)

    def login(this,ch):
        if ch == 99:
            print("Do you want to login. register. recover password. reset password. Exit")
            s.r = home.mic("","Do you want to login. register. recover password. reset password. Exit")
            print(s.r)
            if s.r == "register":
                print ("Do u have a email?")
                rr = home.mic("", "Do u have a email?")
                from Register import Register as r
                if rr == "yes" or rr == "s":
                    r.register("",0)
                    s.login(99)
                elif rr == "no" or rr == "No":
                    r.register("",6)



        if ch == 0 or s.r == "login":
            s.r = ""
            s.user = home.mic("", "please say username")
            print("you said "+ s.user +" is this correct?")
            verfy = home.mic("", "you said "+ s.user +" is this correct?")
            s.vr=verfy
            if s.vr == "no":
                s.login(0)
            elif s.vr == "yes":
                s.flag = 1
            else:
                s.login(0)
        if ch == 1 or s.flag == 1:
            pwd = home.mic("", "please say the password")
            pw = pwd.replace(" ", "")
            print("you said "+ pw +" is this correct?")
            cp = home.mic("","you said "+ pw +" is this correct?")
            if cp == "yes":
                    import connection
                    mydb = connection.con()
                    db = mydb.cursor()
                    db.execute("select phone from users where username = %s", (s.user, ))
                    chh = db.fetchall()
                    if len(chh)!=0:
                        phone = chh[0][0]

                    db.execute("select email,epassword from users where username=%s and password=%s", (s.user, pw))
                    r = db.fetchall()
                    for i in r:
                        s.email = i[0]
                        s.password = i[1]
                        print(s.email+" "+s.password)
                    print(len(r))
                    check = len(r)
                    import datetime
                    x = datetime.datetime.now()
                    alert = x.strftime('%I:%M %p %d-%B-%Y')
                    if check == 1:
                        print("Successfully logged in...")
                        home.talk("", "Successfully logged in...")
                        import Sms

                        Sms.send_sms(phone, "Alert! \nLogged in at, "+alert)
                        home.ask("", s.email, s.password)
                    elif check !=1:
                        print ("username or password invalid")
                        home.talk("", "username or password invalid")
                        import Sms
                        Sms.send_sms(phone, "Alert! \nSomeone trying to login using your username at, "+alert+"\nif that was you please ignore....")
                        s.login(99)


            elif cp == "no":
                s.login(1)

            else:
                s.login(1)
        elif s.r == "recover password" or s.r == "Recover password" or s.r == "recoverpassword" or s.r == "Recoverpassword":
            print(s.r)
            import RecoverPassword as rp
            rp.recoverPassword(0)
        elif s.r == "reset password" or s.r == "Reset password" or s.r == "Resetpassword" or s.r == "resetpassword":
            from resetPassword import Reset as r
            r.resetPassword("", 0)
        elif s.r == "exit":
            home.talk("", "Exiting, Have a nice day.")
            s.exit()
        else:
            home.talk("", "Sorry not recognized please say again")
            s.login(99)

    def launch(this):
        s.root = Tk()
        s.root.geometry("1366x763")
        s.root.title("Voice Based Email Eystem For Blinds")
        image = PhotoImage(file="back.png")
        Label(text="Voice Based Email System For Blinds", bg="lightblue", width=1366, font=('Arial', 30),pady=20).pack()
        Button(height=600, width=1366, image=image, command=s.start).pack()
        s.root.mainloop()



s = startup()
