import re

def validate_contact_number(contact_number):
    # Define a regular expression pattern for valid contact numbers
    pattern = r'^(\+\d{1,2}\s?)?(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$'

    # Use the re.match() function to check if the contact number matches the pattern
    if re.match(pattern, contact_number):
        return "Valid"
    else:
        return "Invalid"

# Test cases
contacts = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

for i in contacts:
    res = validate_contact_number(i)
    print(f"{i}: {res}")
