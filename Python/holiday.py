import jpholiday
import datetime

def isHoliday(year_date):
    if jpholiday.is_holiday_name(year_date) == None and year_date.weekday() < 5:
        return False
    else:
        return True

if __name__ == "__main__":
    print(datetime.date(2022,2,23).weekday())
    print(isHoliday(datetime.date(2022,2,23)))
