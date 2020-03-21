# Python program to illustrate
# Matching regex objects
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is +91-415-555-4242')
print('Phone number found: ', mo.groups())
