import datetime 

year1, month1, date1 = map(int, input().split())
year2, month2, date2 = map(int, input().split())

today = datetime.date(year1, month1, date1)
end_day = datetime.date(year2, month2, date2)
today_1000 = datetime.date(year1 + 1000, month1, date1)
date = (end_day - today).days

if date < (today_1000 - today).days:
    print('D-%d' % date)
else:
    print("gg")