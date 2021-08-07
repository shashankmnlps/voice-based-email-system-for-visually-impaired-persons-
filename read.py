import imaplib
import email
import re
import speech_recognition as sr
from email.header import decode_header
import pyttsx3
import webbrowser
from home import home
class read:
    body = "h"
    def talk(this,text):
        engine = pyttsx3.init()
        engine.setProperty("rate", 178)
        engine.say(text)
        engine.runAndWait()
    def get_info1(this):
        info =input("enter:")
        return info

    def get_info(this):
        try:
            listener = sr.Recognizer()
            listener.pause_threshold = 0.7
            listener.energy_threshold = 400
            with sr.Microphone() as source:
                print("listening.....")
                voice = listener.listen(source, timeout=5)

                answer = listener.recognize_google(voice)
            return answer
        except:
            print("Please Say Again")
            r.talk("Please Say Again")
            d = r.get_info()
            return d




    def read_email_from_gmail(this,username, password):

            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login(username, password)
            mstatus, messages = mail.select("INBOX")

            result, data = mail.search(None, 'ALL')
            mail_ids = data[0]

            id_list = mail_ids.split()
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])

            for i in range(latest_email_id,first_email_id, -1):
                # need str(i)
                result, data = mail.fetch(str(i), '(RFC822)' )

                for response_part in data:
                    if isinstance(response_part, tuple):

                        # from_bytes, not from_string
                        msg = email.message_from_bytes(response_part[1])
                        email_from = decode_header(msg['from'])[0][0]
                        if isinstance(email_from, bytes):
                            email_from = email_from.decode()
                        print('From : ' + email_from + '\n')
                        r.talk('From : ' + email_from + '\n')
                        print('can i read subject of this mail')
                        r.talk('can i read subject of this mail')
                        reply = r.get_info()
                        if (reply == "yes" or reply == "s"):
                            subject = decode_header(msg['subject'])[0][0]
                            if isinstance(subject, bytes):
                                subject = subject.decode()
                            print('Subject : ' + subject + '\n')

                            r.talk('Subject : ' + subject + '\n')
                            r.talk('CAN I READ THIS MAIL?')
                            reply2 = r.get_info()
                            if (reply2 == "yes" or reply2 == "s"):
                                if msg.is_multipart():
                                    error = 0
                                    for part in msg.walk():
                                        content_type = part.get_content_type()
                                        content_disposition = str(part.get("Content-Disposition"))
                                        try:
                                            r.body = part.get_payload(decode=True).decode()

                                        except:

                                            error = error + 1
                                            if error == 2:
                                                content_type = "text/html"

                                        if content_type == "text/plain" and "attachment" not in content_disposition:
                                            print(r.body)
                                            r.talk(r.body)
                                            r.talk("CAN I OPEN LINK IF CONTAINS")
                                            reply3 = r.get_info()
                                            if (reply3 == "yes" or reply3 == "s"):
                                                try:
                                                    url = re.search("(?P<url>https?://[^\s]+)", body).group("url")
                                                    print(url)
                                                    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

                                                    webbrowser.get(chrome_path).open(url)
                                                except:
                                                    print("no link found!")
                                                    r.talk("no link found!")
                                                home.ask("",username,password)
                                            elif reply3 == "no":
                                                r.talk("can i read next mail ")
                                                reply4 = r.get_info()
                                                if reply4 == "no":
                                                    r.talk("stopped thank you ")
                                                    home.ask("",username,password)
                                                elif (reply4 == "yes" or reply4 == "s"):
                                                    break


                                        elif content_type == "text/html":
                                            print("Body of this mail not readable")
                                            r.talk("Body of this mail not readable")
                                else:
                                    print("Body of this mail not readable")
                                    r.talk("Body of this mail not readable")
                            elif reply2 == "no":
                                r.talk("continuing")
                        elif reply == "no":
                            r.talk("reading next mail")
r = read()

