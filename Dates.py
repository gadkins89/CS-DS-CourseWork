from datetime import date, timedelta, time, datetime
import calendar

# 1 Complete read_date()

def read_date(user_date):
    date_obj = datetime.strptime(user_date, "%Y-%m-%d").strftime("%m/%d/%Y")
    return date_obj
    

# 2. Use read_date() to read four (unique) date objects, putting the date objects in a list

user_dates = 0
dates_list = []
while user_dates < 4:
    date_input = input("Enter a date in YYYY-MM-DD format: \n")
    dates_list.append(read_date(date_input))
    user_dates += 1


# 3. Use sorted() to sort the dates, earliest first

sort_dates = sorted(dates_list, key = lambda x: x.rpartition("/")[-1])


# 4. Output the sorted_dates in order, earliest first, in the format mm/dd/yy

for d in enumerate(sort_dates):
    print(d)


# 5. Output the number of days between the last two dates in the sorted list
#    as a positive number

d0 = datetime.strptime(sort_dates[-1], "%m/%d/%Y")
d1 = datetime.strptime(sort_dates[-2], "%m/%d/%Y")

delta = d0 - d1

print(f"The number of days between the last 2 dates: {delta} ")


# 6. Output the date that is 3 weeks from the most recent date in the list

future_date = datetime.strptime(sort_dates[0], "%m/%d/%Y") + timedelta(weeks = 3)

print(f"Three weeks ahead of the most recent date: {future_date} ")


# 7. Output the full name of the day of the week of the earliest day

day_of_the_week_num = datetime.strptime(sort_dates[0], "%m/%d/%Y").weekday()

day_of_the_week = calendar.day_name[day_of_the_week_num]

print(f"The day of the week of the earliest day is: {day_of_the_week} ")