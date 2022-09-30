from extracts.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")
wwr = extract_wwr_jobs(keyword)

jobs = wwr 
for job in jobs:
  print(job)
  print("*********")
