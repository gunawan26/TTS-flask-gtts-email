import imaplib
import email
import smtplib
import Tts


nama_email = "testtts2019@gmail.com"
password = "nlptc2019"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

def read_msg(msg):

    for part in msg.walk():
        if part.get_content_type()=="text/plain":
            body = part.get_payload()
            return body
    pass

def read_email():


    my_mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    my_mail.login(nama_email, password)
    my_mail.select('inbox')

    type_email, data = my_mail.search(None, 'ALL')

    mail_ids = data[0]
    id_list = mail_ids.split()

    latest_email_id = int(id_list[-1])
    first_email_id = int(id_list[0])
    value_to_return = []

    for i in range(latest_email_id, first_email_id, -1):
        result, data = my_mail.fetch(str(i), '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                dict_value = {}
                msg = email.message_from_string(response_part[1].decode('utf8'))
                # print(msg)
                email_subject = msg['subject']
                email_from = msg['from']
                body = read_msg(msg)
                sender = 'From : ' + email_from
                subject_email = 'Subject : ' + email_subject

                dict_value['from'] = email_from.rstrip()
                dict_value['subject'] = email_subject.rstrip()
                dict_value['content'] = body.rstrip()
                dict_value['speech'] = "An Email From "+email_from.rstrip()\
                                       +", email subject is "+ email_subject.rstrip()\
                                       +", is talk about "+body.rstrip()

                value_to_return.append(dict_value)


    return value_to_return

if __name__=="__main__":
  read_email()