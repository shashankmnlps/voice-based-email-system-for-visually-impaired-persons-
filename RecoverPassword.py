from home import home
from startup import startup as s

def recoverPassword(ch):
    flag = 0
    if ch == 0:
        r = home.mic("", "Please say username")
        print("You said, " + r + " is this correct?")
        r2 = home.mic("", "You said, " + r + " is this correct?")
        if r2 == "yes" or r2 == "s":
            flag = 1

        elif r2 == "no":
            recoverPassword(0)
        else:
            home.talk("", "Sorry not recognized please say again")
            recoverPassword(0)

    if flag == 1 or ch == 1:
        r3 = home.mic("", "Please say Keyword")
        print(r3)
        r4 = home.mic("", "You said, " + r3 + " is this correct?")
        if r4 == "yes" or r2 == "s":
            import connection
            mydb = connection.con()
            db = mydb.cursor()
            db.execute("select * from users where username = %s and keyword = %s", (r, r3))
            data = db.fetchall()
            if (len(data) == 1):
                pas = data[0][3]
                print(pas)
                home.talk("", "Your password is,")
                home.talk("", pas)
                home.talk("", " I am repeating again Your password is, ")
                home.talk("", pas)
                mydb.commit()
                s.login("", 99)
            else:
                home.talk("", "Username or keyword is invalid!")
                s.login("", 99)
        elif r4 == "no":
            recoverPassword(1)
        else:
            home.talk("", "Sorry not recognized please say again")
            recoverPassword(1)