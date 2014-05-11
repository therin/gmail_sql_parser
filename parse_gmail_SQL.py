# -*- coding: utf-8 -*-
import pyodbc
import imaplib
import smtplib
import email
import re
import pickle
raw_mails = []
mails = []
new_ids_to_fetch = []
my_full_list = []
picture_full_list = []
sql_final_result = []
output = []
updated_final_list = []
updated_picture_list = []
sql_picture_final_result = []

def check_email_type(ids):
	mail1 = imaplib.IMAP4_SSL('imap.gmail.com')
	mail1.login('test@test.biz', 'your_password')
	mail1.list()
	mail1.select("inbox") # connect to inbox.
	result, data = mail1.uid('fetch', ids, '(RFC822)')
	raw_email = data[0][1]
	email_message = email.message_from_string(raw_email)
	if "PictureGUID" in str(email_message):
		return "Picture"
	else:
		return "Normal"


def parse_picture_email(ids2):
	mail1 = imaplib.IMAP4_SSL('imap.gmail.com')
	mail1.login('test@test.biz', 'your_password')
	mail1.list()
	mail1.select("inbox") # connect to inbox.
	something = []
	result, data = mail1.uid('fetch', ids2, '(RFC822)')
	raw_email = data[0][1]
	email_message = email.message_from_string(raw_email)
	PictureGUID = re.search(r'(PictureGUID\",\")([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})',email_message.get_payload(decode=True))
	if PictureGUID == None:
		PictureGUID_1 = 'Nothing'
	else:
		PictureGUID_1 = PictureGUID.group(2)
	something.append(PictureGUID_1)
	CompanyId = re.search(r'(CompanyId\",\")([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})',email_message.get_payload(decode=True))
	if CompanyId == None:
		CompanyId_1 = 'Nothing'
	else:
		CompanyId_1 = CompanyId.group(2)
	something.append(CompanyId_1)
	TestGuid = re.search(r'(TestGuid\",\")([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})',email_message.get_payload(decode=True))
	if TestGuid == None:
		TestGuid_1 = 'Nothing'
	else:
		TestGuid_1 = TestGuid.group(2)
	something.append(TestGuid_1)
	Description = re.search(r'(Description\",\")([^"]*)',email_message.get_payload(decode=True))
	if Description == None:
		Description_1 = 'Nothing'
	else:
		Description_1 = Description.group(2)
	something.append(Description_1)
	Geolocation = re.search(r'(Geolocation\",\")([^"]*)',email_message.get_payload(decode=True))
	if Geolocation == None:
		Geolocation_1 = 'Nothing'
	else:
		Geolocation_1 = Geolocation.group(2)
	something.append(Geolocation_1)
	CreatedDate = re.search(r'(CreatedDate\",\")([^"]*)',email_message.get_payload(decode=True))
	if CreatedDate == None:
		CreatedDate_1 = 'Nothing'
	else:
		CreatedDate_1 = CreatedDate.group(2)
	something.append(CreatedDate_1)
	CreatedBy = re.search(r'(CreatedBy\",\")([^"]*)',email_message.get_payload(decode=True))
	if CreatedBy == None:
		CreatedBy_1 = 'Nothing'
	else:
		CreatedBy_1 = CreatedBy.group(2)
	something.append(CreatedBy_1)
	return something

def parse_normal_email(ids2):
	mail1 = imaplib.IMAP4_SSL('imap.gmail.com')
	mail1.login('sergey@smarttrade.biz', '!Qazxsw2')
	mail1.list()
	mail1.select("inbox") # connect to inbox.
	something = []
	result, data = mail1.uid('fetch', ids2, '(RFC822)')
	raw_email = data[0][1]
	email_message = email.message_from_string(raw_email)
	address = re.search(r'(Address\",\")([^"]*)',email_message.get_payload(decode=True))
	if address == None:
		address_1 = 'Nothing'
	else:
		address_1 = address.group(2)
	something.append(address_1)
	AssetDescription = re.search(r'(AssetDescription\",\")([^"]*)',email_message.get_payload(decode=True))
	if AssetDescription == None:
		AssetDescription_1 = 'Nothing'
	else:
		AssetDescription_1 = AssetDescription.group(2)
	something.append(AssetDescription_1)
	assetguid = re.search(r'(AssetGuid\",\")([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})',email_message.get_payload(decode=True))
	if assetguid == None:
		assetguid_1 = 'Nothing'
	else:
		assetguid_1 = assetguid.group(2)
	something.append(assetguid_1)
	testguid = re.search(r'(TestGuid\",\")([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})',email_message.get_payload(decode=True))
	if testguid == None:
		testguid_1 = 'Nothing'
	else:
		testguid_1 = testguid.group(2)
	something.append(testguid_1)
	DateTime = re.search(r'(DateTime\",\")([^"]*)',email_message.get_payload(decode=True))
	if DateTime == None:
		DateTime_1 = 'Nothing'
	else:
		DateTime_1 = DateTime.group(2)
	something.append(DateTime_1)
	Geolocation = re.search(r'(Geolocation\",\")([^"]*)',email_message.get_payload(decode=True))
	if Geolocation == None:
		Geolocation_1 = 'Nothing'
	else:
		Geolocation_1 = Geolocation.group(2)
	something.append(Geolocation_1)
	LoginName = re.search(r'(LoginName\",\")([^"]*)',email_message.get_payload(decode=True))
	if LoginName == None:
		LoginName_1 = 'Nothing'
	else:
		LoginName_1 = LoginName.group(2)
	something.append(LoginName_1)
	LoginRealName = re.search(r'(LoginRealName\",\")([^"]*)',email_message.get_payload(decode=True))
	if LoginRealName == None:
		LoginRealName_1 = 'Nothing'
	else:
		LoginRealName_1 = LoginRealName.group(2)
	something.append(LoginRealName_1)
	Premises = re.search(r'(Premises\",\")([^"]*)',email_message.get_payload(decode=True))
	if Premises == None:
		Premises_1 = 'Nothing'
	else:
		Premises_1 = Premises.group(2)
	something.append(Premises_1)
	Remarks = re.search(r'(Remarks\",\")([^"]*)',email_message.get_payload(decode=True))
	if Remarks == None:
		Remarks_1 = 'Nothing'
	else:
		Remarks_1 = Remarks.group(2)
	something.append(Remarks_1)
	Test = re.search(r'(Test\",\")([^"]*)',email_message.get_payload(decode=True))
	if Remarks == None:
		Test_1 = 'Nothing'
	else:
		Test_1 = Test.group(2)
	something.append(Test_1)
	TestResult = re.search(r'(TestResult\",\")([^"]*)',email_message.get_payload(decode=True))
	if TestResult == None:
		TestResult_1 = 'Nothing'
	else:
		TestResult_1 = TestResult.group(2)
	something.append(TestResult_1)
	Urgent = re.search(r'(Urgent\",\")([^"]*)',email_message.get_payload(decode=True))
	if Urgent == None:
		Urgent_1 = 'Nothing'
	else:
		Urgent_1 = Urgent.group(2)
	something.append(Urgent_1)
	TickRemarks = re.search(r'(TickRemarks\",\")([^"]*)',email_message.get_payload(decode=True))
	if TickRemarks == None:
		TickRemarks_1 = 'Nothing'
	else:
		TickRemarks_1 = TickRemarks.group(2)
	something.append(TickRemarks_1)
	TickDefects = re.search(r'(TickDefects\",\")([^"]*)',email_message.get_payload(decode=True))
	if TickDefects == None:
		TickDefects_1 = 'Nothing'
	else:
		TickDefects_1 = TickDefects.group(2)
	something.append(TickDefects_1)
	TickIsolations = re.search(r'(TickIsolations\",\")([^"]*)',email_message.get_payload(decode=True))
	if TickIsolations == None:
		TickIsolations_1 = 'Nothing'
	else:
		TickIsolations_1 = TickIsolations.group(2)
	something.append(TickIsolations_1)
	PFA = re.search(r'(PFA\",\")([^"]*)',email_message.get_payload(decode=True))
	if PFA == None:
		PFA_1 = 'Nothing'
	else:
		PFA_1 = PFA.group(2)
	something.append(PFA_1)
	CompanyId = re.search(r'(CompanyId\",\")([^"]*)',email_message.get_payload(decode=True))
	if CompanyId == None:
		CompanyId_1 = 'Nothing'
	else:
		CompanyId_1 = CompanyId.group(2)
	something.append(CompanyId_1)
	return something

def get_email_body(ids):
	mail2 = imaplib.IMAP4_SSL('imap.gmail.com')
	mail2.login('test@test.biz', 'your_password')
	mail2.list()
	mail2.select("inbox") # connect to inbox.
	result, data = mail2.uid('fetch', ids, '(RFC822)')
	raw_email = data[0][1]
	email_message = email.message_from_string(raw_email)
	some = email_message.get_payload()
	return some

def send_normal_email(output,ids):
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login("test@test.biz", "your_password")
	sender = 'test@test.biz'
	recipient = 'test@test.biz'
	subject = 'Standart SmartForms Error Report'
	body = '\n' + output + "<br><br><br><br>" + "<b>" + "Original email text:" + "</b>" + "<br><br>" + str(get_email_body(ids))
	headers = ["From: " + sender,"Subject: " + subject,"MIME-Version: 1.0","Content-Type: text/html"]
	headers = "\r\n".join(headers)
	server.sendmail(sender, recipient, headers + "\r\n\r\n" +  body)
	server.quit()

def query_picture(results):
	ending = []
	cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=yk75jbqq0x.database.windows.net;DATABASE=SmartTrade;UID=stadmin@yk75jbqq0x;PWD=Azure-44')
	cursor = cnxn.cursor()
	cursor.execute("SELECT [Id],[CompanyId],[TestGuid],[Description],[Geolocation],[CreatedDate],[CreatedBy],[Picture] \
    	FROM dbo.sf_Picture WHERE id=? and companyid=? and testguid=?",results[0],results[1],results[2])
	row = cursor.fetchone()
	if row == None:
		return row
	else:
		for i in row:
		    ending.append(str(i))
		return ending

def query_normal(results):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=yk75jbqq0x.database.windows.net;DATABASE=SmartTrade;UID=stadmin@yk75jbqq0x;PWD=Azure-44')
    cursor = cnxn.cursor()
    cursor.execute("SELECT [Address],[AssetDescription],[AssetGuid],[DateTime],[Geolocation],[LoginName],[LoginRealName],[Premises], \
	           [Remarks],[Test],[TestResult],[Urgent],[TickRemarks],[TickDefects],[TickIsolations],[PFA],[CompanyId] \
	           FROM	sf_testresult WHERE assetguid=? and testguid=? \
	           and companyid=?",results[0],results[1],results[2])
    row = cursor.fetchone()
    ending = []
    for i in row:
    	ending.append(i)
    return ending

def picture_comparison(my_full_list_entry,sql_final_result):
	modified_full_list_entry = []
	modified_full_list_entry.append(my_full_list_entry[1])
	internal_list = []
	for i in range(len(modified_full_list_entry)):
		for entry1, entry2 in zip(modified_full_list_entry[i], sql_final_result):
			if entry1.lower() != entry2.lower():
				result = "\""+ entry1+ "\"" + "  <font color=\"red\">is different from</font>  " + "\""+ entry2+ "\""
			else:
				result = "\""+entry1+"\"" + "  <font color=\"green\">is the same as</font>  " + "\""+entry2+"\""
			internal_list.append(result)
	return internal_list

def normal_comparison(my_full_list_entry,sql_final_result):
	modified_full_list_entry = []
	modified_full_list_entry.append(my_full_list_entry[1])
	internal_list = []
	for entry in modified_full_list_entry:
		del entry[3]
	for i in range(len(modified_full_list_entry)):
		for entry1, entry2 in zip(modified_full_list_entry[i], sql_final_result):
			if entry1.lower() != entry2.lower():
				result = "\""+ entry1+ "\"" + "  <font color=\"red\">is different from</font>  " + "\""+ entry2+ "\""
			else:
				result = "\""+entry1+"\"" + "  <font color=\"green\">is the same as</font>  " + "\""+entry2+"\""
			internal_list.append(result)
	return internal_list



mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('sergey@smarttrade.biz', '!Qazxsw2')
mail.list()
mail.select("inbox") # connect to inbox.

result, data = mail.uid('search', None, '(FROM "smartforms@smarttrade.biz" HEADER Subject "Cloud Exception Details")')
fetch_ids2 = data[0].split()


try:
	with open("full_result.txt", 'rb') as f:
		my_list = pickle.load(f)
except:
	my_list = []
	print "No result file"
	pass
for i in fetch_ids2:
	if i not in my_list:
		new_ids_to_fetch.append(i)
		my_list.append(i)
print "Found new mail" + " " + str(new_ids_to_fetch)
with open("full_result.txt", 'wb') as f:
    pickle.dump(my_list, f)

for ids2 in new_ids_to_fetch:
	print ids2
	if check_email_type(ids2) == "Picture":
		print "It's a picture type email"
		entry = parse_picture_email(ids2)
		if query_picture((entry[0],entry[1],entry[2])) == None:
			print "Query returned zero results"
			output123 = "Hi Everyone," + "<br><br>" + "<b>" + "Query returned zero results" + "</b>"
			send_normal_email(output123,ids2)
		else:
		    picture_full_list.append((ids2,parse_picture_email(ids2)))
	else:
		my_full_list.append((ids2,parse_normal_email(ids2)))


for i, (ids,entry) in enumerate(picture_full_list):
	try:
		if "Nothing" in entry:
		    print "One of the guids is missing"
		    output123 = "Hi Everyone," + "<br><br>" + "<b>" + "TestGuid is missing in this email" + "</b>"
		    send_normal_email(output123,ids)
		else:
			sql_picture_final_result.append(query_picture((entry[0],entry[1],entry[2])))
			updated_picture_list.append((ids,entry))
	except:
		print "Nothing to check"
        pass

for i, (ids,entry) in enumerate(my_full_list):
	try:
	    if "Nothing" in entry:
		    print "One of the guids is missing"
		    output123 = "Hi Everyone," + "<br><br>" + "<b>" + "TestGuid is missing in this email" + "</b>"
		    send_normal_email(output123,ids)	
	    else:
	    	sql_final_result.append(query_normal((entry[2],entry[3],entry[17])))
	    	updated_final_list.append((ids,entry))
	except:
		print "Nothing to check"
    	pass

for i in range(len(sql_picture_final_result)):
    send_normal_email('<br><br>'.join(picture_comparison(updated_picture_list[i],sql_picture_final_result[i])), updated_picture_list[i][0])
for i in range(len(sql_final_result)):
	send_normal_email('<br><br>'.join(normal_comparison(updated_final_list[i],sql_final_result[i])), updated_final_list[i][0])
