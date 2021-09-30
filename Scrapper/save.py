import csv

jobs = ['1', '2', '3', '4']


def save_to_file(jobs):
    file = open("jobs.csv", mode="w",
                encoding='utf-8-sig', newline='')
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
