# Write your code here
import re

def parse_link(string):
    match = re.fullmatch(r'(<a href=")(.+)(">)(.+)(</a>)',string)
    if (match):
        return (match.group(4), match.group(2))
    return None