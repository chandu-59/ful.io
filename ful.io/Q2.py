import requests
from bs4 import BeautifulSoup
import re

def extract_information(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract social links
        social_links = []
        for link in soup.find_all('a', href=True):
            if re.search(r'facebook|linkedin', link['href']):
                social_links.append(link['href'])
        
        # Extract email
        email = soup.find(string=re.compile(r'\S+@\S+\.\S+'))
        
        # Extract contact details
        contact_details = soup.find(string=re.compile(r'\+?[\d\s-]+'))
        
        return social_links, email, contact_details
    except Exception as e:
        print("Error:", e)
        return None, None, None

# Get user input
url = input("Enter the website URL: ")

# Extract information
social_links, email, contact_details = extract_information(url)

# Print output
print("Output:")
print("Social links -")
for link in social_links:
    print(link)

print("Email/" + str(email))
print("Contact:")
print(contact_details)
