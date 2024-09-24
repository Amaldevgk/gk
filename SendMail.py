import yagmail
import os
from dotenv import load_dotenv

load_dotenv()



sender = "devgk07@gmail.com"
reciever = "caudatxyh@emlpro.com"
subject ='test main using python'
contents = '''
this the content side for mail
'''

yag = yagmail.SMTP(user=sender,password=os.gentenv('PASSWORD'))
yag.send(to=reciever,subject=subject,contents=contents)
print("email send")


