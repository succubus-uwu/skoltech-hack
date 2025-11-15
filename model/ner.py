import spacy
import random
from pathlib import Path
from spacy.training import Example
from spacy.util import minibatch, compounding
from spacy.training import offsets_to_biluo_tags

"Я жить город Москва улица Ленин дом 51"

# Пример тренировочных данных (остаются без изменений в формате)
TRAIN_DATA = [
    # Sample 1
    (
        'москва улица арбат дом 28',
        {'entities': [(7, 18, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 2
    (
        '620075 екатеринбург ленин проспект 54 корп 1',
        {'entities': [(0, 6, 'addr:postcode'), (20, 34, 'addr:street'), (35, 44, 'addr:housenumber')]}
    ),

    # Sample 3
    (
        'спб невский пр 88/2',
        {'entities': [(4, 14, 'addr:street'), (15, 19, 'addr:housenumber')]}
    ),

    # Sample 4
    (
        'казань улица бауман дом 25',
        {'entities': [(7, 19, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 5
    (
        'новосибирск красный проспект 35 корпус 3',
        {'entities': [(12, 28, 'addr:street'), (29, 40, 'addr:housenumber')]}
    ),

    # Sample 6
    (
        'нижний новгород больший покровский 15',
        {'entities': [(16, 34, 'addr:street'), (35, 37, 'addr:housenumber')]}
    ),

    # Sample 7
    (
        'город краснодар улица красный дом 122',
        {'entities': [(16, 29, 'addr:street'), (34, 37, 'addr:housenumber')]}
    ),

    # Sample 8
    (
        'владивосток улица светланский 33',
        {'entities': [(12, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 9
    (
        '198152 санкт-петербург набережная обводный канал дом 118',
        {'entities': [(0, 6, 'addr:postcode'), (23, 48, 'addr:street'), (53, 56, 'addr:housenumber')]}
    ),

    # Sample 10
    (
        'ростов-на-дон проспект будённовский 65',
        {'entities': [(14, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 11
    (
        'москва дом 12 корп 5 кутузовский проспект',
        {'entities': [(21, 41, 'addr:street'), (11, 20, 'addr:housenumber')]}
    ),

    # Sample 12
    (
        'самара улица ленинградский дом 88',
        {'entities': [(7, 26, 'addr:street'), (31, 33, 'addr:housenumber')]}
    ),

    # Sample 13
    (
        'уфа проспект октябрь 45/1',
        {'entities': [(4, 20, 'addr:street'), (21, 25, 'addr:housenumber')]}
    ),

    # Sample 14
    (
        'воронеж улица плехановский 53',
        {'entities': [(8, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 15
    (
        'пр ленин 120 челябинск',
        {'entities': [(0, 8, 'addr:street'), (9, 12, 'addr:housenumber')]}
    ),

    # Sample 16
    (
        'пермь улица комсомольский дом 37',
        {'entities': [(6, 25, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 17
    (
        'волгоград аллея герой 1',
        {'entities': [(10, 21, 'addr:street'), (22, 23, 'addr:housenumber')]}
    ),

    # Sample 18
    (
        '420012 казань улица кремлёвский 18',
        {'entities': [(0, 6, 'addr:postcode'), (14, 31, 'addr:street'), (32, 34, 'addr:housenumber')]}
    ),

    # Sample 19
    (
        'омск улица маркс 41 к2',
        {'entities': [(5, 16, 'addr:street'), (17, 22, 'addr:housenumber')]}
    ),

    # Sample 20
    (
        'город тюмень улица республика дом 155',
        {'entities': [(13, 29, 'addr:street'), (34, 37, 'addr:housenumber')]}
    ),

    # Sample 21
    (
        'москва улица арбат дом 28',
        {'entities': [(7, 18, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 22
    (
        '630102 новосибирск красный проспект 82',
        {'entities': [(0, 6, 'addr:postcode'), (19, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 23
    (
        'санкт-петербург невский пр 45 корп 1',
        {'entities': [(16, 26, 'addr:street'), (27, 36, 'addr:housenumber')]}
    ),

    # Sample 24
    (
        'екатеринбург улица ленин 50',
        {'entities': [(13, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 25
    (
        'казань улица бауман дом 12 квартира 45',
        {'entities': [(7, 19, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 26
    (
        'нижний новгород больший покровский 18',
        {'entities': [(16, 34, 'addr:street'), (35, 37, 'addr:housenumber')]}
    ),

    # Sample 27
    (
        'владивосток светланский улица дом 33',
        {'entities': [(12, 29, 'addr:street'), (34, 36, 'addr:housenumber')]}
    ),

    # Sample 28
    (
        'ростов-на-дон проспект будённовский 65/2',
        {'entities': [(14, 35, 'addr:street'), (36, 40, 'addr:housenumber')]}
    ),

    # Sample 29
    (
        'краснодар улица красный 125 квартира 8',
        {'entities': [(10, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 30
    (
        '420012 казань дом 7 корп 3 улица кремлёвский',
        {'entities': [(0, 6, 'addr:postcode'), (27, 44, 'addr:street'), (18, 26, 'addr:housenumber')]}
    ),

    # Sample 31
    (
        'самара московский шоссе 15а',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 32
    (
        'спб набережная фонтанка 56',
        {'entities': [(4, 23, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 33
    (
        'уфа проспект октябрь 45',
        {'entities': [(4, 20, 'addr:street'), (21, 23, 'addr:housenumber')]}
    ),

    # Sample 34
    (
        'волгоград улица мир дом 28 корпус 1',
        {'entities': [(10, 19, 'addr:street'), (24, 35, 'addr:housenumber')]}
    ),

    # Sample 35
    (
        'пермь улица ленин 68',
        {'entities': [(6, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 36
    (
        'воронеж кольцовский 25/1',
        {'entities': [(8, 19, 'addr:street'), (20, 24, 'addr:housenumber')]}
    ),

    # Sample 37
    (
        'омск маркс 41 корп 2',
        {'entities': [(5, 10, 'addr:street'), (11, 20, 'addr:housenumber')]}
    ),

    # Sample 38
    (
        'челябинск пр ленин 52',
        {'entities': [(10, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 39
    (
        'тюмень улица республика дом 10',
        {'entities': [(7, 23, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 40
    (
        'иркутск карла маркс улица 3',
        {'entities': [(8, 25, 'addr:street'), (26, 27, 'addr:housenumber')]}
    ),

    # Sample 41
    (
        'москва улица арбат дом 28',
        {'entities': [(7, 18, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 42
    (
        '620075 екатеринбург ленин проспект 54 корп 1',
        {'entities': [(0, 6, 'addr:postcode'), (20, 34, 'addr:street'), (35, 44, 'addr:housenumber')]}
    ),

    # Sample 43
    (
        'спб садовый улица 12/23',
        {'entities': [(4, 17, 'addr:street'), (18, 23, 'addr:housenumber')]}
    ),

    # Sample 44
    (
        'казань улица бауман 47',
        {'entities': [(7, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 45
    (
        'новосибирск красный проспект дом 35 квартира 12',
        {'entities': [(12, 28, 'addr:street'), (33, 35, 'addr:housenumber')]}
    ),

    # Sample 46
    (
        'краснодар улица красный дом 154',
        {'entities': [(10, 27, 'addr:street'), (28, 31, 'addr:housenumber')]}
    ),

    # Sample 47
    (
        '190000 санкт-петербург набережная канал грибоедов 5',
        {'entities': [(0, 6, 'addr:postcode'), (23, 49, 'addr:street'), (50, 51, 'addr:housenumber')]}
    ),

    # Sample 48
    (
        'владивосток светланский улица 33',
        {'entities': [(12, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 49
    (
        'москва тверская-ямский 1-я улица дом 10 корпус 2',
        {'entities': [(7, 32, 'addr:street'), (37, 48, 'addr:housenumber')]}
    ),

    # Sample 50
    (
        'ростов-на-дон проспект будённовский 85',
        {'entities': [(14, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 52
    (
        'омск маркс проспект 18а',
        {'entities': [(5, 19, 'addr:street'), (20, 23, 'addr:housenumber')]}
    ),

    # Sample 53
    (
        'самара улица молодогвардейский 151',
        {'entities': [(7, 30, 'addr:street'), (31, 34, 'addr:housenumber')]}
    ),

    # Sample 54
    (
        'пермь комсомольский пр дом 34',
        {'entities': [(6, 22, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 55
    (
        'челябинск киров 130',
        {'entities': [(10, 15, 'addr:street'), (16, 19, 'addr:housenumber')]}
    ),

    # Sample 56
    (
        'воронеж улица плехановский 9',
        {'entities': [(8, 26, 'addr:street'), (27, 28, 'addr:housenumber')]}
    ),

    # Sample 57
    (
        'волгоград проспект ленин дом 21/2',
        {'entities': [(10, 24, 'addr:street'), (29, 33, 'addr:housenumber')]}
    ),

    # Sample 58
    (
        'саратов московский улица 34',
        {'entities': [(8, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 59
    (
        'тюмень улица республика дом 61',
        {'entities': [(7, 23, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 60
    (
        'иркутск карла маркс 25 квартира 8',
        {'entities': [(8, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 61
    (
        'москва улица арбат дом 28',
        {'entities': [(7, 18, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 62
    (
        '620075 екатеринбург проспект ленин 54а',
        {'entities': [(0, 6, 'addr:postcode'), (20, 34, 'addr:street'), (35, 38, 'addr:housenumber')]}
    ),

    # Sample 63
    (
        'санкт-петербург невский пр 88 корп 1',
        {'entities': [(16, 26, 'addr:street'), (27, 36, 'addr:housenumber')]}
    ),

    # Sample 64
    (
        'казань улица бауман дом 12',
        {'entities': [(7, 19, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 65
    (
        'новосибирск красный проспект дом 35',
        {'entities': [(12, 28, 'addr:street'), (33, 35, 'addr:housenumber')]}
    ),

    # Sample 66
    (
        'нижний новгород больший покровский 15/22',
        {'entities': [(24, 34, 'addr:street'), (35, 40, 'addr:housenumber')]}
    ),

    # Sample 67
    (
        'краснодар улица красный 154',
        {'entities': [(10, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 68
    (
        'владивосток улица светланский дом 47 квартира 12',
        {'entities': [(12, 29, 'addr:street'), (34, 36, 'addr:housenumber')]}
    ),

    # Sample 69
    (
        '198095 спб набережная обводный канал 118',
        {'entities': [(0, 6, 'addr:postcode'), (11, 36, 'addr:street'), (37, 40, 'addr:housenumber')]}
    ),

    # Sample 70
    (
        'ростов-на-дон проспект будённовский 93',
        {'entities': [(14, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 71
    (
        'уфа улица ленин 25 корп 3',
        {'entities': [(4, 15, 'addr:street'), (16, 25, 'addr:housenumber')]}
    ),

    # Sample 72
    (
        'пермь комсомольский проспект дом 34',
        {'entities': [(6, 28, 'addr:street'), (33, 35, 'addr:housenumber')]}
    ),

    # Sample 73
    (
        'волгоград улица мир 11',
        {'entities': [(10, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 74
    (
        'самара московский шоссе 15а',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 75
    (
        'омск маркс 41 корпус 2',
        {'entities': [(5, 10, 'addr:street'), (11, 22, 'addr:housenumber')]}
    ),

    # Sample 76
    (
        'челябинск пр ленин дом 52б',
        {'entities': [(10, 18, 'addr:street'), (23, 26, 'addr:housenumber')]}
    ),

    # Sample 77
    (
        'воронеж улица плехановский дом 9',
        {'entities': [(8, 26, 'addr:street'), (31, 32, 'addr:housenumber')]}
    ),

    # Sample 78
    (
        'тюмень улица республика 142',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 79
    (
        'иркутск карла маркс 17',
        {'entities': [(8, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 80
    (
        'саратов улица московский 85/89',
        {'entities': [(8, 24, 'addr:street'), (25, 30, 'addr:housenumber')]}
    ),

    # Sample 81
    (
        'москва улица арбат дом 28',
        {'entities': [(7, 18, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 82
    (
        '620075 екатеринбург улица малышев 36 корп 1',
        {'entities': [(0, 6, 'addr:postcode'), (20, 33, 'addr:street'), (34, 43, 'addr:housenumber')]}
    ),

    # Sample 83
    (
        'спб невский проспект 85',
        {'entities': [(4, 20, 'addr:street'), (21, 23, 'addr:housenumber')]}
    ),

    # Sample 84
    (
        'казань улица бауман дом 20/25',
        {'entities': [(7, 19, 'addr:street'), (24, 29, 'addr:housenumber')]}
    ),

    # Sample 85
    (
        'новосибирск красный проспект дом 1',
        {'entities': [(12, 28, 'addr:street'), (33, 34, 'addr:housenumber')]}
    ),

    # Sample 86
    (
        'город краснодар улица красный 122',
        {'entities': [(16, 29, 'addr:street'), (30, 33, 'addr:housenumber')]}
    ),

    # Sample 87
    (
        'владивосток светланский улица 50',
        {'entities': [(12, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 88
    (
        'ростов-на-дон пр будённовский 93',
        {'entities': [(14, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 89
    (
        'самара улица ленинградский 55 квартира 12',
        {'entities': [(7, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 90
    (
        '197022 санкт-петербург набережная река фонтанка дом 15',
        {'entities': [(0, 6, 'addr:postcode'), (23, 47, 'addr:street'), (52, 54, 'addr:housenumber')]}
    ),

    # Sample 91
    (
        'пермь улица ленин 68',
        {'entities': [(6, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 92
    (
        'воронеж кольцовский улица 35',
        {'entities': [(8, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 93
    (
        'город уфа проспект октябрь дом 107 корп 2',
        {'entities': [(10, 26, 'addr:street'), (31, 41, 'addr:housenumber')]}
    ),

    # Sample 94
    (
        'челябинск улица киров дом 104',
        {'entities': [(10, 21, 'addr:street'), (26, 29, 'addr:housenumber')]}
    ),

    # Sample 95
    (
        'омск улица ленин 12а',
        {'entities': [(5, 16, 'addr:street'), (17, 20, 'addr:housenumber')]}
    ),

    # Sample 96
    (
        'тюмень улица республика 142',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 97
    (
        'иркутск улица карла маркс 25',
        {'entities': [(8, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 98
    (
        'хабаровск муравьёв-амурский 15',
        {'entities': [(10, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 99
    (
        'ярославль первомайский улица дом 67',
        {'entities': [(10, 28, 'addr:street'), (33, 35, 'addr:housenumber')]}
    ),

    # Sample 100
    (
        'тула проспект ленин 99/2',
        {'entities': [(5, 19, 'addr:street'), (20, 24, 'addr:housenumber')]}
    ),

    # Sample 101
    (
        'москва улица арбат дом 28',
        {'entities': [(7, 18, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 102
    (
        '620075 екатеринбург ленин проспект 54 корп 1',
        {'entities': [(0, 6, 'addr:postcode'), (20, 34, 'addr:street'), (35, 44, 'addr:housenumber')]}
    ),

    # Sample 103
    (
        'спб набережная канал грибоедов 15/2',
        {'entities': [(4, 30, 'addr:street'), (31, 35, 'addr:housenumber')]}
    ),

    # Sample 104
    (
        'казань улица бауман дом 47',
        {'entities': [(7, 19, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 105
    (
        'новосибирск красный проспект 35',
        {'entities': [(12, 28, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 106
    (
        'город владивосток улица светланский дом 10 квартира 25',
        {'entities': [(18, 35, 'addr:street'), (40, 42, 'addr:housenumber')]}
    ),

    # Sample 107
    (
        'краснодар улица красный 122',
        {'entities': [(10, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 108
    (
        '198152 санкт-петербург московский проспект дом 78 корпус 3',
        {'entities': [(0, 6, 'addr:postcode'), (23, 42, 'addr:street'), (47, 58, 'addr:housenumber')]}
    ),

    # Sample 109
    (
        'ростов-на-дон переулок халтуринский 18',
        {'entities': [(14, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 110
    (
        'уфа улица ленин 3/1',
        {'entities': [(4, 15, 'addr:street'), (16, 19, 'addr:housenumber')]}
    ),

    # Sample 111
    (
        'город омск маркс пр 41',
        {'entities': [(11, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 112
    (
        'пермь улица комсомольский проспект дом 34',
        {'entities': [(12, 34, 'addr:street'), (39, 41, 'addr:housenumber')]}
    ),

    # Sample 113
    (
        'воронеж кольцовский улица 56 корп 2',
        {'entities': [(8, 25, 'addr:street'), (26, 35, 'addr:housenumber')]}
    ),

    # Sample 114
    (
        '420012 казань дом 88 улица пушкин',
        {'entities': [(0, 6, 'addr:postcode'), (21, 33, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 115
    (
        'самара московский шоссе 15а',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 116
    (
        'челябинск улица киров 25',
        {'entities': [(10, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 117
    (
        'нижний новгород больший покровский дом 12',
        {'entities': [(16, 34, 'addr:street'), (39, 41, 'addr:housenumber')]}
    ),

    # Sample 118
    (
        'тюмень улица республика 142',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 119
    (
        'город иркутск бульвар гагарин 38',
        {'entities': [(14, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 120
    (
        'волгоград проспект ленин дом 67',
        {'entities': [(10, 24, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 121
    (
        'москва улица арбат дом 28',
        {'entities': [(7, 18, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 122
    (
        '620075 екатеринбург улица малышев 36 корп 1',
        {'entities': [(0, 6, 'addr:postcode'), (20, 33, 'addr:street'), (34, 43, 'addr:housenumber')]}
    ),

    # Sample 123
    (
        'спб невский проспект 85',
        {'entities': [(4, 20, 'addr:street'), (21, 23, 'addr:housenumber')]}
    ),

    # Sample 124
    (
        'казань улица бауман дом 12 квартира 45',
        {'entities': [(7, 19, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 125
    (
        'новосибирск красный проспект 100',
        {'entities': [(12, 28, 'addr:street'), (29, 32, 'addr:housenumber')]}
    ),

    # Sample 126
    (
        'город владивосток улица светланский 50',
        {'entities': [(18, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 127
    (
        'краснодар улица красный 122',
        {'entities': [(10, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 128
    (
        '198095 санкт-петербург набережная обводный канал дом 14',
        {'entities': [(0, 6, 'addr:postcode'), (23, 48, 'addr:street'), (53, 55, 'addr:housenumber')]}
    ),

    # Sample 129
    (
        'ростов-на-дон проспект будённовский 78/2',
        {'entities': [(14, 35, 'addr:street'), (36, 40, 'addr:housenumber')]}
    ),

    # Sample 130
    (
        'уфа улица ленин 25 к3',
        {'entities': [(4, 15, 'addr:street'), (16, 21, 'addr:housenumber')]}
    ),

    # Sample 131
    (
        'город омск дом 67 улица маркс',
        {'entities': [(18, 29, 'addr:street'), (15, 17, 'addr:housenumber')]}
    ),

    # Sample 132
    (
        'воронеж кольцовский улица 15',
        {'entities': [(8, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 133
    (
        'пермь улица ленин дом 39',
        {'entities': [(6, 17, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 134
    (
        'волгоград пр ленин 88',
        {'entities': [(10, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 135
    (
        'самара улица куйбышев дом 120 квартира 8',
        {'entities': [(7, 21, 'addr:street'), (26, 29, 'addr:housenumber')]}
    ),

    # Sample 136
    (
        'челябинск улица киров 104',
        {'entities': [(10, 21, 'addr:street'), (22, 25, 'addr:housenumber')]}
    ),

    # Sample 137
    (
        'тюмень улица республика 142',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 138
    (
        'город иркутск улица карла маркс 25',
        {'entities': [(14, 31, 'addr:street'), (32, 34, 'addr:housenumber')]}
    ),

    # Sample 139
    (
        'ярославль московский проспект дом 12 корп 2',
        {'entities': [(10, 29, 'addr:street'), (34, 43, 'addr:housenumber')]}
    ),

    # Sample 140
    (
        'сочи курортный проспект 105',
        {'entities': [(5, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 141
    (
        'москва улица арбат дом 28',
        {'entities': [(7, 18, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 142
    (
        '630102 новосибирск красный проспект 82',
        {'entities': [(0, 6, 'addr:postcode'), (19, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 143
    (
        'спб невский пр 45 корп 1',
        {'entities': [(4, 14, 'addr:street'), (15, 24, 'addr:housenumber')]}
    ),

    # Sample 144
    (
        'екатеринбург улица ленин 15',
        {'entities': [(13, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 145
    (
        'казань бауман 20/5 квартира 12',
        {'entities': [(7, 13, 'addr:street'), (14, 18, 'addr:housenumber')]}
    ),

    # Sample 146
    (
        'нижний новгород больший покровский дом 37',
        {'entities': [(16, 34, 'addr:street'), (39, 41, 'addr:housenumber')]}
    ),

    # Sample 147
    (
        'краснодар улица красный дом 154',
        {'entities': [(10, 27, 'addr:street'), (28, 31, 'addr:housenumber')]}
    ),

    # Sample 148
    (
        'владивосток светланский улица 22',
        {'entities': [(12, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 149
    (
        '119021 москва зубовский бульвар 17 корпус 1',
        {'entities': [(0, 6, 'addr:postcode'), (14, 31, 'addr:street'), (32, 43, 'addr:housenumber')]}
    ),

    # Sample 150
    (
        'ростов-на-дон проспект ворошиловский 45',
        {'entities': [(14, 36, 'addr:street'), (37, 39, 'addr:housenumber')]}
    ),

    # Sample 151
    (
        'самара улица молодогвардейский дом 88 квартира 25',
        {'entities': [(7, 30, 'addr:street'), (35, 37, 'addr:housenumber')]}
    ),

    # Sample 152
    (
        'пермь комсомольский проспект 34',
        {'entities': [(6, 28, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 153
    (
        'воронеж улица плехановский 53',
        {'entities': [(8, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 154
    (
        'волгоград пр ленин 10',
        {'entities': [(10, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 155
    (
        'омск маркс 41 корп 2',
        {'entities': [(5, 10, 'addr:street'), (11, 20, 'addr:housenumber')]}
    ),

    # Sample 156
    (
        'челябинск киров 120',
        {'entities': [(10, 15, 'addr:street'), (16, 19, 'addr:housenumber')]}
    ),

    # Sample 157
    (
        'уфа проспект октябрь дом 62',
        {'entities': [(4, 20, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 158
    (
        'красноярск улица мир 15 квартира 8',
        {'entities': [(11, 20, 'addr:street'), (21, 23, 'addr:housenumber')]}
    ),

    # Sample 159
    (
        'иркутск карла маркс 25',
        {'entities': [(8, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 160
    (
        'тюмень улица республика дом 14',
        {'entities': [(7, 23, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 161
    (
        'москва улица арбат дом 28',
        {'entities': [(7, 18, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 162
    (
        '620075 екатеринбург ленин проспект 54 корп 1',
        {'entities': [(0, 6, 'addr:postcode'), (20, 34, 'addr:street'), (35, 44, 'addr:housenumber')]}
    ),

    # Sample 163
    (
        'спб набережная канал грибоедов 15/2',
        {'entities': [(4, 30, 'addr:street'), (31, 35, 'addr:housenumber')]}
    ),

    # Sample 164
    (
        'казань улица бауман 47',
        {'entities': [(7, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 165
    (
        'новосибирск красный проспект дом 82',
        {'entities': [(12, 28, 'addr:street'), (33, 35, 'addr:housenumber')]}
    ),

    # Sample 166
    (
        'нижний новгород больший покровский 18',
        {'entities': [(16, 34, 'addr:street'), (35, 37, 'addr:housenumber')]}
    ),

    # Sample 167
    (
        'краснодар улица красный дом 122',
        {'entities': [(10, 27, 'addr:street'), (28, 31, 'addr:housenumber')]}
    ),

    # Sample 168
    (
        'владивосток светланский улица 33',
        {'entities': [(12, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 169
    (
        '198152 санкт-петербург московский пр 78 корпус 3',
        {'entities': [(0, 6, 'addr:postcode'), (23, 36, 'addr:street'), (37, 48, 'addr:housenumber')]}
    ),

    # Sample 170
    (
        'ростов-на-дон проспект будённовский 45а',
        {'entities': [(14, 35, 'addr:street'), (36, 39, 'addr:housenumber')]}
    ),

    # Sample 171
    (
        'воронеж улица кольцовский 56',
        {'entities': [(8, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 172
    (
        'пермь комсомольский проспект дом 34',
        {'entities': [(6, 28, 'addr:street'), (33, 35, 'addr:housenumber')]}
    ),

    # Sample 173
    (
        'самара улица ленинградский 89 корп 2',
        {'entities': [(7, 26, 'addr:street'), (27, 36, 'addr:housenumber')]}
    ),

    # Sample 174
    (
        'уфа проспект октябрь 125',
        {'entities': [(4, 20, 'addr:street'), (21, 24, 'addr:housenumber')]}
    ),

    # Sample 175
    (
        'омск маркс 41',
        {'entities': [(5, 10, 'addr:street'), (11, 13, 'addr:housenumber')]}
    ),

    # Sample 176
    (
        'челябинск улица киров 104',
        {'entities': [(10, 21, 'addr:street'), (22, 25, 'addr:housenumber')]}
    ),

    # Sample 177
    (
        '454091 челябинск свердловский проспект дом 60',
        {'entities': [(0, 6, 'addr:postcode'), (17, 38, 'addr:street'), (43, 45, 'addr:housenumber')]}
    ),

    # Sample 178
    (
        'тюмень улица республика дом 24/1',
        {'entities': [(7, 23, 'addr:street'), (28, 32, 'addr:housenumber')]}
    ),

    # Sample 179
    (
        'иркутск карла маркс 16',
        {'entities': [(8, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 180
    (
        'хабаровск муравьёв-амурский 23 квартира 15',
        {'entities': [(10, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 181
    (
        'москва улица арбат дом 28',
        {'entities': [(7, 18, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 182
    (
        '630102 новосибирск красный проспект 82',
        {'entities': [(0, 6, 'addr:postcode'), (19, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 183
    (
        'санкт-петербург невский пр 45 корп 1',
        {'entities': [(16, 26, 'addr:street'), (27, 36, 'addr:housenumber')]}
    ),

    # Sample 184
    (
        'екатеринбург улица ленин 52',
        {'entities': [(13, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 185
    (
        'казань бауман 12/15',
        {'entities': [(7, 13, 'addr:street'), (14, 19, 'addr:housenumber')]}
    ),

    # Sample 186
    (
        'нижний новгород улица больший покровский дом 29',
        {'entities': [(16, 40, 'addr:street'), (45, 47, 'addr:housenumber')]}
    ),

    # Sample 187
    (
        'владивосток светланский улица дом 33',
        {'entities': [(12, 29, 'addr:street'), (34, 36, 'addr:housenumber')]}
    ),

    # Sample 188
    (
        'краснодар улица красный 154',
        {'entities': [(10, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 189
    (
        'ростов-на-дон проспект будённовский 93',
        {'entities': [(14, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 190
    (
        'уфа ленин 42 корп 3',
        {'entities': [(4, 9, 'addr:street'), (10, 19, 'addr:housenumber')]}
    ),

    # Sample 191
    (
        '420012 казань дом 18 улица кремлёвский',
        {'entities': [(0, 6, 'addr:postcode'), (21, 38, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 192
    (
        'самара московский шоссе 15а',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 193
    (
        'омск улица ленин дом 22',
        {'entities': [(5, 16, 'addr:street'), (21, 23, 'addr:housenumber')]}
    ),

    # Sample 194
    (
        'челябинск пр ленин 56',
        {'entities': [(10, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 195
    (
        'воронеж улица кольцовский 35',
        {'entities': [(8, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 196
    (
        'спб набережная канал грибоедов 7',
        {'entities': [(4, 30, 'addr:street'), (31, 32, 'addr:housenumber')]}
    ),

    # Sample 197
    (
        'пермь улица ленин дом 68',
        {'entities': [(6, 17, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 198
    (
        'волгоград проспект ленин 10 корпус 2',
        {'entities': [(10, 24, 'addr:street'), (25, 36, 'addr:housenumber')]}
    ),

    # Sample 199
    (
        'тюмень улица республика 142',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 200
    (
        'иркутск карла маркс 25',
        {'entities': [(8, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),
]



def train_spacy_ner(train_data, n_iter=30, model_dir="./spacy_geo_model"):
    """
    Обучаем NER с нуля, без базовой модели
    """
    # Создаем пустую русскую модель
    nlp = spacy.blank("ru")

    # Добавляем ТОЛЬКО NER компонент
    ner = nlp.add_pipe("ner")

    # Добавляем наши метки
    for _, annotations in train_data:
        for ent in annotations.get("entities", []):
            ner.add_label(ent[2])

    print(f"Метки NER: {ner.labels}")

    # Создаем примеры
    examples = []
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        examples.append(Example.from_dict(doc, annotations))

    # Инициализируем
    nlp.initialize(lambda: examples)

    # Обучаем
    for itn in range(n_iter):
        losses = {}
        random.shuffle(examples)
        nlp.update(examples, drop=0.5, losses=losses)

        if itn % 500 == 0:
            print(f"Epoch {itn}, Loss: {losses['ner']:.4f}")

    # Тест ДО сохранения
    text, _ = train_data[0]
    doc = nlp(text)
    print(f"\n✓ Результат ДО сохранения: {[(ent.text, ent.label_) for ent in doc.ents]}")

    # === СОХРАНЕНИЕ МОДЕЛИ ===
    output_dir = Path(model_dir)
    if output_dir.exists():
        import shutil
        shutil.rmtree(output_dir)  # Удаляем старую модель!

    output_dir.mkdir(parents=True, exist_ok=True)
    nlp.to_disk(output_dir)
    print(f"\n✓ Модель сохранена в {output_dir}")

    return nlp


# Обучение
trained_nlp = train_spacy_ner(TRAIN_DATA, n_iter=30)

# === ТЕСТ ПОСЛЕ ЗАГРУЗКИ ===
print("\n" + "=" * 70)
print("ТЕСТ: Загрузка модели с диска")
print("=" * 70)

output_dir = "./spacy_geo_model"
nlp_loaded = spacy.load(output_dir)

while True:
    test_text = input("москва ул арбат далее 28 кв 15: ")
    doc = nlp_loaded(test_text)

    print(f"\nТекст: '{test_text}'")
    print(f"✓ Результат ПОСЛЕ загрузки:")
    for ent in doc.ents:
        print(f"  '{ent.text}' -> {ent.label_}")
