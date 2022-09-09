from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
title_links = soup.find_all(name="a", class_="titlelink")
scores_text = [score.text for score in soup.find_all(name="span", class_="score")]
scores = [int(score.split()[0]) for score in scores_text]
posts = zip(title_links, scores)
sorted_posts = sorted(posts, key=lambda x: x[1], reverse=True)
# print(sorted_posts)
for post in sorted_posts:
    title = post[0].text
    link = post[0]['href']
    score = post[1]
    print(title, link, score)