from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("we can't reach the code")
else:
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_="li")
  for job_section in jobs:
    jobs = []    
    li_tags = soup.select('li')
    jobs.append(li_tags.text)
  print(jobs)  
