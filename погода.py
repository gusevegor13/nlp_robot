from datetime import date
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import re
# какая погода будет в городе (город) (дата)


replace_months = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12
}


def parse_date(day_str, month_str, year_str):
    day = int(day_str)
    if month_str not in replace_months:
        raise Exception('Invalid month')
    month = replace_months[month_str]
    year = int(year_str)
    return date(year, month, day)


def process(request):
    regex = r'какая погода будет в городе (.+?) (?:(\d{1,2}) (.+) (\d{4})|(завтра|послезавтра|сегодня))'
    match = re.search(regex, request, flags=re.IGNORECASE)
    if match is None:
        return

    print(match.groups())

    if match.groups()[4] is not None:
        text = match.groups()[4]
        if text == 'сегодня':
            parsed_date = date.today()
        elif text == 'завтра':
            parsed_date = date.today() + relativedelta(days=1)
        elif text == 'послезавтра':
            parsed_date = date.today() + relativedelta(days=2)
        else:
            raise Exception()
    else:
        parsed_date = parse_date(match[2], match[3], match[4])

    city = match[1]

    print(parsed_date)
    print('город', city)


def multiple_replace(request, replace_values):
    for i, j in replace_values.items():
        if request.find(i) != -1:
            request = request.replace(i, j)
            break
    return print(parse(request))


process('какая погода будет в городе ростов на дону 29 ноября 2021')
process('какая погода будет в городе ростов на дону послезавтра')
process('какая погода будет в городе москва 27 февраля 2022')
