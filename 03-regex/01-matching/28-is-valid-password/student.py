# Write your code here
import re

def is_valid_password(string):
    right_regex = [
        r'.{12,}',
        r'[0-9]+',
        r'[A-Z]+',
        r'[a-z]+',
        r'[-+*/.@]'
    ]

    bad_regex = [
        r'(.)\1{2}',
        r'(.)(.*\1){3}'
    ]

    for regex in right_regex:
        if not re.search(regex, string):
            return False
    for regex in bad_regex:
        if re.search(regex, string):
            return False
        
    return True