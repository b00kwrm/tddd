import csv

tagged_lines = []

with open('tddd-cron-tagged.csv') as f:
    reader = csv.DictReader(f)
    lines = list(reader)


for line in lines:
    if line['notes'] == 'T1168_local_job_scheduling':
        tagged_lines.append(line['notes'])
    if line['notes'] == 'T1078_valid_accounts':
        tagged_lines.append(line['notes'])

assert 'T1168_local_job_scheduling' in tagged_lines
assert 'T1078_valid_accounts' in tagged_lines
        
