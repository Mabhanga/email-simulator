class Email:
    Inbox = []

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True

def populate_inbox():
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Thank you for joining us.")
    email2 = Email("sender2@example.com", "Great work on the bootcamp!", "You're doing an amazing job.")
    email3 = Email("sender3@example.com", "Your excellent marks!", "Congratulations on your achievements.")
    Email.Inbox.append(email1)
    Email.Inbox.append(email2)
    Email.Inbox.append(email3)

def list_emails():
    for index, email in enumerate(Email.Inbox):
        print(f"{index} {email.subject_line}")

def read_email(index):
    email = Email.Inbox[index]
    print(f"\nEmail from {email.email_address}:\nSubject: {email.subject_line}\nContent: {email.email_content}\n")
    email.mark_as_read()

populate_inbox()

while True:
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")
    choice = input("Enter your choice: ")

    if choice == "1":
        list_emails()
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
        print(f"\nEmail from {Email.Inbox[index].email_address} marked as read.\n")
    elif choice == "2":
        unread_emails = [email for email in Email.Inbox if not email.has_been_read]
        print("Unread emails:")
        for email in unread_emails:
            print(email.subject_line)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")


