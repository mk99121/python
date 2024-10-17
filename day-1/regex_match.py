import re

text = "brown fox is like a dog"
pattern = r"brown"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

 # re.match() only checks for a match at the beginning of the string.