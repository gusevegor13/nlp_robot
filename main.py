from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import re


def parse_date(day_str, month_str, year_str):
    day = int(day_str)
    if month_str not in replace_months:
        raise Exception('Invalid month')
    month = replace_months[month_str]
    year = int(year_str)
    return date(year, month, day)


def schedule():
    request = input()
    if request.find("расписание") != -1 and request.find("сегодня") != -1:
        time_now = date.today()
        print(time_now)
    elif request.find("расписание") != -1 and request.find("послезавтра") != -1:
        time_aftertomorrow = date.today() + relativedelta(days=+2)
        print(time_aftertomorrow)
    elif request.find("расписание") != -1 and request.find("завтра") != -1:
        time_tomorrow = date.today() + relativedelta(days=+1)
        print(time_tomorrow)
    else:
        print(request)
        regex = r'какое расписание будет (?:(\d{1,2}) (.+) (\d{4}))'
        match = re.search(regex, request, flags=re.IGNORECASE)
        if match is None:
            return
        multiple_replace(match[1] + match[2] + match[3], replace_months)

replace_months = {
    "января": "january",
    "февраля": "february",
    "марта": "march",
    "апреля": "april",
    "мая": "may",
    "июня": "june",
    "июля": "july",
    "августа": "august",
    "сентября": "september",
    "октября": "october",
    "ноября": "november",
    "декабря": "december"
}


def multiple_replace(request, replace_values):
    for i, j in replace_values.items():
        if request.find(i) != -1:
            request = request.replace(i, j)
            break
    print(parse(request))
    return parse(request)


schedule()




