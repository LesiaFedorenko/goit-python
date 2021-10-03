from datetime import datetime

users = [{'name': 'Lesia', 'birthday': '1977-07-28'},
         {'name': 'Zina', 'birthday': '1979-07-28'},
         {'name': 'Olga', 'birthday': '1987-07-04'},
         {'name': 'Vova', 'birthday': '1998-07-26'},
         {'name': 'Sasha', 'birthday': '2000-02-26'},
         {'name': 'Natasha', 'birthday': '1988-07-31'},
         {'name': 'Lena', 'birthday': '1956-09-01'},
         {'name': 'Oleg', 'birthday': '2001-07-24'},
         {'name': 'Pavel', 'birthday': '2000-09-04'},
         {'name': 'Roma', 'birthday': '2020-09-10'},
         ]

def congratulate(users):
    current_date = datetime.now()
    wk = current_date.isocalendar()[1]
    if wk != 52:
        next_week = wk + 1
    else:
        next_week = 1
    dict_birthday = {}

    for i in users:
        for key, val in i.items():
            if key == 'birthday':
                data = val.split('-')
                birthday = datetime(year=current_date.year, month=int(data[1]), day=int(data[2]))
                if (birthday.strftime('%A') == 'Sunday' or birthday.strftime('%A') == 'Saturday') and birthday.isocalendar()[1] ==wk:
                    dict_birthday.update({'Monday (Weekend birthday persons)': (i['name'])})
                if birthday.isocalendar()[1] == next_week:
                    if birthday.strftime('%A') not in dict_birthday:
                        dict_birthday.update({birthday.strftime('%A'): (i['name'])})
                    else:
                        dict_birthday[birthday.strftime('%A')] = dict_birthday[birthday.strftime('%A')]+', '+(i['name'])

    for key, val in dict_birthday.items():
        print(f"{key}: {val}")


congratulate(users)
