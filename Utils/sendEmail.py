# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 07:36:00 2022

@author: damba
"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email, smtplib
from datetime import datetime
from datetime import date

from Checkatrade.Configs.emailConfig import *


def sendEmail(table_contents):
	email_subject = format(datetime.now(),'%d-%B-%Y') + " : Oldest Character by Film "

	message = MIMEMultipart("alternative")
	message["Subject"] = email_subject
	message["From"] = EMAIL_FROM
	message["To"] = EMAIL_TO
    
	# write the HTML part
	if len(table_contents) >0:
		html = """\
	<!DOCTYPE html><html><head><style>
	#customers {  font-family: Arial, Helvetica, sans-serif;  border-collapse: collapse;  width: 70%;}
	#customers td, #customers th { align="middle"  ; border: 1px solid #ddd;  padding: 3px;}
	#customers tr { align="middle" ;text-align: center;  }
	#customers th {  padding-top: 3px; padding-bottom: 3px;  text-align: center;  background-color: #4CAF50;  color: white;}
	</style>
	</head><body><p>Hi Team,</p><p><t><br>	Please find the Oldest Character by Film  </p><table id="customers">
	 <thead>
    <tr style="text-align: right;">
	<th>FILM Title</th>
      <th>Character Name</th>
    
      
    </tr>
  </thead>
""" +	str(table_contents)		+"""
	</table>
	<p>------------------------------------<p>
	<p>	Thanks, </p>
	<p>GDPR Team </p>
	</body>
	</html> """
	else:
		html= """\
	<!DOCTYPE html><html><head><style>
	#customers {  font-family: Arial, Helvetica, sans-serif;  border-collapse: collapse;  width: 70%;}
	#customers td, #customers th { align="middle"  ; border: 1px solid #ddd;  padding: 3px;}
	#customers tr { align="middle" ;text-align: center;  }
	#customers th {  padding-top: 3px; padding-bottom: 3px;  text-align: center;  background-color: #4CAF50;  color: white;}
	</style>
	</head><body><p>Hi Team,</p><p><t><br>	There is no relevant data available   </p>
	<br><p></br>
	<p></p></p>
			<p>------------------------------------<p>
	<p>	Thanks, </p>
	<p>GDPR Team </p>
	</body>
	</html> 
		"""

	part2 = MIMEText(html, "html")
	
	message.attach(part2)
	# send your message
	with smtplib.SMTP(SMTP_SERVER) as server:
		server.sendmail(EMAIL_FROM, EMAIL_TO, message.as_string())

	print('Email Sent') 