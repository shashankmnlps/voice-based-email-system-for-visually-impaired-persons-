import pyttsx3 as py
import speech_recognition as sr



class home:

    def talk(this,text):
        engine = py.init()
        engine.setProperty('rate', 145)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()

    def mic(self, question):
        ans = input(question)
        return ans
    def mic1(self, question):
        try:
            listener = sr.Recognizer()
            listener.pause_threshold = 0.7
            listener.energy_threshold = 400
            with sr.Microphone() as source:
                e.talk(question)
                print("listening.....")
                voice = listener.listen(source,timeout=5)

                answer = listener.recognize_google(voice)
            return answer
        except:
            print ("Please Say Again")
            d = e.mic("Please Say Again")
            return d


    def ask(this,username,password):
        print ("You want send mail, read the mail, Delete mail")
        answer = e.mic("You want send mail, read the mail, Delete mail, Logout")
        if (answer == "sendmail" or answer == "send mail" or answer == "send" or answer == "send the mail"):
            check = 1
            import send
            send.send.to("",username,password)

        elif (answer == "readmail" or answer == "read mail" or answer == "read"):
            from read import read
            read.read_email_from_gmail("",username, password)
        elif answer == "delete" or answer == "delete mail" or answer == "deletemail":
            import delete
            delete.dell(username, password)
        elif answer == "logout" or answer == "Logout" or answer == "log out":
            from startup import startup
            startup.login("",99)
        else:
            print ("please Say Again")
            e.talk("please Say Again")
            e.ask(username, password)

e = home()