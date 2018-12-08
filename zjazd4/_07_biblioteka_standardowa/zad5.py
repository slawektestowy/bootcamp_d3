import re

# kodów pocztowych - 12-123
# '[0-9]{2}-[0-9]{3}'
# '\d{2}-\d{3}'
# adresów email - test@email.com
# [0-9a-zA-Z]+@(?:[0-9a-zA-Z]+\.)+[0-9a-zA-Z]+
# daty 12 Jan 1990

post_pattern = re.compile('\d{2}-\d{3}')
email_pattern = re.compile('[\w-]+@(?:[\w-]+\.)+\w+')
date_pattern = re.compile('\d{1,2} \w{3} \d{4}')

with open('input.txt','r') as f:
    data = f.read()

wystapienia = post_pattern.findall(data)
print(len(wystapienia),wystapienia)
wystapienia = email_pattern.findall(data)
print(len(wystapienia),wystapienia)
wystapienia = date_pattern.findall(data)
print(len(wystapienia),wystapienia)

