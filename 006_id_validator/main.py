def ask_for_id():
    global isikukood
    while True:
        idcode = input('Please enter your national id: ')
        if idcode.isdecimal():
            if len(idcode) != 11:
                if len(idcode) < 11:
                    print('ID you entered is too short.')
                    continue
                else:
                    print('ID you entered is too long.')
                    continue
            else:
                isikukood = idcode
                return
        else:
            print('ID you entered is not numeric!')
            continue


def get_gender():
    n = isikukood[0]
    if n not in '09':
        if int(n) % 2 == 0:
            print('You are female')
        else:
            print('You are male')
    else:
        print('Something wrong with ID you entered.')


def get_date_of_birth():
    day = isikukood[5:7]
    month = isikukood[3:5]
    year = isikukood[1:3]
    bcent = ''
    n = isikukood[0]
    if n not in '09':
        if n in '12':
            bcent = '18'
        elif n in '34':
            bcent = '19'
        elif n in '56':
            bcent = '20'
        elif n in '78':
            bcent = '21'
        print(f'{day}.{month}.{bcent}{year}')
    else:
        print('Something wrong with ID you entered.')


def get_birth_region():
    chk = isikukood[7:10]
    if int(chk) in range(1, 11):
        print('Kuressaare haigla')
    elif '011' <= chk <= '019':
        print('Tartu Ülikooli Naistekliinik')
    elif '021' <= chk and '150' >= chk:
        print('Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)')


def validate_id():
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    result = 0
    for num in range(10):
        result += chk1[num] * int(isikukood[num])
    if result % 11 == int(isikukood[-1]):
        print('ID is valid')
    elif result % 11 == 10:
        result = 0
        for num in range(10):
            result += chk2[num] * int(isikukood[num])
        if result % 11 == int(isikukood[-1]):
            print('ID is valid')
        else:
            print('ID is not valid')
    else:
        print('ID is not valid')

def menu():
    ask_for_id()
    while True:
        user_choice = input('Please choose:\n'
                            '1.Gender\n'
                            '2.Date of birth\n'
                            '3.Birth region\n'
                            '4.Validation\n'
                            '5.Change ID\n'
                            '0.Exit\n'
                            '--> ')
        if user_choice == '1':
            get_gender()
        elif user_choice == '2':
            get_date_of_birth()
        elif user_choice == '3':
            get_birth_region()
        elif user_choice == '4':
            validate_id()
        elif user_choice == '5':
            ask_for_id()
        elif user_choice == '0':
            break
        else:
            print('Choice out of range.')


isikukood = ''
menu()
