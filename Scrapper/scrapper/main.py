from indeed import get_jobs as get_indeed_jobs
from alba import get_jobs as get_alba_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs("python")
alba_jobs = get_alba_jobs("개발자")
jobs = indeed_jobs + alba_jobs

save_to_file(jobs)
