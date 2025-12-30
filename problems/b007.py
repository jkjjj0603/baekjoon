from datetime import datetime, timezone, timedelta

kst = timezone(timedelta(hours=9))
today = datetime.now(kst).date()
print(today.strftime("%Y-%m-%d"))