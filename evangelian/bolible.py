from requests import get
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver?query="
search_term = "cookie"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("we can't reach the code")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  cookie = soup.find_all('section', class_="jobs")
  print(cookie)
