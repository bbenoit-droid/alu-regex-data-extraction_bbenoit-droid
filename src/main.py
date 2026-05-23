import re
import json

#  let me fetch the data from the rwa-text file
with open("../input/raw-text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Regex patterns

# 1. Extract all email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
alu_pattern = r'^[A-Za-z0-9._%+-]+@alueducation\.com$'
alumni_pattern = r'^[A-Za-z0-9._%+-]+@alumni\.alueducation\.com$'
si_pattern = r'^[A-Za-z0-9._%+-]+@si\.alueducation\.com$'

print("Extracting email addresses...")
emails = re.findall(email_pattern, text)
print(f"Found {len(emails)} email addresses.")