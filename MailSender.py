import smtplib as s
ob = s.SMTP("smtp.gmail.com",587)

ob.starttls()

ob.login("your_gmail@example.com", "yourgmail_password")

# Type subject and  body
subject ="Sending mail using python{from karan}"
body ="This is just testing"


message = "Subject:{}\n\n{}".format(subject, body)

# Type mail Address where to send mail{n-number of email's}
listOfAddress = ["rec1_gmail","rec2_gmail","rec3_gmail"]

ob.sendmail("your_gmail@example.com", listOfAddress, message)

print("send successfully...")
ob.quit()