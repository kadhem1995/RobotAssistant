import smtplib
import os
email_address=os.environ.get('robotassistantkadhem@gmail.com')
email_password=os.environ.get('kadhem1995')
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(email_address, email_password)
	subject='hello world'
	body='first massage with python language'
	msg=f'Subject:{subject}\n\n{body}'
	smtp.sendmail(email_address,'kadhemaniabi0@gmail.com',msg)

