import random

email = ''
nick = ''
password = ''
for i in range(8):
	password += random.choice('ABCDEFGHIGKLMNOPQRSTUVYXWZabcdefghigklmnopqrstuvyxwz1234567890')
	nick += random.choice('ABCDEFGHIGKLMNOPQRSTUVYXWZabcdefghigklmnopqrstuvyxwz')
	email += random.choice('ABCDEFGHIGKLMNOPQRSTUVYXWZabcdefghigklmnopqrstuvyxwz1234567890')

email = email+'@gmail.com'

# print(password)
# print(nick)
# print(email)


