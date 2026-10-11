import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    headings = soup.find_all(["h1", "h2", "h3"])

    headlines = []

    for heading in headings:
        text = heading.get_text(strip=True)

        if text and text not in headlines:
            headlines.append(text)

    with open("headlines.txt", "w", encoding="utf-8") as file:
        file.write("NEWS HEADLINES")
        file.write("=" * 50 + "")

        for number, headline in enumerate(headlines, start=1):
            file.write(f"{number}. \n{headline}")

    print(f"Success! {len(headlines)} headlines saved in headlines.txt")

except Exception as error:
    print("Error:", error)