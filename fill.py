import os
import random
from datetime import datetime, timedelta

total_days = 365
start_date = datetime.now() - timedelta(days=total_days)

for i in range(total_days):
    commit_date = start_date + timedelta(days=i)
    
    # 35% દિવસો ખાલી રહેશે (કોઈ કમિટ નહીં)
    if random.random() < 0.35:
        continue
    
    # બાકીના દિવસોમાં 1 થી 4 કમિટ્સ રેન્ડમલી થશે (આછો-ઘાટો કલર બનશે)
    daily_commits = random.randint(1, 4)
    
    for c in range(daily_commits):
        hour = random.randint(9, 21)
        minute = random.randint(10, 55)
        formatted_date = commit_date.strftime(f'%Y-%m-%d {hour}:{minute}:00')
        
        with open('activity.txt', 'a') as file:
            file.write(f'Work on {formatted_date}\n')
        
        os.system('git add activity.txt')
        os.system(f'git commit --date="{formatted_date}" -m "Update {formatted_date}"')

print("Realistic activity generated!")