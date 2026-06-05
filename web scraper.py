import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("span", class_="titleline")

    print("Top News Headlines\n")

    with open("headlines.txt", "w", encoding="utf-8") as file:

        for i, article in enumerate(articles, start=1):
            title = article.get_text()
            link = article.find("a")["href"]

            print(f"{i}. {title}")
            print(f"   Link: {link}\n")

            file.write(f"{i}. {title}\n")
            file.write(f"   Link: {link}\n\n")

    print("Headlines saved to headlines.txt")

except requests.exceptions.RequestException as e:
    print("Error:", e)
