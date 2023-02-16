from app2 import  password #this password is password of your email app password
import smtplib, ssl # this library help to send mail via machine 
from email.message import EmailMessage # this help to structure messsage

smtp_server = "smtp.gmail.com"# smtp stand for (send mail tranfer protocols )
port = 587  # For starttls
sender_email = "ritikdummymail@gmail.com"
receiver_email = str(input("Enter the reciver mail to send Email ! : "))
password = password
# message = "hy new mail arrie just recentel send directr message also  " 

subject = input(" Enter Subject of Email ! : ") # making due to email.message
body = input("Enter the body content of EmaIL ! : ")

# structure content of mail 

em = EmailMessage()
em['From'] = sender_email
em['To'] = receiver_email
em['subject'] = subject
em.set_content(body)


# Create a secure SSL context ( secure socket layer )
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    print("We are Succefully Login to Server ! : ")
    server.sendmail(sender_email , receiver_email , em.as_string())
    print("Succefully send Mails ! : ")
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print("Some erro Came due to fail server ! : ")
finally:
    server.quit()
    print(" Succefully Log out Fro the Server ! : ")