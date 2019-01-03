from flask import Flask, render_template
from flask_gtts import gtts
import GmailConnector

app = Flask(__name__)
gtts(app=app,temporary=True, # to remove audio files on exit
    tempdir='static/', # relative path in-which audio files will be stored
    route=False) # opens route on /gtts that takes /language/text as args to return gtts mp3 link)


# inboxs=[
#         {
#             'from':'gkadek1998@gmail.com',
#             'subject':'testing',
#             'content':'hi, how are you doing'
#         },
#         {
#             'from':'gkadek1998@gmail.com',
#             'subject':'testing',
#             'content':'hi, how are you doing,glad to see you in this summer i hope we can met in indonesia right ?'
#         }
#     ]

inboxs=GmailConnector.read_email()


@app.route("/")
def hello():
    return render_template('index.html',inboxs = inboxs)




if __name__=="__main__":

    app.run(debug=True)