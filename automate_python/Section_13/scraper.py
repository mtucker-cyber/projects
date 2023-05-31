# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from urllib.parse import urlparse

# Specify the URL to be scraped
#url = "URL to be scraped"

# Initialize a WebDriver for Firefox
driver = webdriver.Firefox()

# Open the specified URL
driver.get(url)

# Get the domain from the URL
domain = urlparse(url).netloc  

# Initialize lists to store phone numbers and email addresses
phone_numbers = []
email_addresses = []

# Find phone numbers and email addresses on the main page
content = driver.page_source
phone_numbers += re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]\d{4}', content)
email_addresses += re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)

# Find all links on the main page
links = driver.find_elements(By.TAG_NAME, "a")
urls = [link.get_attribute('href') for link in links]

# Visit each link and find phone numbers and email addresses
for url in urls:
    if domain in urlparse(url).netloc:  # Check if the link belongs to the same domain
        driver.get(url)
        content = driver.page_source
        phone_numbers += re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]\d{4}', content)
        email_addresses += re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)

# Remove duplicates from phone_numbers and email_addresses
phone_numbers = list(set(phone_numbers))
email_addresses = list(set(email_addresses))

# Print the collected phone numbers and email addresses
print("Phone numbers found:", phone_numbers)
print("Email addresses found:", email_addresses)

# Close the WebDriver
driver.close()