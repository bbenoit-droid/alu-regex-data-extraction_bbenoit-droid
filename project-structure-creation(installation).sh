#!/bin/bash
read -p "Type 'Y' to install the project: " approve
if [[ "$approve" == "Y" || "$approve" == "y" ]]; then
    echo "Installing the project..."
    
mkdir -p input output src
touch input/raw_text.txt
touch output/sample-output.json.txt
touch src/main.py.py
echo "Project structure created with the following directories: input, output, src"

cat <<EOF > src/main.py
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
EOF

cat <<EOF > input/raw-text.txt
========================================================
INTERNAL CUSTOMER ACTIVITY EXPORT — API RESPONSE LOG
Generated: 2026-05-23T08:41:11Z
Environment: production-mirror
========================================================

Customer Name: John A. Murenzi
Primary Email: john.murenzi@alueducation.com
Secondary Email: jmurenzi_backup92@gmail.com
Phone: +250 788 321 901
Website: https://www.greenbasketafrica.org

Card Number: 4539-1488-0343-6467
Amount: $249.99

--------------------------------------------------------

Hotel: LakeView Retreat Kigali
Email: diane.uwase@alumni.alueducation.com
Phone: +250 (788) 555-111 or +250786101724
Website: https://lakeviewretreat.rw

Temp Card: 5500 0000 0000 0004

--------------------------------------------------------

Suspicious Input:
<script>alert('hack')</script>
admin@@fake..com
DROP TABLE users;
1111-1111-1111-111

--------------------------------------------------------

Research Email: research@si.alueducation.com
Meeting Times: 09:45, 14:30, 7:15 PM

Campaign:
https://campaigns.afrinnovators.com/launch?ref=twitter

Contact: media.team@alueducation.com
EOF

cat <<EOF > README.md
# Frontend Regex Data Extraction Project

# Overview
This project extracts and validates structured data from messy real-world text using Python regex.

It focuses on:
- Data extraction
- Input validation
- Security awareness (malicious input handling)
- Safe output formatting

---

# Features

- Extract emails, URLs, phone numbers, and credit cards
- Validate ALU-specific email domains:
  - @alueducation.com
  - @alumni.alueducation.com
  - @si.alueducation.com
- Mask sensitive credit card numbers (optional codes , but commented)
- Reject unsafe/malformed input (e.g., @@, script injection)
- Export structured JSON output

---

# Security Considerations

- Input is treated as untrusted
- Malformed emails are filtered
- Script injections are ignored
- Credit card numbers are masked before output(optinal , codess to do it are commented)
- Regex uses strict boundaries to avoid partial matches

---

# How to Run

cd src
python3 main.py

EOF

echo "Project structure created successfully. You can now run the main.py script to extract data from raw-text.txt and save it to sample-output.json."
else
    echo "Installation aborted. Please run the script again and type 'Y' to install."
fi
