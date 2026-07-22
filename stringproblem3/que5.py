
# 5. Website URL Verification System

# A software company is developing an automated website registration
# portal. Before saving a website address, the system must verify whether
# the URL follows the required company format.

# Conditions: - Must start with www - Must end with .com

# Input: Enter website: www.amazon.com

# Output: Valid Website
website = input("Enter website: ")

if website[:3] == "www" and website[-4:] == ".com":
    print("Valid Website")
else:
    print("Invalid Website")