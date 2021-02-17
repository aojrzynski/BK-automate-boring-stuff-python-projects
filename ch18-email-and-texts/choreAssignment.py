#! python3
# choreAssignment.py - Randomly assigns chores to a list of emails, and sends out notificatin emails regarding those chores.
#
# NOTES: Once the program runs, please provide your email password. This program will run once a week for ten weeks.

import smtplib, random, time, getpass

# Get email credentials. 
user_email = 'example@example.com'
user_password = getpass.getpass('Please enter your email password:') # Using getpass means the password is input securely.

# Assign chore and send email.
def choreAssignment():
    chores = ['kitchen','bathroom','living room', 'garage']

    for email in emails:
        randomChore = random.choice(chores)
        chores.remove(randomChore)

        message = str('Subject: Weekly Chores\n Your chore for this week is: ' + randomChore + '.')
        print(email + ' : ' + randomChore)
        smtpObj.sendmail(user_email, email, message)

emails = ['example1@gexample.com', 'example2@gexample.com', 'example3@gexample.com', 'example4@gexample.com']

# Connect to the email, run the function 'choreAssignment' and disconnect from the email. Repeat every week for ten weeks.
for i in range(10):
    smtpObj = smtplib.SMTP('smtp.example.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(user_email, user_password)
    choreAssignment()
    smtpObj.quit()
    time.sleep(86400 * 7)


