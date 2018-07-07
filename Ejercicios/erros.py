# -*- coding: utf-8 -*-


countries = {
    'venezuela': 31,
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(raw_input('Escribe el nombre de un pais: ')).lower()

    try:
        print('la poblacion de {} es de {} millones'.format(country, countries[country]))
    except KeyError:
        print(KeyError)
        print('No tenemos el dato de la población de {}'.format(country))
        #country = int(raw_input('escribe la poblacion de {}: '.format(country)))
        #countries[country] = country