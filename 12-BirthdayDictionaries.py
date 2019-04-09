if __name__ == '__main__':

    birthdays = {
        'Marc Yu': '06/03/1995',
        'Randy Chan': '12/05/1995',
        'Malcolm Ngo': '17/22/1995',
        'Kenley Tan': '08/13/1995',
        'Jayson Revidad': '05/07/1995'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))