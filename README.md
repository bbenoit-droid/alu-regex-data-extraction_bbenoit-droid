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

