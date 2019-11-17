import re
"""
It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is .
"""
def emailMainFormat(ls):
    list(ls)
    for emails in ls:
        print(emails)
        #emails.split(emails, "@")
        print(emails.findall(r"\w+", emails))

emailMainFormat(input().split())