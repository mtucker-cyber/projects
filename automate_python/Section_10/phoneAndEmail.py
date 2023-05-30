#! python3

import re
import pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional)
(\s|-)                      # first seperator
\d\d\d                      # first 3 digits
(\s|-)                      # second seperator
\d\d\d\d                    # last 4 digits
((ext(\.)?\s|x) (\d{2,5}))? # extension (optional)
) 
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''

[A-Za-z0-9_.+-]+            # name
@                           # @ symbol
[A-Za-z0-9-.+-]+            # domain name part 

''', re.VERBOSE)
# Get the text of the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractPhone = phoneRegex.findall(text)
extractEmail = emailRegex.findall(text)

allPhone = []
for phoneNumber in extractPhone:
    allPhone.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhone) + '\n' + '\n'.join(extractEmail)
pyperclip.copy(results)