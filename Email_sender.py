## __AUTHOR__   :   BalaKiranKumar
#  require Modules to be installed
# pip install smtplib
# pip install imghdr

import os
import smtplib
import imghdr
from email.message import EmailMessage
EMAIL_ADDRESS=os.environ.get('Email_mail')
EMAIL_PASSWORD=os.environ.get('Email_pass')
a=1
count=0
while a :
	path=input("Enter path to switch the directory :\t")
	while True :
		try :
			os.chdir(path)
			break
		except :
			print("Enter the path correctly which is existing!!!")
	for i in os.listdir():
		print(i)
	print("1: NORMALFILE or videos\n2: PortableDocumentFormat\n3: IMAGE\n4: For Empty Message")
	print("Enter your choice to send which type :\t")
	file_choice=int(input())
	while True :
		if file_choice in [1,2,3,4] :
			print("Valid choice")
			break
		else :
			print("Make sure you enter the correct choice.")
	print("1: For uploading multiple files \n2:for Manualy")
	multifiles=int(input("Enter"))
	if multifiles == 1:
		file_extension=input("Enter file extension : \t")
	comp_upload=[]
	if multifiles == 1:
		for i in os.listdir():
			if i.endswith(file_extension): 
				comp_upload.append(i)
		manual_upload=[]
	if multifiles == 2 :
		manual_upload=input("enter filenames seperated by Double spaces :\t").split()
		file_extension=""
	
	
	files_upload=comp_upload+manual_upload
	
	#msg composing
	if count == 0:
		contacts = input("Enter reciever names by seperated by space :\t").split()
		subject_in= input("Enter the subject :\t")
		content_in= input("enter the Body to insert :\t")
		msg = EmailMessage()
		msg['Subject'] = subject_in
		msg['From'] = EMAIL_ADDRESS
		msg['To'] = contacts
		msg.set_content(content_in)

	#normal files
	if file_choice == 1 :
		for item in files_upload:
			if multifiles == 1:
				if item.endswith(file_extension) :
					with open(item,'rb') as normal_file:
						file_data=normal_file.read()
						file_name=normal_file.name
					# normal file
					msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=file_name)
			else:
				with open(item,'rb') as normal_file:
					file_data=normal_file.read()
					file_name=normal_file.name
				# normal file
				msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=file_name)

	# PDF files
	if file_choice == 2 :
		for item in files_upload:
			if item.endswith(file_extension) :
				with open(item,"rb") as pdf:
					pdf_data=pdf.read()
					pdf_name=pdf.name
				# pdf
				msg.add_attachment(pdf_data,maintype="application",subtype="octet-stream",filename=pdf_name)
			else:
				with open(item,'rb') as normal_file:
					file_data=normal_file.read()
					file_name=normal_file.name
				# normal file
				msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=file_name)
		
	#IMAGE FILES
	if file_choice == 3 :
		for item in files_upload:
			if item.endswith(file_extension) :
				with open(item,'rb') as image:
					image_data=image.read()
					image_type=imghdr.what(image.name)
					image_name=image.name
				# image
				msg.add_attachment(image_data,maintype="image",subtype=image_type,filename=image_name)
			else:
				with open(item,'rb') as normal_file:
					file_data=normal_file.read()
					file_name=normal_file.name
				# normal file
				msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=file_name)
	if file_choice == 4 :
		print("The content is shown in body that,s it")
	print("If u wanna add more attachments press 1\n wanna quit press 0")
	a=int(input("Enterr choice :\t"))
	count+=1
	
print("Composing Gmail to {0} from {1}'s account".format(contacts,EMAIL_ADDRESS))
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	smtp.send_message(msg)
print("Task Accomplished with Sending Gmails")