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

# print("Extracting email addresses...")
# emails = re.findall(email_pattern, text)
# # print(f"Found {len(emails)} email addresses.")
# print(f"Found email addresses : {(emails)} .")
# with open("../output/sample-output.json", "w", encoding="utf-8") as f:
#     json.dump(emails, f, indent=4)  


credit_card_pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
url_pattern = r'https?://[^\s]+'
phone_pattern = r'(\+\d{1,3}\s?)?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{3,4}'

print("Extracting credit cards...")
credit_card = re.findall(credit_card_pattern, text)
print(f"Found {len(credit_card)} credit cards.")
print(f"Found credit cards : {(credit_card)} .")
with open("../output/sample-output.json", "w", encoding="utf-8") as f:
    json.dump(credit_card, f, indent=4)  