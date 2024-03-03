# Mass Email Automation Project

This project automates the process of sending personalized emails for music festival audition invitations. It utilizes the `smtplib` library to connect to an SMTP server, `pandas` library to read recipient data from a CSV file, and the `email` library to compose and send emails.

## Prerequisites

Before running the project, make sure you have the following:

- Python 3 installed on your system
- `smtplib` library installed (`pip install secure-smtplib`)
- `pandas` library installed (`pip install pandas`)

## Usage

1. Update the `sender_email` and `sender_password` variables with your email address and [app-specific password](https://support.google.com/accounts/answer/185833?hl=en) generated for your email account.
2. Modify the `subject` and `message_template` variables to customize the email subject and content.
3. Ensure you have a recipient data file in the same directory as the `src.py` file. The file should be in CSV format and contain columns for `Name`, `Email`, and `Timeslot`.
4. Run the `src.py` file to start sending the emails.

## Sample CSV File

A sample CSV file, `recipient_data.csv`, is provided to demonstrate the required format for the recipient data. Please update it with the actual recipient information before running the script.

## Note

- Make sure to enable access for less secure apps in your email account settings if required.
- The project is currently configured to use Gmail's SMTP server. If you're using a different email provider, update the `smtp_server` and `smtp_port` variables accordingly.
- Note that the `sender_password` variable should contain an app-specific password generated for your email account, rather than your actual Gmail password. You can generate an app-specific password by following the instructions provided by your email service provider.

Feel free to customize and enhance the project to fit your specific requirements. Contributions and improvements are welcome!

