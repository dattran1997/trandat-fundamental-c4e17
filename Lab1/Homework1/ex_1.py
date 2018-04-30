from gmail import GMail, Message
from random import choice
from datetime import *

boolean = True
while boolean:
    #random noi dung
    sickness_list = ["ốm", "sốt", "táo bón"]
    sickness = choice(sickness_list)

    #nội dung
    html_template ='''<p>Anh ơi h&ocirc;m nay em bị <span style="color: #000000;">{{ốm}}</span> qu&aacute; kh&ocirc;ng đi học được, a cho e nghỉ buổi h&ocirc;m nay nh&eacute;, e hứa sẽ kh&ocirc;ng học v&agrave; ch&eacute;p b&agrave;i đầy đủ đ&acirc;u :))</p>
    <p>&lt;&lt;-th&acirc;n:<span style="color: #0000ff;">Annonymous</span>-&gt;&gt;</p>'''
    html_content = html_template.replace("{{ốm}}",sickness)

    #connect GMail
    GMail = GMail('<dattran1997@gmail.com>','Socchuot297')
    msg = Message('Đơn xin nghỉ ốm',to='<datgato1997@gmail.com>',html = html_content)

    now = datetime.now()
    hour = now.hour
    minute = now.minute

    if (hour >= 7 and minute > 0) :
        GMail.send(msg)
        boolean = False
