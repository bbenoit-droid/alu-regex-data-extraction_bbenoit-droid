import re
import json
from datetime import datetime, timezone


with open("../input/raw-text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# metadata

meta = {
    "source": "ALU SYSTEM AGGREGATOR",
    "generated_at": datetime.now(timezone.utc).isoformat(),
}

# Regex patterns for data extraction

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

alu_pattern = r'^[A-Za-z0-9._%+-]+@alueducation\.com$'
alumni_pattern = r'^[A-Za-z0-9._%+-]+@alumni\.alueducation\.com$'
si_pattern = r'^[A-Za-z0-9._%+-]+@si\.alueducation\.com$'

credit_card_pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
url_pattern = r'https?://[^\s]+'
phone_pattern = r'\+?\d[\d\s()-]{7,}\d'

# security validation 

def is_safe_email(email):
    return not (".." in email or "@@" in email or "<" in email)

def mask_card(card):
    digits = re.sub(r'\D', '', card)
    return "*" * 12 + digits[-4:]

def is_valid_time(value):
    return bool(re.match(r'^([01]?\d|2[0-3]):[0-5]\d(:[0-5]\d)?(\s?(AM|PM))?$', value))

# email processing and validation

emails_raw = re.findall(email_pattern, text)
emails_filtered = [e for e in emails_raw if is_safe_email(e)]

alu_emails = [e for e in emails_filtered if re.match(alu_pattern, e)]
alumni_emails = [e for e in emails_filtered if re.match(alumni_pattern, e)]
si_emails = [e for e in emails_filtered if re.match(si_pattern, e)]

invalid_emails = [
    e for e in emails_raw if e not in emails_filtered
]

# credit cards validation and masking

cards_raw = re.findall(credit_card_pattern, text)

credit_cards = [
    {
        "masked": mask_card(c),
        "source": c
    }
    for c in cards_raw
]

# urls

urls_raw = re.findall(url_pattern, text)

suspicious_urls = [
    u for u in urls_raw if "javascript:" in u or ".." in u
]

valid_urls = [
    u for u in urls_raw if u not in suspicious_urls
]

# phones

phones = re.findall(phone_pattern, text)
phones = ["".join(p).strip() for p in phones]

# security events detection

security_events = {
    "sql_injection_attempts": re.findall(r'DROP TABLE.*', text, re.IGNORECASE),
    "html_injection": re.findall(r'<[^>]+>', text)
}

# time extraction and validation

time_matches = re.findall(r'\b\d{1,2}:\d{2}(?:\s?(?:AM|PM))?\b', text)

valid_times = [t for t in time_matches if is_valid_time(t)]
invalid_times = [t for t in time_matches if not is_valid_time(t)]


# the structure of the output json file

result = {
    "meta": meta,

    "emails": {
        "valid": emails_filtered,
        "alu": alu_emails,
        "alumni": alumni_emails,
        "si": si_emails,
        "rejected": invalid_emails
    },

    "phones": phones,

    "credit_cards": credit_cards,

    "urls": {
        "valid": valid_urls,
        "suspicious": suspicious_urls
    },

    "security_events": security_events,

    "timestamps": {
        "valid_times": valid_times,
        "invalid_times": invalid_times
    }
}

# write the result to a json file

with open("../output/sample-output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("Extraction completed successfully.")