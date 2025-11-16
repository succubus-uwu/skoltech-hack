"""
Training Data for Address NER
Generated: 2025-11-16 05:36:27.844007
Total samples: 200
"""

train_data = [
    (
        'москва улица арбат 25',
        {'entities': [(7, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 3
    (
        'спб невский проспект 88 к2',
        {'entities': [(4, 20, 'addr:street'), (21, 26, 'addr:housenumber')]}
    ),

    # Sample 4
    (
        'екатеринбург улица ленин 54а',
        {'entities': [(13, 24, 'addr:street'), (25, 28, 'addr:housenumber')]}
    ),

    # Sample 5
    (
        'казань бауман 12 к1 с1',
        {'entities': [(7, 13, 'addr:street'), (14, 22, 'addr:housenumber')]}
    ),

    # Sample 6
    (
        'новосибирск красный проспект 100',
        {'entities': [(12, 28, 'addr:street'), (29, 32, 'addr:housenumber')]}
    ),

    # Sample 7
    (
        '125047 москва тверская улица 15',
        {'entities': [(0, 6, 'addr:postcode'), (14, 28, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 8
    (
        'нижний новгород больший покровский 45',
        {'entities': [(16, 34, 'addr:street'), (35, 37, 'addr:housenumber')]}
    ),

    # Sample 9
    (
        'самара улица молодогвардейский 67 к3',
        {'entities': [(7, 30, 'addr:street'), (31, 36, 'addr:housenumber')]}
    ),

    # Sample 10
    (
        'омск проспект мир 33',
        {'entities': [(5, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 11
    (
        'челябинск улица киров 89',
        {'entities': [(10, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 12
    (
        'ростов-на-дон больший садовый 112',
        {'entities': [(14, 29, 'addr:street'), (30, 33, 'addr:housenumber')]}
    ),

    # Sample 13
    (
        'уфа пр октябрь 25 к2',
        {'entities': [(4, 14, 'addr:street'), (15, 20, 'addr:housenumber')]}
    ),

    # Sample 14
    (
        'красноярск улица мир 88',
        {'entities': [(11, 20, 'addr:street'), (21, 23, 'addr:housenumber')]}
    ),

    # Sample 15
    (
        'воронеж проспект революция 56',
        {'entities': [(8, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 16
    (
        'пермь улица ленин 78 к1',
        {'entities': [(6, 17, 'addr:street'), (18, 23, 'addr:housenumber')]}
    ),

    # Sample 17
    (
        '119021 москва остоженка улица 10',
        {'entities': [(0, 6, 'addr:postcode'), (14, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 18
    (
        'волгоград проспект ленин 92',
        {'entities': [(10, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 19
    (
        'краснодар красный улица 145',
        {'entities': [(18, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 20
    (
        'саратов московский 67',
        {'entities': [(8, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 21
    (
        'тюмень улица республика 142',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 22
    (
        'ижевск улица пушкинский 268',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 23
    (
        'барнаул пр ленин 54',
        {'entities': [(8, 16, 'addr:street'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 24
    (
        'ульяновск гончаров 28',
        {'entities': [(10, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 25
    (
        'иркутск улица карла маркс 45 к2',
        {'entities': [(8, 25, 'addr:street'), (26, 31, 'addr:housenumber')]}
    ),

    # Sample 26
    (
        'хабаровск муравьёв-амурский 18',
        {'entities': [(10, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 27
    (
        'ярославль советский площадь 3',
        {'entities': [(10, 27, 'addr:street'), (28, 29, 'addr:housenumber')]}
    ),

    # Sample 28
    (
        'владивосток светланский 22',
        {'entities': [(12, 23, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 29
    (
        'махачкала пр имам шамиль 67',
        {'entities': [(10, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 30
    (
        'томск пр ленин 36',
        {'entities': [(6, 14, 'addr:street'), (15, 17, 'addr:housenumber')]}
    ),

    # Sample 31
    (
        'оренбург улица советский 8',
        {'entities': [(9, 24, 'addr:street'), (25, 26, 'addr:housenumber')]}
    ),

    # Sample 32
    (
        'кемерово советский проспект 63 к1',
        {'entities': [(9, 27, 'addr:street'), (28, 33, 'addr:housenumber')]}
    ),

    # Sample 33
    (
        'новокузнецк киров 55',
        {'entities': [(12, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 34
    (
        'рязань почтовый 61',
        {'entities': [(7, 15, 'addr:street'), (16, 18, 'addr:housenumber')]}
    ),

    # Sample 35
    (
        'астрахань улица киров 14',
        {'entities': [(10, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 36
    (
        'пенза московский 83',
        {'entities': [(6, 16, 'addr:street'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 37
    (
        'липецк пр победа 7',
        {'entities': [(7, 16, 'addr:street'), (17, 18, 'addr:housenumber')]}
    ),

    # Sample 38
    (
        'киров октябрьский проспект 120',
        {'entities': [(6, 26, 'addr:street'), (27, 30, 'addr:housenumber')]}
    ),

    # Sample 39
    (
        'чебоксары московский пр 19 к2',
        {'entities': [(10, 23, 'addr:street'), (24, 29, 'addr:housenumber')]}
    ),

    # Sample 40
    (
        'калининград ленинский проспект 81',
        {'entities': [(12, 30, 'addr:street'), (31, 33, 'addr:housenumber')]}
    ),

    # Sample 41
    (
        'тула проспект ленин 99',
        {'entities': [(5, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 42
    (
        'курск улица ленин 1',
        {'entities': [(6, 17, 'addr:street'), (18, 19, 'addr:housenumber')]}
    ),

    # Sample 43
    (
        'ставрополь пр карла маркс 72',
        {'entities': [(11, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 44
    (
        'сочи курортный проспект 108',
        {'entities': [(5, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 45
    (
        'улан-удэ улица ленин 54',
        {'entities': [(9, 20, 'addr:street'), (21, 23, 'addr:housenumber')]}
    ),

    # Sample 46
    (
        'тверь советский 33',
        {'entities': [(6, 15, 'addr:street'), (16, 18, 'addr:housenumber')]}
    ),

    # Sample 47
    (
        'магнитогорск пр ленин 124 к3',
        {'entities': [(13, 21, 'addr:street'), (22, 28, 'addr:housenumber')]}
    ),

    # Sample 48
    (
        'иваново пр ленин 67',
        {'entities': [(8, 16, 'addr:street'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 49
    (
        'брянск проспект ленин 35',
        {'entities': [(7, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 50
    (
        'белгород народный бульвар 89',
        {'entities': [(9, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 51
    (
        'сургут улица ленин 44',
        {'entities': [(7, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 52
    (
        'владимир больший московский 27',
        {'entities': [(9, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 53
    (
        'нижний тагил пр ленин 1',
        {'entities': [(13, 21, 'addr:street'), (22, 23, 'addr:housenumber')]}
    ),

    # Sample 54
    (
        'архангельск пр троицкий 61',
        {'entities': [(12, 23, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 55
    (
        'чита улица ленин 85',
        {'entities': [(5, 16, 'addr:street'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 56
    (
        'калуга улица киров 1',
        {'entities': [(7, 18, 'addr:street'), (19, 20, 'addr:housenumber')]}
    ),

    # Sample 57
    (
        'смоленск пр гагарин 12а',
        {'entities': [(9, 19, 'addr:street'), (20, 23, 'addr:housenumber')]}
    ),

    # Sample 58
    (
        'волжский пр ленин 97',
        {'entities': [(9, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 59
    (
        'курган улица гоголь 56',
        {'entities': [(7, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 60
    (
        'орёл московский 118',
        {'entities': [(5, 15, 'addr:street'), (16, 19, 'addr:housenumber')]}
    ),

    # Sample 61
    (
        'череповец советский проспект 88',
        {'entities': [(10, 28, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 62
    (
        'вологда мир 93',
        {'entities': [(8, 11, 'addr:street'), (12, 14, 'addr:housenumber')]}
    ),

    # Sample 63
    (
        'владикавказ пр мир 17',
        {'entities': [(12, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 64
    (
        'мурманск пр ленин 82',
        {'entities': [(9, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 65
    (
        'саранск советский 55',
        {'entities': [(18, 20, 'addr:housenumber')]}
    ),

    # Sample 66
    (
        'якутск улица киров 18',
        {'entities': [(7, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 67
    (
        'тамбов советский 106',
        {'entities': [(7, 16, 'addr:street'), (17, 20, 'addr:housenumber')]}
    ),

    # Sample 68
    (
        'грозный пр путин 10',
        {'entities': [(8, 16, 'addr:street'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 69
    (
        'стерлитамак пр октябрь 68',
        {'entities': [(12, 22, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 70
    (
        'кострома советский 2',
        {'entities': [(9, 18, 'addr:street'), (19, 20, 'addr:housenumber')]}
    ),

    # Sample 71
    (
        'петрозаводск пр ленин 29',
        {'entities': [(13, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 72
    (
        'нижневартовск улица ленин 9а к2',
        {'entities': [(14, 25, 'addr:street'), (26, 31, 'addr:housenumber')]}
    ),

    # Sample 73
    (
        'йошкара-ola ленинский проспект 24',
        {'entities': [(12, 30, 'addr:street'), (31, 33, 'addr:housenumber')]}
    ),

    # Sample 74
    (
        'новороссийск совет 12',
        {'entities': [(13, 21, 'addr:housenumber')]}
    ),

    # Sample 75
    (
        'комсомольск-на-амур пр ленин 38',
        {'entities': [(20, 28, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 76
    (
        'таганрог петровский 104',
        {'entities': [(9, 19, 'addr:street'), (20, 23, 'addr:housenumber')]}
    ),

    # Sample 77
    (
        'сыктывкар коммунистический 67',
        {'entities': [(10, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 78
    (
        'нальчик пр ленин 33',
        {'entities': [(8, 16, 'addr:street'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 79
    (
        'шахта советский 155',
        {'entities': [(16, 19, 'addr:housenumber')]}
    ),

    # Sample 80
    (
        'дзержинск пр циолковский 21',
        {'entities': [(10, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 81
    (
        'нижнекамск пр химик 45',
        {'entities': [(11, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 82
    (
        'братск улица мир 39',
        {'entities': [(7, 16, 'addr:street'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 83
    (
        'ангарск квартал 85 дом 10',
        {'entities': [(16, 18, 'addr:housenumber')]}
    ),

    # Sample 84
    (
        'орск пр ленин 12',
        {'entities': [(5, 13, 'addr:street'), (14, 16, 'addr:housenumber')]}
    ),

    # Sample 85
    (
        'старый оскол микрорайон олимпийский 15',
        {'entities': [(13, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 86
    (
        'великий новгород больший московский 24',
        {'entities': [(17, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 87
    (
        'благовещенск улица ленин 108',
        {'entities': [(13, 24, 'addr:street'), (25, 28, 'addr:housenumber')]}
    ),

    # Sample 88
    (
        'энгельс пр строитель 7',
        {'entities': [(8, 20, 'addr:street'), (21, 22, 'addr:housenumber')]}
    ),

    # Sample 89
    (
        'подольск улица киров 63',
        {'entities': [(9, 20, 'addr:street'), (21, 23, 'addr:housenumber')]}
    ),

    # Sample 90
    (
        'псков октябрьский проспект 34',
        {'entities': [(6, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 91
    (
        'бийск улица советский 250',
        {'entities': [(6, 21, 'addr:street'), (22, 25, 'addr:housenumber')]}
    ),

    # Sample 92
    (
        'прокопьевск улица ноградский 27',
        {'entities': [(12, 28, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 93
    (
        'рыбинск крестовый 118',
        {'entities': [(8, 17, 'addr:street'), (18, 21, 'addr:housenumber')]}
    ),

    # Sample 94
    (
        'балаково саратовский шоссе 89',
        {'entities': [(9, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 95
    (
        'армавир улица киров 58',
        {'entities': [(8, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 96
    (
        'северодвинск ломоносов 85',
        {'entities': [(13, 22, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 97
    (
        'королёв пр королёв 14 к1',
        {'entities': [(8, 18, 'addr:street'), (19, 24, 'addr:housenumber')]}
    ),

    # Sample 98
    (
        'петропавловск-камчатский пр победа 62',
        {'entities': [(25, 34, 'addr:street'), (35, 37, 'addr:housenumber')]}
    ),

    # Sample 99
    (
        'мытищи олимпийский проспект 29',
        {'entities': [(7, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 100
    (
        'сызрань советский 45',
        {'entities': [(8, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 101
    (
        'вот 100 различный российский адрес',
        {'entities': []}
    ),

    # Sample 102
    (
        'москва улица арбат 25 к1',
        {'entities': [(7, 18, 'addr:street'), (19, 24, 'addr:housenumber')]}
    ),

    # Sample 103
    (
        'спб невский проспект 108',
        {'entities': [(4, 20, 'addr:street'), (21, 24, 'addr:housenumber')]}
    ),

    # Sample 104
    (
        'екатеринburg улица ленин 45 к2',
        {'entities': [(13, 24, 'addr:street'), (25, 30, 'addr:housenumber')]}
    ),

    # Sample 105
    (
        'казань бауман 67',
        {'entities': [(7, 13, 'addr:street'), (14, 16, 'addr:housenumber')]}
    ),

    # Sample 106
    (
        'новосибирск красный проспект 120/3',
        {'entities': [(12, 28, 'addr:street'), (29, 34, 'addr:housenumber')]}
    ),

    # Sample 107
    (
        '125047 москва тверская улица 15',
        {'entities': [(0, 6, 'addr:postcode'), (14, 28, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 108
    (
        'нижний новгород больший покровский 88',
        {'entities': [(16, 34, 'addr:street'), (35, 37, 'addr:housenumber')]}
    ),

    # Sample 109
    (
        'самара улица ленинградский вл12 к3',
        {'entities': [(7, 26, 'addr:street'), (27, 34, 'addr:housenumber')]}
    ),

    # Sample 110
    (
        'омск проспект мир 56',
        {'entities': [(5, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 111
    (
        'челябинск улица киров 101 с1',
        {'entities': [(10, 21, 'addr:street'), (22, 28, 'addr:housenumber')]}
    ),

    # Sample 112
    (
        '190000 спб набережная река фонтанка 34',
        {'entities': [(0, 6, 'addr:postcode'), (11, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 113
    (
        'ростов-на-дон больший садовый улица 79',
        {'entities': [(14, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 114
    (
        'уфа проспект октябрь 45 к2',
        {'entities': [(4, 20, 'addr:street'), (21, 26, 'addr:housenumber')]}
    ),

    # Sample 115
    (
        'красноярск улица мир 88',
        {'entities': [(11, 20, 'addr:street'), (21, 23, 'addr:housenumber')]}
    ),

    # Sample 116
    (
        'воронеж революция проспект 23',
        {'entities': [(8, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 117
    (
        'пермь улица ленин вл67 к1',
        {'entities': [(6, 17, 'addr:street'), (18, 25, 'addr:housenumber')]}
    ),

    # Sample 118
    (
        'волгоград проспект ленин 112',
        {'entities': [(10, 24, 'addr:street'), (25, 28, 'addr:housenumber')]}
    ),

    # Sample 119
    (
        'краснодар красный улица 145',
        {'entities': [(18, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 120
    (
        'саратов московский 89 к3',
        {'entities': [(8, 18, 'addr:street'), (19, 24, 'addr:housenumber')]}
    ),

    # Sample 121
    (
        'тюмень улица республика 55',
        {'entities': [(7, 23, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 122
    (
        '620014 екатеринбург малышев 78',
        {'entities': [(0, 6, 'addr:postcode'), (20, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 123
    (
        'тольятти автозаводский шоссе 23',
        {'entities': [(9, 28, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 124
    (
        'ижевск улица пушкинский 267',
        {'entities': [(7, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 125
    (
        'барнаул проспект ленин 99',
        {'entities': [(8, 22, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 126
    (
        'ульяновск гончаров 28 к1',
        {'entities': [(19, 24, 'addr:housenumber')]}
    ),

    # Sample 127
    (
        'иркутск улица карла маркс 45',
        {'entities': [(8, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 128
    (
        'хабаровск муравьёв-амурский 23',
        {'entities': [(10, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 129
    (
        'ярославль свобода улица 67 к2',
        {'entities': [(10, 23, 'addr:street'), (24, 29, 'addr:housenumber')]}
    ),

    # Sample 130
    (
        'владивосток светланский 88',
        {'entities': [(12, 23, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 131
    (
        'махачкала проспект имам шамиль 56',
        {'entities': [(10, 30, 'addr:street'), (31, 33, 'addr:housenumber')]}
    ),

    # Sample 132
    (
        'томск проспект ленин 134',
        {'entities': [(6, 20, 'addr:street'), (21, 24, 'addr:housenumber')]}
    ),

    # Sample 133
    (
        'оренбург улица советский 78',
        {'entities': [(9, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 134
    (
        'кемерово весенний 20',
        {'entities': [(9, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 135
    (
        'новокузнецк металлург проспект 45',
        {'entities': [(12, 30, 'addr:street'), (31, 33, 'addr:housenumber')]}
    ),

    # Sample 136
    (
        'рязань почтовый улица 67',
        {'entities': [(7, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 137
    (
        'астрахань улица киров 34 к1',
        {'entities': [(10, 21, 'addr:street'), (22, 27, 'addr:housenumber')]}
    ),

    # Sample 138
    (
        'пенза московский 89',
        {'entities': [(6, 16, 'addr:street'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 139
    (
        'липецк проспект победа 23',
        {'entities': [(7, 22, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 140
    (
        'киров улица ленин 102',
        {'entities': [(6, 17, 'addr:street'), (18, 21, 'addr:housenumber')]}
    ),

    # Sample 141
    (
        'чебоксары московский проспект 56',
        {'entities': [(10, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 142
    (
        'калининград ленинский проспект 78 к2',
        {'entities': [(12, 30, 'addr:street'), (31, 36, 'addr:housenumber')]}
    ),

    # Sample 143
    (
        'брянск проспект ленин 45',
        {'entities': [(7, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 144
    (
        'курск улица ленин 67',
        {'entities': [(6, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 145
    (
        'иваново шереметевский проспект 89',
        {'entities': [(8, 30, 'addr:street'), (31, 33, 'addr:housenumber')]}
    ),

    # Sample 146
    (
        'магнитогорск ленин 134',
        {'entities': [(13, 18, 'addr:street'), (19, 22, 'addr:housenumber')]}
    ),

    # Sample 147
    (
        'тверь советский улица 56',
        {'entities': [(16, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 148
    (
        'ставрополь проспект карла маркс 78',
        {'entities': [(11, 31, 'addr:street'), (32, 34, 'addr:housenumber')]}
    ),

    # Sample 149
    (
        'нижний тагил улица мир 45',
        {'entities': [(13, 22, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 150
    (
        'белгород народный бульвар 23',
        {'entities': [(9, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 151
    (
        'архангельск троицкий проспект 67',
        {'entities': [(12, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 152
    (
        'владимир больший московский улица 89',
        {'entities': [(17, 33, 'addr:street'), (34, 36, 'addr:housenumber')]}
    ),

    # Sample 153
    (
        'сочи курортный проспект 102',
        {'entities': [(5, 23, 'addr:street'), (24, 27, 'addr:housenumber')]}
    ),

    # Sample 154
    (
        'курган улица гоголь 34',
        {'entities': [(7, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 155
    (
        'смоленск проспект гагарин 56',
        {'entities': [(9, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 156
    (
        'калуга улица киров 78',
        {'entities': [(7, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 157
    (
        'чита ленин 45 к1',
        {'entities': [(5, 10, 'addr:street'), (11, 16, 'addr:housenumber')]}
    ),

    # Sample 158
    (
        'орёл московский улица 67',
        {'entities': [(5, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 159
    (
        'волжский проспект ленин 89 с3',
        {'entities': [(0, 17, 'addr:street'), (24, 29, 'addr:housenumber')]}
    ),

    # Sample 160
    (
        'череповец советский проспект 23 с3',
        {'entities': [(10, 28, 'addr:street'), (29, 34, 'addr:housenumber')]}
    ),

    # Sample 161
    (
        'владикавказ проспект мир вл56',
        {'entities': [(12, 24, 'addr:street'), (25, 29, 'addr:housenumber')]}
    ),

    # Sample 162
    (
        'мурманск ленин вл78А',
        {'entities': [(9, 14, 'addr:street'), (15, 20, 'addr:housenumber')]}
    ),

    # Sample 163
    (
        'сургут улица ленин 102',
        {'entities': [(7, 18, 'addr:street'), (19, 22, 'addr:housenumber')]}
    ),

    # Sample 164
    (
        'вологда мир 34',
        {'entities': [(8, 11, 'addr:street'), (12, 14, 'addr:housenumber')]}
    ),

    # Sample 165
    (
        'саранск советский улица 56 к2',
        {'entities': [(18, 23, 'addr:street'), (24, 29, 'addr:housenumber')]}
    ),

    # Sample 166
    (
        'тамбов интернациональный 78',
        {'entities': [(7, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 167
    (
        'стерлитамак проспект октябрь 45',
        {'entities': [(12, 28, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 168
    (
        'грозный проспект кадыров 67',
        {'entities': [(8, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 169
    (
        'якутск улица ленин 89',
        {'entities': [(7, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 170
    (
        'кострома советский 23',
        {'entities': [(9, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 171
    (
        'петрозаводск проспект ленин 56',
        {'entities': [(13, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 172
    (
        'нижневартовск улица ленин 78',
        {'entities': [(14, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 173
    (
        'новороссийск совет 45',
        {'entities': [(13, 21, 'addr:housenumber')]}
    ),

    # Sample 174
    (
        'йошкара-ола ленинский проспект 67 к1',
        {'entities': [(12, 30, 'addr:street'), (31, 36, 'addr:housenumber')]}
    ),

    # Sample 175
    (
        'химки юбилейный проспект 89',
        {'entities': [(6, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 176
    (
        'таганрог петровский улица 23',
        {'entities': [(9, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 177
    (
        'комсомольск-на-амур проспект ленин 56',
        {'entities': [(20, 34, 'addr:street'), (35, 37, 'addr:housenumber')]}
    ),

    # Sample 178
    (
        'сыктывкар коммунистический 78',
        {'entities': [(10, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 179
    (
        'нижнекамск проспект химик 45',
        {'entities': [(11, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 180
    (
        'мытищи олимпийский проспект 67',
        {'entities': [(7, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 181
    (
        'балашиха улица советский 89',
        {'entities': [(9, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 182
    (
        'шахта проспект победа 23',
        {'entities': [(6, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 183
    (
        'дзержинск гайдар 56',
        {'entities': [(10, 16, 'addr:street'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 184
    (
        'орск ленин 78 к2',
        {'entities': [(5, 10, 'addr:street'), (11, 16, 'addr:housenumber')]}
    ),

    # Sample 185
    (
        'ангарск квартал 85 дом 45',
        {'entities': [(23, 25, 'addr:housenumber')]}
    ),

    # Sample 186
    (
        'благовещенск улица ленин 67',
        {'entities': [(13, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 187
    (
        'великий новгород больший санкт-петербургский 89',
        {'entities': [(17, 44, 'addr:street'), (45, 47, 'addr:housenumber')]}
    ),

    # Sample 188
    (
        'псков октябрьский проспект 23',
        {'entities': [(6, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 189
    (
        'бийск улица советский 56',
        {'entities': [(6, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 190
    (
        'прокопьевск шахтёр 78',
        {'entities': [(12, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 191
    (
        'рыбинск крестовый улица 45',
        {'entities': [(8, 23, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 192
    (
        'балаково саратовский шоссе 67',
        {'entities': [(9, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 193
    (
        'армавир улица ленин 89 к1',
        {'entities': [(8, 19, 'addr:street'), (20, 25, 'addr:housenumber')]}
    ),

    # Sample 194
    (
        'северодвинск ломоносов 23',
        {'entities': [(13, 22, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 195
    (
        'подольск революционный проспект 56',
        {'entities': [(9, 31, 'addr:street'), (32, 34, 'addr:housenumber')]}
    ),

    # Sample 196
    (
        'королева проспект космонавт 78',
        {'entities': [(9, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 197
    (
        'сызрань советский улица 45',
        {'entities': [(18, 23, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 198
    (
        'петропавловск-камчатский проспект победа 67',
        {'entities': [(25, 40, 'addr:street'), (41, 43, 'addr:housenumber')]}
    ),

    # Sample 199
    (
        'каменск-уральский алюминиевый 89',
        {'entities': [(18, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

    # Sample 200
    (
        'новочеркасск московский улица 23',
        {'entities': [(13, 29, 'addr:street'), (30, 32, 'addr:housenumber')]}
    ),

]
