import imaplib
import email
from home import home
from email.header import decode_header


def dell(username,password):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    imap.select("INBOX")
    status, messages = imap.search(None, "ALL")
    messages = messages[0].split(b' ')

    for mail in messages:
        _, msg = imap.fetch(mail, "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                email_from = msg['from']
                print("from:"+email_from+'\n')
                home.talk("","from:"+email_from+'\n')
                subject = decode_header(msg["Subject"])[0][0]

                if isinstance(subject, bytes):
                    subject = subject.decode()
                print("subject:"+subject+'\n')
                home.talk("","subject:"+subject+'\n')
                data = home.mic("","can i delete this mail?")
                if data == "yes" or data == "s":
                    home.talk("","deleting mail of subject:" + subject + '\n')
                    imap.store(mail, "+FLAGS", "\\Deleted")
                    print("deleted")
                    home.talk("","deleted")
                elif data == "no":
                    print(" reading next mail")
                    home.talk("", "reading next mail")
                elif data =="stop":
                    home.ask("",username,password)