import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "your_email"
sender_password = "your_password"
subject = 'Audition Invitation'

message_template = '''

Dear {recipient_name},

Thank you for signing up for the 9th International Music Festival. We are delighted to inform you of your auditioin details as below: 

Date: 27.02.24
Time: {recipient_timeslot}
Venue: Room 303

Kindly reply to this email ASAP to indicate your availability for the audition.

Best Regards,
Event Management Team
'''

recipient_data = pd.read_excel('recipient_data.xlsx')

# Connect to the SMTP server
smtp_server = "smtp.gmail.com"
smtp_port = 587

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    for index, row in recipient_data.iterrows():
        name = row['Name']
        email = row['Email']
        timeslot = row['Timeslot']

        # Create a new email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = email
        message['Subject'] = subject

        # Replace placeholders in the message template with actual data
        email_content = message_template.format(
            recipient_name=name,
            recipient_timeslot=timeslot
        )

        # Attach the email body as plain text
        message.attach(MIMEText(email_content, 'plain'))

        # Send the email
        server.sendmail(sender_email, email, message.as_string())
        print(f"Email sent to {name}")

    # Disconnect from the SMTP server
    server.quit()

    print("All emails sent successfully!")

except smtplib.SMTPException as e:
    print(f"Error: {str(e)}")