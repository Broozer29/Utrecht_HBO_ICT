def convert(celcius):
    return (celcius * 1.8) + 32


def table():
    gradenCelcius = -30.0
    print('{:<2}F{:<7}C'.format(' ',' '))
    while gradenCelcius < 41:
        gradenFahrenheit = convert(gradenCelcius)
        print('{:>5} {:>7}'.format(gradenFahrenheit, gradenCelcius))
        gradenCelcius += 10

table()
