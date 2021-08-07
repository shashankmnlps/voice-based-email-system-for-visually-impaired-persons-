from home import home
import smtplib as sm
class send:
    flag =0
    email =""
    pas = ""
    def send(self,ch):
        if ch != 1:
            print ("Please say the subject")
            s.subject = home.mic("","Please say the subject")
            print ("You Said, " + s.subject + " is this correct?")
            c = home.mic("", "You Said, " + s.subject + " is this correct?")
            if c == "no":
                s.send(0)
            if c == "yes":
                s.flag = 1
            else:
                s.send(0)
        if ch == 1 or s.flag == 1:
            print ("Say The text Message")
            msg = home.mic("","Say The text Message")
            print(msg)
            mail  = 'Subject: {}\n\n{}'.format(s.subject, msg)
            print("You Said " + msg + " Do you want to send or do you want to change?")
            conform = home.mic("","You Said " + msg + " Do you want to send or do you want to change?")
            if (conform == "send" or conform == "yes send" or conform == "yes"):
                print(send.to1)
                server = sm.SMTP('smtp.gmail.com', 587)
                server.starttls()
                username = s.email
                password = s.pas
                server.login(username, password)
                server.sendmail(username, send.to1, mail)
                print ("Mail Is Successfully Sent...")
                home.talk("","Mail Is Successfully Sent...")
                home.ask("",username,password)
            elif (conform == "change" or conform == "chenge" or conform == "i want to change"):
                s.send(1)
            else:
                print ("could'nt Recognized")
                home.talk("","could'nt Recognized")
                s.send(1)

    def conf(self):
        print ("You Said " + send.to1 + "Is this correct?")
        replay = home.mic("", "You Said " + send.to1 + "Is this correct?")
        print(replay)
        if (replay == "yes" or replay == "s"):
            s.send(0)
        elif (replay == "no"):
            s.to(s.email,s.pas)
        else:
            print ("plaese Say Again")
            home.talk("", "plaese Say Again")
            s.conf()


    def to(this,username,password):
        s.email=username
        s.pas=password
        print ("to whome you want to send")
        answer2 = home.mic("","to whome you want to send")
        temp = answer2.replace(" ", "")
        tomail = temp.lower()
        send.to1 = tomail + "@gmail.com"
        s.conf()



s = send()