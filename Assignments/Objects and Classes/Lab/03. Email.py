class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}'


emails = []
line = input()

while line != 'Stop':
    tokens = line.split(' ')
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()


send_emails = list(map(int, input().split(', ')))
for i in send_emails:
    emails[i].send()

for x in emails:
    print(x.get_info())
