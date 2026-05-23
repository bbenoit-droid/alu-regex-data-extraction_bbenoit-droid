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
phone_pattern = r'(\+\d{3} \d{3} \d{3} \d{3}|\+\d{3} \(\d{3}\) \d{3}-\d{3}|\+\d{12})'



# print("Extracting credit cards...")
# credit_card = re.findall(credit_card_pattern, text)
# print(f"Found {len(credit_card)} credit cards.")
# print(f"Found credit cards : {(credit_card)} .")
# with open("../output/sample-output.json", "w", encoding="utf-8") as f:
#     json.dump(credit_card, f, indent=4)  

# security verification

# if you want to mask the credit card numbers in the output, you can use the following function:
# def mask_card(card):
#     digits = re.sub(r'\D', '', card)
#     return "*" * 12 + digits[-4:]

def is_safe_email(email):
    # block obvious fake patterns
    if ".." in email or "@@" in email or "<" in email:
        return False
    return True


# final extraction 

emails_raw = re.findall(email_pattern, text)
emails = [e for e in emails_raw if is_safe_email(e)]

alu_emails = [e for e in emails if re.match(alu_pattern, e)]
alumni_emails = [e for e in emails if re.match(alumni_pattern, e)]
si_emails = [e for e in emails if re.match(si_pattern, e)]

cards_raw = re.findall(credit_card_pattern, text)
# cards = [mask_card(c) for c in cards_raw]

urls = re.findall(url_pattern, text)
phones = re.findall(phone_pattern, text)
phones = ["".join(p).strip() for p in phones]


# the structure of the output json file

result = {
    "emails": emails,
    "alu_emails": alu_emails,
    "alumni_emails": alumni_emails,
    "si_emails": si_emails,
    "credit_cards": cards_raw,
    "urls": urls,
    "phones": phones
}

# write the result to a json file

with open("../output/sample-output.json", "w") as f:
    json.dump(result, f, indent=4)

print("Extraction completed successfully.")


