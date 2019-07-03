import smtplib
 
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
 
smtp.login('(e-mail)', '(senha)')
 
de = '(e-mail_origem)'
para = ['(e-mail_destino)']
msg = """From: %s
To: %s
Subject: Survey about Scratch Day Events
 
My name is (name), and I'm a student from Federal University of Technology - Parana, Brazil. I'm a member of the scientific project on children's education using Scratch and along with Professor Igor Wiese, we are studying about how Scratch can help to develop computational thinking.

We want to identify best practices used during the Scratch Days. 
In this sense, it would be of great help if you could spare 10 minutes to answer the following questionnaire: https://goo.gl/forms/VYPipMe10oOgrffF3

Your participation in answering the survey is greatly appreciated, but in no way required. The information that is collected will be used to develop tools, educational resources, and write up scientific papers. All results will be presented as summaries.

Your individual responses or any personal information about you will not be identifiable in any published reports of the data. Your IP address is not collected. There will be no follow-up.

If you provide your name in the last question of the survey, your identity will be made available only to us. However, you will not be identified in any reports of the data, nor will your identity be made available to anyone outside the research team.

Thank you so much for your time, and please do not hesitate in contacting me if you have any question. """ % (de, ', '.join(para))
 
smtp.sendmail(de, para, msg)
 
smtp.quit()
