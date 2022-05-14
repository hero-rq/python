from indeed import extract_indeed_pages, extract_job, extract_jobs 
from save import save_to_file

last_indeed_page = extract_indeed_pages()

indeed_jobs = extract_jobs(last_indeed_page) 

save_to_file(indeed_jobs)
