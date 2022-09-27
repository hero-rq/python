from requests import get

base_url = "https://search.naver.com/search.naver?query="
search_term = "panda"

response = get(f"{base_url}{search_term}")
print(response.text)
