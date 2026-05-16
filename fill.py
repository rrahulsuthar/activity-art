import os
import random
from datetime import datetime, timedelta

# ૧ ઓગસ્ટ ૨૦૨૫ થી લઈને આજ સુધીની તારીખ
start_date = datetime(2025, 8, 1)
end_date = datetime.now()
total_days = (end_date - start_date).days + 1

for i in range(total_days):
    commit_date = start_date + timedelta(days=i)
    
    # દરરોજ ફરજિયાત ૧ થી ૪ કમિટ થશે (કોઈ પણ દિવસ ખાલી નહીં રહે)
    daily_commits = random.randint(1, 4)
    
    for c in range(daily_commits):
        hour = random.randint(9, 21)
        minute = random.randint(10, 55)
        formatted_date = commit_date.strftime(f'%Y-%m-%d {hour}:{minute}:00')
        
        with open('activity.txt', 'a') as file:
            file.write(f'Work on {formatted_date}\n')
        
        os.system('git add activity.txt')
        os.system(f'git commit --date="{formatted_date}" -m "Update {formatted_date}"')

print("All dates up to today successfully generated!")