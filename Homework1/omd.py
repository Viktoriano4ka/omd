# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('\nВыберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар с зонтиком ☂️. '
        '\nНо у неё не было зонтика, у неё было кое-что получше...'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('\nПопробовать ещё раз?: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step1()
    print('👋')


def step2_no_umbrella():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар без зонтика ❌☂️. ', '\nА всё почему? ',
        '\nА всё потому, что утка-маляр из Питера 🦆 и у неё есть стильный дождевик от именитого бренда "Крялентино"'
          )


if __name__ == '__main__':
    step1()
