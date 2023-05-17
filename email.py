from datetime import datetime


# creating my class

class Email:
    # initializing my constructors
    def __init__(self, from_address="", subject_line="", email_contents="", as_been_read=False, is_spam=False):
        self.address = from_address
        self.subject = subject_line
        self.message = email_contents
        self.read = as_been_read
        self.spam = is_spam
        self.timestamp = datetime.now()

    def mark_as_read(self):  # defining a method to change read to True
        self.read = True

    def mark_as_spam(self):  # defining a method to change spam to True
        self.spam = True

    # defining a method to display our email
    def __str__(self):
        return f"""
    From: {self.address} 
    Subject: {self.subject}
    Message: {self.message} 
    Read: {self.read}
    Spam: {self.spam}
    Time: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"""


# class to manipulate my inbox
class Inbox:
    messages = []

    def add_email(self, address, subject, message):
        new_email = Email(address, subject, message)
        self.messages.append(new_email)

    def list_messages_from_sender(self, sender_address):
        for i, index in enumerate(range(len(self.messages)), 1):
            if self.messages[index].address == sender_address:
                print(f"""{i} {self.messages[index].subject}""")

    def get_email(self):

        for count, i in enumerate(range(len(self.messages)), start=1):
            if self.messages[i].address == sender_address:
                print(f"""Email #: {count} 
    From: {self.messages[i].address} 
    Subject: {self.messages[i].subject}
    Read: {self.messages[i].read}
    Spam: {self.messages[i].spam}""")

        select = int(input("Enter the email number you'd like to view : "))

        collect = self.messages[select - 1]
        print(collect)
        Email.mark_as_read(collect)

    def mark_as_spam(self):
        # First, print out all the emails so the user can see which one they want to mark
        for count, i in enumerate(range(len(self.messages)), start=1):
            if self.messages[i].address == sender_address:
                print(f"""Email #: {count} 
        From: {self.messages[i].address} 
        Subject: {self.messages[i].subject}
        Read: {self.messages[i].read}
        Spam: {self.messages[i].spam}""")

        select = int(input("Please enter the index of the email to be marked as spam : "))

        collect2 = self.messages[select - 1]
        Email.mark_as_spam(collect2)

    def get_spam_emails(self):
        spam_emails = []
        for i in self.messages:
            if i.spam:
                spam_emails.append(i)

            output = ""

        for email in spam_emails:
            output += f"From: {email.address}\n"
            output += f"Subject: {email.subject}\n"
            output += f"Message: {email.message} \n"
        print(output)

    def get_unread_emails(self):
        unread_emails = []
        for a in self.messages:
            if not a.read:
                unread_emails.append(a)

            unread_output = ""

        for e in unread_emails:
            unread_output += f"From: {e.address}\n"
            unread_output += f"Subject: {e.subject}\n"
            unread_output += f"Message: {e.message} \n\n"
        print(unread_output)

    def delete(self):

        # First, print out all the emails so the user can see which one they want to delete
        for count, i in enumerate(range(len(self.messages)), start=1):
            if self.messages[i].address == sender_address:
                print(f"""Email #: {count} 
           From: {self.messages[i].address} 
           Subject: {self.messages[i].subject}
           Read: {self.messages[i].read}
           Spam: {self.messages[i].spam}""")

        # Ask the user which email they want to delete
        select = int(input("Please enter the index of the email to be deleted: "))

        # Delete the selected email will del statement
        del self.messages[select - 1]


# declared a variable to hold our Inbox class
inbox = Inbox()

# Manually adding email data to our program for review purpose
inbox.add_email("john@example.com", "Hello World", "Here is email content 1")
inbox.add_email("john@example.com", "Hello World2", "Here is email content 2")
inbox.add_email("john@example.com", "Hello World2", "Here is email content 3")
inbox.add_email("jane@example.com", "Python Programming", "Here is email content 2")

# declared a variable to hold time stamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
usage_message = f'''
{timestamp} | Welcome to the email system! 

What would you like to do today?
s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''

# An Email Simulation


user_choice = ""

while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":
        # Send an email (Create a new Email object)
        address = input("Please enter the address of the sender\n:")
        subject = input("Please enter the subject line of the email\n:")
        message = input("Please enter the contents of the email\n:")
        inbox.add_email(address, subject, message)

        # Now add the email to the Inbox

        # Print a success message
        print("Email has been added to inbox.")

        pass
    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input("Please enter the address of the sender\n:")
        print("View emails below\n")
        inbox.list_messages_from_sender(sender_address)

        # Now list all emails from this sender

        pass
    elif user_choice == "r":
        # Read an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        inbox.get_email()

        # Step 3: ask the user for the index of the email
        # refer to line 51

        # Step 4: display the email
        # refer to line 55

        pass
    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        inbox.mark_as_spam()

        # Step 3: ask the user for the index of the email
        # refer to line 67

        # Step 4: mark the email as spam
        # refer to line 70

        # Step 5: print a success message
        print("Email has been marked as spam")

        pass
    elif user_choice == "gu":
        print("View Unread emails below\n")
        # List all unread emails
        inbox.get_unread_emails()
        pass
    elif user_choice == "gs":
        print("View Spam emails below\n")
        # List all spam emails
        inbox.get_spam_emails()
        pass
    elif user_choice == "e":
        print("Goodbye")
        break
    elif user_choice == "d":
        # Delete an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        inbox.delete()

        # Step 3: ask the user for the index of the email
        # email_index = int(input("Please enter the index of the email to be deleted\n:"))

        # Step 4: delete the email

        # Step 5: print a success message
        print("Email has been deleted")

        pass
    else:
        print("Oops - Incorrect input")
