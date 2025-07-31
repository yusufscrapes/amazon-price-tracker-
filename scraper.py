from bs4 import BeautifulSoup

# Load the local HTML file
with open("sample.html", "r", encoding="utf-8") as file:
    html = file.read()

# Parse with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Try to extract title and price
title = soup.find(id="productTitle")
price = soup.find("span", {"class": "a-price-whole"})

# Display the results
print("Product Title:", title.get_text(strip=True) if title else "Not found")
whole = soup.find("span", {"class": "a-price-whole"})
fraction = soup.find("span", {"class": "a-price-fraction"})

if whole and fraction:
    price = f"{whole.get_text(strip=True).rstrip('.')}.{fraction.get_text(strip=True)}"
else:
    price = "Not found"

print("Price:", price)
