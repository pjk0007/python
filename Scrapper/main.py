from indeed import get_jobs as get_indeed_jobs
from alba import get_jobs as get_alba_jobs

indeed_jobs = get_indeed_jobs()
alba_jobs = get_alba_jobs()
jobs = indeed_jobs + alba_jobs

print(alba_jobs)
