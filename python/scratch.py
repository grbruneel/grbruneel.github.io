from datetime import datetime, timedelta

now = datetime.today()
later = now + timedelta(seconds=20000)

print(now)
print(later.strftime("%d-%m-%Y, %H:%M:%S"))