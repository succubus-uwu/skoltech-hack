"""
Training Data for Address NER
Generated: 2025-11-16 10:30:57.868736
Total samples: 200
"""

TRAIN_DATA = [
    # Sample 1
    (
        'саратов фестивальный улица 69',
        {'entities': [(0, 7, 'addr:city'), (8, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 2
    (
        'хорошёвский шоссе 123007 64а с2',
        {'entities': [(0, 17, 'addr:street'), (18, 24, 'addr:postcode'), (25, 31, 'addr:housenumber')]}
    ),

    # Sample 3
    (
        'нежинский улица 119501 5 с1',
        {'entities': [(10, 15, 'addr:street'), (16, 22, 'addr:postcode'), (23, 27, 'addr:housenumber')]}
    ),

    # Sample 4
    (
        '103073',
        {'entities': [(0, 6, 'addr:postcode')]}
    ),

    # Sample 5
    (
        'москва новгородский улица 12',
        {'entities': [(0, 6, 'addr:city'), (7, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 6
    (
        'москва 78с1 проспект вернадский',
        {'entities': [(0, 6, 'addr:city'), (7, 11, 'addr:housenumber'), (12, 31, 'addr:street')]}
    ),

    # Sample 7
    (
        '19 улица прянишников спб',
        {'entities': [(3, 20, 'addr:street'), (0, 2, 'addr:housenumber'), (21, 24, 'addr:city')]}
    ),

    # Sample 8
    (
        'волоколамский шоссе 73',
        {'entities': [(0, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 9
    (
        'улица маршал катуков 21 к2',
        {'entities': [(0, 20, 'addr:street'), (21, 26, 'addr:housenumber')]}
    ),

    # Sample 10
    (
        'строгинский бульвар 123458 14 к5 казань',
        {'entities': [(0, 19, 'addr:street'), (20, 26, 'addr:postcode'), (27, 32, 'addr:housenumber'), (33, 39, 'addr:city')]}
    ),

    # Sample 11
    (
        'бескудниковский бульвар 59а с2а улан уд',
        {'entities': [(0, 23, 'addr:street'), (24, 31, 'addr:housenumber'), (32, 39, 'addr:city')]}
    ),

    # Sample 12
    (
        'дмитровский шоссе 60а 127474',
        {'entities': [(0, 17, 'addr:street'), (18, 21, 'addr:housenumber'), (22, 28, 'addr:postcode')]}
    ),

    # Sample 13
    (
        '17 к2 улица кулаковый',
        {'entities': [(3, 5, 'addr:housenumber'), (6, 21, 'addr:street')]}
    ),

    # Sample 14
    (
        'севастопольский проспект 24а сколково',
        {'entities': [(0, 24, 'addr:street'), (25, 28, 'addr:housenumber'), (29, 37, 'addr:city')]}
    ),

    # Sample 15
    (
        '87 к1 улица удальцов',
        {'entities': [(3, 5, 'addr:housenumber'), (6, 20, 'addr:street')]}
    ),

    # Sample 16
    (
        '15 шенкурский проезд',
        {'entities': [(3, 20, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 17
    (
        'ленинградский проспект 37 к1 москва',
        {'entities': [(0, 22, 'addr:street'), (23, 28, 'addr:housenumber'), (29, 35, 'addr:city')]}
    ),

    # Sample 18
    (
        '127253 псковский улица 12 к3',
        {'entities': [(0, 6, 'addr:postcode'), (7, 22, 'addr:street'), (23, 28, 'addr:housenumber')]}
    ),

    # Sample 19
    (
        'улица плещеев 127560 26а',
        {'entities': [(0, 13, 'addr:street'), (14, 20, 'addr:postcode'), (21, 24, 'addr:housenumber')]}
    ),

    # Sample 20
    (
        '4а 127560 улица конёнкова брянск',
        {'entities': [(3, 9, 'addr:postcode'), (10, 25, 'addr:street'), (0, 2, 'addr:housenumber'), (26, 32, 'addr:city')]}
    ),

    # Sample 21
    (
        '25а улица лесков',
        {'entities': [(4, 16, 'addr:street'), (0, 3, 'addr:housenumber')]}
    ),

    # Sample 22
    (
        'шипиловский улица 17 к1',
        {'entities': [(0, 17, 'addr:street'), (18, 23, 'addr:housenumber')]}
    ),

    # Sample 23
    (
        'роман переулок 5 липецк',
        {'entities': [(0, 14, 'addr:street'), (15, 16, 'addr:housenumber'), (17, 23, 'addr:city')]}
    ),

    # Sample 24
    (
        '7/5 с3 улица больший дмитровка',
        {'entities': [(0, 6, 'addr:housenumber'), (7, 30, 'addr:street')]}
    ),

    # Sample 25
    (
        '125009 13 тверская улица берлин',
        {'entities': [(0, 6, 'addr:postcode'), (7, 9, 'addr:housenumber'), (10, 24, 'addr:street'), (25, 31, 'addr:city')]}
    ),

    # Sample 26
    (
        'театральный проезд 2',
        {'entities': [(0, 18, 'addr:street'), (19, 20, 'addr:housenumber')]}
    ),

    # Sample 27
    (
        '13 цветной бульвар',
        {'entities': [(3, 18, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 28
    (
        'мерзляковский переулок 15',
        {'entities': [(0, 22, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 29
    (
        'улица твардовский 2 к2',
        {'entities': [(0, 17, 'addr:street'), (18, 22, 'addr:housenumber')]}
    ),

    # Sample 30
    (
        'дмитровский шоссе 81',
        {'entities': [(0, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 31
    (
        '109559 11 белореченский улица',
        {'entities': [(0, 6, 'addr:postcode'), (7, 9, 'addr:housenumber'), (10, 29, 'addr:street')]}
    ),

    # Sample 32
    (
        '117535 дорожный улица 20а',
        {'entities': [(0, 6, 'addr:postcode'), (7, 21, 'addr:street'), (22, 25, 'addr:housenumber')]}
    ),

    # Sample 33
    (
        '117519 кировоградский улица 21',
        {'entities': [(0, 6, 'addr:postcode'), (7, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 34
    (
        '35г улица яблочкова',
        {'entities': [(2, 3, 'addr:housenumber'), (4, 19, 'addr:street')]}
    ),

    # Sample 35
    (
        'улица островитянов 1',
        {'entities': [(0, 18, 'addr:street'), (19, 20, 'addr:housenumber')]}
    ),

    # Sample 36
    (
        '101 к6 проспект вернадский 119526',
        {'entities': [(4, 6, 'addr:housenumber'), (7, 26, 'addr:street'), (27, 33, 'addr:postcode')]}
    ),

    # Sample 37
    (
        '2 к2 улица кулаковый',
        {'entities': [(2, 4, 'addr:housenumber'), (5, 20, 'addr:street')]}
    ),

    # Sample 38
    (
        'улица кулаковый 3 к1',
        {'entities': [(0, 15, 'addr:street'), (16, 20, 'addr:housenumber')]}
    ),

    # Sample 39
    (
        '58 кантемировский улица',
        {'entities': [(3, 23, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 40
    (
        '7 к4 клязьминский улица',
        {'entities': [(2, 4, 'addr:housenumber'), (5, 23, 'addr:street')]}
    ),

    # Sample 41
    (
        'профсоюзный улица 61',
        {'entities': [(0, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 42
    (
        '61 к1 профсоюзный улица',
        {'entities': [(3, 5, 'addr:housenumber'), (6, 23, 'addr:street')]}
    ),

    # Sample 43
    (
        '35 мосфильмовский улица',
        {'entities': [(3, 23, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 44
    (
        '119607 85 улица удальцов',
        {'entities': [(0, 6, 'addr:postcode'), (7, 9, 'addr:housenumber'), (10, 24, 'addr:street')]}
    ),

    # Sample 45
    (
        '127549 бибиревский улица 5',
        {'entities': [(0, 6, 'addr:postcode'), (7, 24, 'addr:street'), (25, 26, 'addr:housenumber')]}
    ),

    # Sample 46
    (
        '117587 126а варшавский шоссе',
        {'entities': [(0, 6, 'addr:postcode'), (7, 11, 'addr:housenumber'), (12, 28, 'addr:street')]}
    ),

    # Sample 47
    (
        '12 улица иван франко',
        {'entities': [(3, 20, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 48
    (
        '16 больший бронный улица',
        {'entities': [(3, 24, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 49
    (
        '115569 улица маршал захаров 8 к1',
        {'entities': [(0, 6, 'addr:postcode'), (7, 27, 'addr:street'), (28, 32, 'addr:housenumber')]}
    ),

    # Sample 50
    (
        'улица санников 3 к3 127562',
        {'entities': [(0, 14, 'addr:street'), (15, 19, 'addr:housenumber'), (20, 26, 'addr:postcode')]}
    ),

    # Sample 51
    (
        'мохов улица 125009 15/1 с1',
        {'entities': [(6, 11, 'addr:street'), (12, 18, 'addr:postcode'), (19, 26, 'addr:housenumber')]}
    ),

    # Sample 52
    (
        '103073',
        {'entities': [(0, 6, 'addr:postcode')]}
    ),

    # Sample 53
    (
        '119501 нежинский улица 7',
        {'entities': [(0, 6, 'addr:postcode'), (7, 22, 'addr:street'), (23, 24, 'addr:housenumber')]}
    ),

    # Sample 54
    (
        '117648 к809',
        {'entities': [(0, 6, 'addr:postcode'), (7, 11, 'addr:housenumber')]}
    ),

    # Sample 55
    (
        'к810 117648',
        {'entities': [(5, 11, 'addr:postcode')]}
    ),

    # Sample 56
    (
        'проспект вернадский 78 с2',
        {'entities': [(0, 19, 'addr:street'), (20, 25, 'addr:housenumber')]}
    ),

    # Sample 57
    (
        'проспект вернадский 78 с3',
        {'entities': [(0, 19, 'addr:street'), (20, 25, 'addr:housenumber')]}
    ),

    # Sample 58
    (
        '78 с6 проспект вернадский',
        {'entities': [(3, 5, 'addr:housenumber'), (6, 25, 'addr:street')]}
    ),

    # Sample 59
    (
        '13 улица академик глушко',
        {'entities': [(3, 24, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 60
    (
        'феодосийский улица 1 к1 117628',
        {'entities': [(13, 18, 'addr:street'), (19, 23, 'addr:housenumber'), (24, 30, 'addr:postcode')]}
    ),

    # Sample 61
    (
        '49 ярославский шоссе',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 20, 'addr:street')]}
    ),

    # Sample 62
    (
        '94 алтуфьевский шоссе',
        {'entities': [(3, 21, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),
    # Sample 64
    (
        'улица академик скрябин 3',
        {'entities': [(0, 22, 'addr:street'), (23, 24, 'addr:housenumber')]}
    ),

    # Sample 65
    (
        'садовый-кудринский улица 25',
        {'entities': [(0, 24, 'addr:street'), (25, 27, 'addr:housenumber')]}
    ),

    # Sample 66
    (
        '109378 волгоградский проспект 169 к2',
        {'entities': [(0, 6, 'addr:postcode'), (7, 29, 'addr:street'), (30, 36, 'addr:housenumber')]}
    ),

    # Sample 67
    (
        '9 с9 улица образец',
        {'entities': [(2, 4, 'addr:housenumber'), (5, 18, 'addr:street')]}
    ),

    # Sample 68
    (
        '2 театральный площадь',
        {'entities': [(2, 21, 'addr:street'), (0, 1, 'addr:housenumber')]}
    ),

    # Sample 69
    (
        'страстный бульвар 5',
        {'entities': [(0, 17, 'addr:street'), (18, 19, 'addr:housenumber')]}
    ),

    # Sample 70
    (
        'олимпийский проспект 18/1',
        {'entities': [(0, 20, 'addr:street'), (21, 25, 'addr:housenumber')]}
    ),

    # Sample 71
    (
        'бульвар ян райнис 125373 43 к2',
        {'entities': [(0, 17, 'addr:street'), (18, 24, 'addr:postcode'), (25, 30, 'addr:housenumber')]}
    ),

    # Sample 72
    (
        '35 к2 улица юный ленинец',
        {'entities': [(3, 5, 'addr:housenumber'), (6, 24, 'addr:street')]}
    ),

    # Sample 73
    (
        'площадь академик курчатов 1 с20а 123098',
        {'entities': [(0, 25, 'addr:street'), (26, 32, 'addr:housenumber'), (33, 39, 'addr:postcode')]}
    ),

    # Sample 74
    (
        'улица миклухо-маклай 21а',
        {'entities': [(0, 20, 'addr:street'), (21, 24, 'addr:housenumber')]}
    ),

    # Sample 75
    (
        '12 к1 улица академик волгин',
        {'entities': [(3, 5, 'addr:housenumber'), (6, 27, 'addr:street')]}
    ),

    # Sample 76
    (
        'улица академик волгин 12',
        {'entities': [(0, 5, 'addr:street'), (6, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 77
    (
        '100 проспект вернадский',
        {'entities': [(4, 23, 'addr:street'), (0, 3, 'addr:housenumber')]}
    ),

    # Sample 78
    (
        '76 проспект вернадский',
        {'entities': [(3, 22, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 79
    (
        'варшавский шоссе 170г',
        {'entities': [(0, 16, 'addr:street'), (17, 21, 'addr:housenumber')]}
    ),

    # Sample 80
    (
        '117405 156б варшавский шоссе',
        {'entities': [(0, 6, 'addr:postcode'), (12, 28, 'addr:street'), (7, 11, 'addr:housenumber')]}
    ),

    # Sample 81
    (
        '110 с62 дмитровский шоссе',
        {'entities': [(4, 7, 'addr:housenumber'), (8, 25, 'addr:street')]}
    ),

    # Sample 82
    (
        'шоссейный улица 4д',
        {'entities': [(0, 15, 'addr:street'), (16, 18, 'addr:housenumber')]}
    ),

    # Sample 83
    (
        '105568 1 к1 улица чечулина',
        {'entities': [(0, 6, 'addr:postcode'), (7, 11, 'addr:housenumber'), (12, 26, 'addr:street')]}
    ),

    # Sample 84
    (
        'больший пироговский улица 17 с1',
        {'entities': [(0, 25, 'addr:street'), (26, 31, 'addr:housenumber')]}
    ),

    # Sample 85
    (
        'улица лужники 24 с9 119048',
        {'entities': [(6, 13, 'addr:street'), (14, 19, 'addr:housenumber'), (20, 26, 'addr:postcode')]}
    ),

    # Sample 86
    (
        '8 с2 трубецкой улица',
        {'entities': [(2, 4, 'addr:housenumber'), (5, 20, 'addr:street')]}
    ),

    # Sample 87
    (
        'леонтьевский переулок 22',
        {'entities': [(0, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 88
    (
        'тверской бульвар 16',
        {'entities': [(0, 16, 'addr:street'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 89
    (
        '26 улица генерал белов',
        {'entities': [(3, 22, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 90
    (
        'тверская улица 125009 7',
        {'entities': [(0, 14, 'addr:street'), (15, 21, 'addr:postcode'), (22, 23, 'addr:housenumber')]}
    ),

    # Sample 91
    (
        'тверская улица 6 с6',
        {'entities': [(0, 14, 'addr:street'), (15, 19, 'addr:housenumber')]}
    ),

    # Sample 92
    (
        '2/14 старый площадь',
        {'entities': [(0, 4, 'addr:housenumber'), (5, 19, 'addr:street')]}
    ),

    # Sample 93
    (
        '4 старый площадь',
        {'entities': [(2, 16, 'addr:street'), (0, 1, 'addr:housenumber')]}
    ),

    # Sample 94
    (
        'старый площадь 8/5',
        {'entities': [(7, 14, 'addr:street'), (15, 18, 'addr:housenumber')]}
    ),

    # Sample 95
    (
        '12 новорязанский улица',
        {'entities': [(3, 22, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 96
    (
        '43 с1 сосинский улица',
        {'entities': [(3, 5, 'addr:housenumber'), (6, 21, 'addr:street')]}
    ),

    # Sample 97
    (
        'марксистский улица 24',
        {'entities': [(0, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 98
    (
        '35б к2 воронцовский улица',
        {'entities': [(0, 6, 'addr:housenumber'), (7, 25, 'addr:street')]}
    ),

    # Sample 99
    (
        'улица щипка 5/3',
        {'entities': [(0, 11, 'addr:street'), (12, 15, 'addr:housenumber')]}
    ),

    # Sample 100
    (
        '11 улица петровка',
        {'entities': [(3, 17, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 101
    (
        'сургут улица больший дмитровка 125009 15',
        {'entities': [(0, 6, 'addr:city'), (7, 30, 'addr:street'), (31, 37, 'addr:postcode'), (38, 40, 'addr:housenumber')]}
    ),

    # Sample 102
    (
        'соликамск улица кузнецкий мост 3 с2',
        {'entities': [(0, 9, 'addr:city'), (10, 30, 'addr:street'), (31, 35, 'addr:housenumber')]}
    ),

    # Sample 103
    (
        'армавир улица кузнецкий мост 19 с1',
        {'entities': [(0, 7, 'addr:city'), (8, 28, 'addr:street'), (29, 34, 'addr:housenumber')]}
    ),

    # Sample 104
    (
        'астрахань армянский переулок 2 101000',
        {'entities': [(0, 9, 'addr:city'), (10, 28, 'addr:street'), (29, 30, 'addr:housenumber'), (31, 37, 'addr:postcode')]}
    ),

    # Sample 105
    (
        'энгельс улица талалихин 33 с1',
        {'entities': [(0, 7, 'addr:city'), (8, 23, 'addr:street'), (24, 29, 'addr:housenumber')]}
    ),

    # Sample 106
    (
        'калуга лубянский проезд 5 с1',
        {'entities': [(0, 6, 'addr:city'), (7, 23, 'addr:street'), (24, 28, 'addr:housenumber')]}
    ),

    # Sample 107
    (
        'грозный улица маросейка 7/8 с1',
        {'entities': [(0, 7, 'addr:city'), (8, 23, 'addr:street'), (24, 30, 'addr:housenumber')]}
    ),

    # Sample 108
    (
        '25 121359 альметьевск улица маршал тимошенко',
        {'entities': [(3, 9, 'addr:postcode'), (10, 21, 'addr:city'), (22, 44, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 109
    (
        'ижевск 6 улица генерал белов',
        {'entities': [(0, 6, 'addr:city'), (9, 28, 'addr:street')]}
    ),

    # Sample 110
    (
        'белгород 4 115563 улица генерал белов',
        {'entities': [(0, 8, 'addr:city'), (9, 10, 'addr:housenumber'), (11, 17, 'addr:postcode'), (18, 37, 'addr:street')]}
    ),

    # Sample 111
    (
        'шахта лесной улица 1/2 125047',
        {'entities': [(6, 18, 'addr:street'), (19, 22, 'addr:housenumber'), (23, 29, 'addr:postcode')]}
    ),

    # Sample 112
    (
        'балаково 9/23 с1 2-я бауманский улица 105005',
        {'entities': [(0, 8, 'addr:city'), (9, 13, 'addr:housenumber'), (17, 37, 'addr:street'), (38, 44, 'addr:postcode')]}
    ),

    # Sample 113
    (
        'магнитогорск 3 2-я бауманский улица',
        {'entities': [(0, 12, 'addr:city'), (15, 35, 'addr:street'), (13, 14, 'addr:housenumber')]}
    ),

    # Sample 114
    (
        'камышин проспект вернадский 101 к1',
        {'entities': [(0, 7, 'addr:city'), (8, 27, 'addr:street'), (28, 34, 'addr:housenumber')]}
    ),

    # Sample 115
    (
        'новошахтинск 2 андреевский набережная',
        {'entities': [(0, 12, 'addr:city'), (15, 37, 'addr:street')]}
    ),

    # Sample 116
    (
        '117519 миасс кировоградский улица 30а',
        {'entities': [(0, 6, 'addr:postcode'), (7, 12, 'addr:city'), (13, 33, 'addr:street'), (34, 37, 'addr:housenumber')]}
    ),

    # Sample 117
    (
        'кирово-чепецк варшавский шоссе 132 к1',
        {'entities': [(0, 13, 'addr:city'), (14, 30, 'addr:street'), (31, 37, 'addr:housenumber')]}
    ),

    # Sample 118
    (
        '117534 королёв кировоградский улица 42б',
        {'entities': [(0, 6, 'addr:postcode'), (7, 14, 'addr:city'), (15, 35, 'addr:street'), (36, 39, 'addr:housenumber')]}
    ),

    # Sample 119
    (
        '107497 тамбов иркутский улица 11 к1',
        {'entities': [(0, 6, 'addr:postcode'), (7, 13, 'addr:city'), (14, 29, 'addr:street'), (30, 35, 'addr:housenumber')]}
    ),

    # Sample 120
    (
        'тобольск улица крылатский холм 45 к2 121614',
        {'entities': [(0, 8, 'addr:city'), (9, 30, 'addr:street'), (31, 36, 'addr:housenumber'), (37, 43, 'addr:postcode')]}
    ),

    # Sample 121
    (
        'кострома 45 к1 121614 улица крылатский холм',
        {'entities': [(0, 8, 'addr:city'), (9, 14, 'addr:housenumber'), (15, 21, 'addr:postcode'), (22, 43, 'addr:street')]}
    ),

    # Sample 122
    (
        'самара волгоградский проспект 45 с1',
        {'entities': [(0, 6, 'addr:city'), (7, 29, 'addr:street'), (30, 35, 'addr:housenumber')]}
    ),

    # Sample 123
    (
        'коломна балаклавский проспект 48 к1',
        {'entities': [(0, 7, 'addr:city'), (8, 29, 'addr:street'), (30, 35, 'addr:housenumber')]}
    ),

    # Sample 124
    (
        'таганрог балаклавский проспект 48 к1',
        {'entities': [(0, 8, 'addr:city'), (9, 30, 'addr:street'), (31, 36, 'addr:housenumber')]}
    ),

    # Sample 125
    (
        'таганрог улица адмирал лазарев 35 к1',
        {'entities': [(0, 8, 'addr:city'), (9, 30, 'addr:street'), (31, 36, 'addr:housenumber')]}
    ),

    # Sample 126
    (
        'грозный большой черкасский переулок 15',
        {'entities': [(0, 7, 'addr:city'), (8, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 127
    (
        'раменский улица ильинка 15 с1',
        {'entities': [(0, 9, 'addr:city'), (10, 23, 'addr:street'), (24, 29, 'addr:housenumber')]}
    ),

    # Sample 128
    (
        'барнаул востряковский проезд 3а 117546',
        {'entities': [(0, 7, 'addr:city'), (8, 28, 'addr:street'), (29, 31, 'addr:housenumber'), (32, 38, 'addr:postcode')]}
    ),

    # Sample 129
    (
        'балаково 5 щукинскай улица',
        {'entities': [(0, 8, 'addr:city'), (9, 10, 'addr:housenumber'), (11, 26, 'addr:street')]}
    ),

    # Sample 130
    (
        'волгодонск 3-я улица ямский поле 9 125040',
        {'entities': [(0, 10, 'addr:city'), (11, 32, 'addr:street'), (33, 34, 'addr:housenumber'), (35, 41, 'addr:postcode')]}
    ),

    # Sample 131
    (
        'великий новгород бумажный проезд 14 с1',
        {'entities': [(0, 16, 'addr:city'), (17, 32, 'addr:street'), (33, 38, 'addr:housenumber')]}
    ),

    # Sample 132
    (
        'владикавказ бумажный проезд 14 с2',
        {'entities': [(0, 11, 'addr:city'), (12, 27, 'addr:street'), (28, 33, 'addr:housenumber')]}
    ),

    # Sample 133
    (
        'тобольск скаковой улица 34 к4',
        {'entities': [(0, 8, 'addr:city'), (9, 23, 'addr:street'), (24, 29, 'addr:housenumber')]}
    ),

    # Sample 134
    (
        'тамбов скаковой улица 34 к3',
        {'entities': [(0, 6, 'addr:city'), (7, 21, 'addr:street'), (22, 27, 'addr:housenumber')]}
    ),

    # Sample 135
    (
        'кисловодск пятницкий улица 1/2 с1',
        {'entities': [(0, 10, 'addr:city'), (11, 26, 'addr:street'), (27, 33, 'addr:housenumber')]}
    ),

    # Sample 136
    (
        'коломна вл112 проспект мир',
        {'entities': [(0, 7, 'addr:city'), (8, 13, 'addr:housenumber'), (14, 26, 'addr:street')]}
    ),

    # Sample 137
    (
        'щёлково угличский улица 6а',
        {'entities': [(0, 7, 'addr:city'), (8, 23, 'addr:street'), (24, 26, 'addr:housenumber')]}
    ),

    # Sample 138
    (
        'нижневартовск волоколамский шоссе 77',
        {'entities': [(0, 13, 'addr:city'), (14, 33, 'addr:street'), (34, 36, 'addr:housenumber')]}
    ),

    # Sample 139
    (
        'рыбинск 103073',
        {'entities': [(0, 7, 'addr:city'), (8, 14, 'addr:postcode')]}
    ),

    # Sample 140
    (
        'керчь 103073',
        {'entities': [(0, 5, 'addr:city'), (6, 12, 'addr:postcode')]}
    ),

    # Sample 141
    (
        'энгельс 103073',
        {'entities': [(0, 7, 'addr:city'), (8, 14, 'addr:postcode')]}
    ),

    # Sample 142
    (
        'соликамск 103073',
        {'entities': [(0, 9, 'addr:city'), (10, 16, 'addr:postcode')]}
    ),

    # Sample 143
    (
        'салават 103073',
        {'entities': [(0, 7, 'addr:city'), (8, 14, 'addr:postcode')]}
    ),

    # Sample 144
    (
        'ковровый 103073',
        {'entities': [(9, 15, 'addr:postcode')]}
    ),

    # Sample 145
    (
        'брянск 103073',
        {'entities': [(0, 6, 'addr:city'), (7, 13, 'addr:postcode')]}
    ),

    # Sample 146
    (
        'великий новгород 29',
        {'entities': [(0, 16, 'addr:city'), (17, 19, 'addr:housenumber')]}
    ),

    # Sample 147
    (
        'подольск 2-я брестский улица 125047 6',
        {'entities': [(0, 8, 'addr:city'), (13, 28, 'addr:street'), (29, 35, 'addr:postcode'), (36, 37, 'addr:housenumber')]}
    ),

    # Sample 148
    (
        'ижевск 2-я брестский улица 8',
        {'entities': [(0, 6, 'addr:city'), (7, 26, 'addr:street'), (27, 28, 'addr:housenumber')]}
    ),

    # Sample 149
    (
        'елец мичуринский проспект 17 к2',
        {'entities': [(0, 4, 'addr:city'), (5, 25, 'addr:street'), (26, 31, 'addr:housenumber')]}
    ),

    # Sample 150
    (
        'хабаровск бумажный проезд 2/2 с6 125040',
        {'entities': [(0, 9, 'addr:city'), (10, 25, 'addr:street'), (26, 32, 'addr:housenumber'), (33, 39, 'addr:postcode')]}
    ),

    # Sample 151
    (
        'шахта 36/40 3-я тверская-ямский улица',
        {'entities': [(6, 11, 'addr:housenumber'), (12, 31, 'addr:street'), (32, 37, 'addr:street')]}
    ),

    # Sample 152
    (
        'курган 1-я тверская-ямский улица 26',
        {'entities': [(0, 6, 'addr:city'), (7, 32, 'addr:street'), (33, 35, 'addr:housenumber')]}
    ),

    # Sample 153
    (
        'таганрог лесной улица 5 сб 125047',
        {'entities': [(0, 8, 'addr:city'), (9, 21, 'addr:street'), (22, 23, 'addr:housenumber'), (27, 33, 'addr:postcode')]}
    ),

    # Sample 154
    (
        '125047 тамбов лесной улица 4 с1',
        {'entities': [(0, 6, 'addr:postcode'), (7, 13, 'addr:city'), (14, 26, 'addr:street'), (27, 31, 'addr:housenumber')]}
    ),

    # Sample 155
    (
        '4 125047 энгельс улица бутырский вал',
        {'entities': [(2, 8, 'addr:postcode'), (9, 16, 'addr:city'), (17, 36, 'addr:street')]}
    ),

    # Sample 156
    (
        'благовещенск улица бутырский вал 8/3 с1',
        {'entities': [(0, 12, 'addr:city'), (13, 32, 'addr:street'), (33, 39, 'addr:housenumber')]}
    ),

    # Sample 157
    (
        'камышин улица земляной вал 105064 29',
        {'entities': [(0, 7, 'addr:city'), (8, 26, 'addr:street'), (27, 33, 'addr:postcode'), (34, 36, 'addr:housenumber')]}
    ),

    # Sample 158
    (
        '125047 омск 46 2-я брестский улица',
        {'entities': [(0, 6, 'addr:postcode'), (7, 11, 'addr:city'), (12, 14, 'addr:housenumber'), (19, 34, 'addr:street')]}
    ),

    # Sample 159
    (
        '125047 бийск 7 улица бутырский вал',
        {'entities': [(0, 6, 'addr:postcode'), (7, 12, 'addr:city'), (15, 34, 'addr:street'), (13, 14, 'addr:housenumber')]}
    ),

    # Sample 160
    (
        '125047 красногорск 1-я тверская-ямский улица 36 с1',
        {'entities': [(0, 6, 'addr:postcode'), (7, 18, 'addr:city'), (19, 44, 'addr:street'), (45, 50, 'addr:housenumber')]}
    ),

    # Sample 161
    (
        'камышин 1-я тверская-ямский улица 34',
        {'entities': [(0, 7, 'addr:city'), (8, 33, 'addr:street'), (34, 36, 'addr:housenumber')]}
    ),

    # Sample 162
    (
        'коломна 1-я тверская-ямский улица 30',
        {'entities': [(0, 7, 'addr:city'), (8, 33, 'addr:street'), (34, 36, 'addr:housenumber')]}
    ),

    # Sample 163
    (
        'керчь улица александр невский 1',
        {'entities': [(0, 5, 'addr:city'), (6, 29, 'addr:street'), (30, 31, 'addr:housenumber')]}
    ),

    # Sample 164
    (
        '32 125047 пятигорск 1-я тверская-ямский улица',
        {'entities': [(3, 9, 'addr:postcode'), (10, 19, 'addr:city'), (20, 45, 'addr:street'), (0, 2, 'addr:housenumber')]}
    ),

    # Sample 165
    (
        'южный-сахалинск 4-й лесной переулок 6',
        {'entities': [(0, 15, 'addr:city'), (16, 35, 'addr:street'), (36, 37, 'addr:housenumber')]}
    ),

    # Sample 166
    (
        'черкесск улица бутырский вал 18',
        {'entities': [(0, 8, 'addr:city'), (9, 28, 'addr:street'), (29, 31, 'addr:housenumber')]}
    ),

    # Sample 167
    (
        'воронеж улица бутырский вал 7 к2',
        {'entities': [(0, 7, 'addr:city'), (8, 27, 'addr:street'), (28, 32, 'addr:housenumber')]}
    ),

    # Sample 168
    (
        'самара улица бутырский вал 22',
        {'entities': [(0, 6, 'addr:city'), (7, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 169
    (
        'брянск улица бутырский вал 24',
        {'entities': [(0, 6, 'addr:city'), (7, 26, 'addr:street'), (27, 29, 'addr:housenumber')]}
    ),

    # Sample 170
    (
        'елец 2-й лесной переулок 11 с1',
        {'entities': [(0, 4, 'addr:city'), (5, 24, 'addr:street'), (25, 30, 'addr:housenumber')]}
    ),

    # Sample 171
    (
        'камышин улица бутырский вал 20',
        {'entities': [(0, 7, 'addr:city'), (8, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 172
    (
        'пятигорск 4-я тверская-ямский улица 125047 12 с2',
        {'entities': [(0, 9, 'addr:city'), (10, 35, 'addr:street'), (36, 42, 'addr:postcode'), (43, 48, 'addr:housenumber')]}
    ),

    # Sample 173
    (
        '125047 балаково 5 с19 улица фадеев',
        {'entities': [(0, 6, 'addr:postcode'), (7, 15, 'addr:city'), (16, 21, 'addr:housenumber'), (22, 27, 'addr:street'), (28, 34, 'addr:street')]}
    ),

    # Sample 174
    (
        '9 125047 химки улица фадеев',
        {'entities': [(2, 8, 'addr:postcode'), (9, 14, 'addr:city'), (15, 27, 'addr:street')]}
    ),

    # Sample 175
    (
        'владикавказ улица фадеев 5 с6',
        {'entities': [(0, 11, 'addr:city'), (12, 24, 'addr:street'), (25, 29, 'addr:housenumber')]}
    ),

    # Sample 176
    (
        'ярославль 4-я тверская-ямский улица 125047 16 к3',
        {'entities': [(0, 9, 'addr:city'), (10, 35, 'addr:street'), (36, 42, 'addr:postcode'), (43, 48, 'addr:housenumber')]}
    ),

    # Sample 177
    (
        'киров 12 с1 125047 4-я тверская-ямский улица',
        {'entities': [(0, 5, 'addr:city'), (9, 11, 'addr:housenumber'), (12, 18, 'addr:postcode'), (19, 44, 'addr:street')]}
    ),

    # Sample 178
    (
        '125047 рязань 7 с3 улица фадеев',
        {'entities': [(0, 6, 'addr:postcode'), (7, 13, 'addr:city'), (14, 18, 'addr:housenumber'), (19, 31, 'addr:street')]}
    ),

    # Sample 179
    (
        'обнинск 4-я тверская-ямский улица 16 к1 125047',
        {'entities': [(0, 7, 'addr:city'), (8, 33, 'addr:street'), (34, 39, 'addr:housenumber'), (40, 46, 'addr:postcode')]}
    ),

    # Sample 180
    (
        '125047 тобольск улица чаяновый 10 с1',
        {'entities': [(0, 6, 'addr:postcode'), (7, 15, 'addr:city'), (16, 30, 'addr:street'), (31, 36, 'addr:housenumber')]}
    ),

    # Sample 181
    (
        'курган 5 125047 улица фадеев',
        {'entities': [(0, 6, 'addr:city'), (9, 15, 'addr:postcode'), (16, 28, 'addr:street'), (7, 8, 'addr:housenumber')]}
    ),

    # Sample 182
    (
        '125047 мур улица фадеев 5 с1',
        {'entities': [(0, 6, 'addr:postcode'), (11, 23, 'addr:street'), (24, 28, 'addr:housenumber')]}
    ),

    # Sample 183
    (
        'обнинск 10 с2 улица чаяновый 125047',
        {'entities': [(0, 7, 'addr:city'), (11, 13, 'addr:housenumber'), (14, 28, 'addr:street'), (29, 35, 'addr:postcode')]}
    ),

    # Sample 184
    (
        'каменск-уральский улица фадеев 7 с2 125047',
        {'entities': [(0, 17, 'addr:city'), (18, 30, 'addr:street'), (31, 35, 'addr:housenumber'), (36, 42, 'addr:postcode')]}
    ),

    # Sample 185
    (
        'черкесск улица фадеев 13/5 с15',
        {'entities': [(0, 8, 'addr:city'), (9, 21, 'addr:street'), (22, 30, 'addr:housenumber')]}
    ),

    # Sample 186
    (
        'улан-удэ 4-я тверская-ямский улица 125047 8/9',
        {'entities': [(0, 8, 'addr:city'), (9, 34, 'addr:street'), (35, 41, 'addr:postcode'), (42, 45, 'addr:housenumber')]}
    ),

    # Sample 187
    (
        'сочи улица фадеев 125047 5 с1',
        {'entities': [(0, 4, 'addr:city'), (5, 17, 'addr:street'), (18, 24, 'addr:postcode'), (25, 29, 'addr:housenumber')]}
    ),

    # Sample 188
    (
        '125047 владикавказ улица чаяновый 12',
        {'entities': [(0, 6, 'addr:postcode'), (7, 18, 'addr:city'), (19, 33, 'addr:street'), (34, 36, 'addr:housenumber')]}
    ),

    # Sample 189
    (
        'волгодонск улица фадеев 5а с1',
        {'entities': [(0, 10, 'addr:city'), (11, 23, 'addr:street'), (24, 29, 'addr:housenumber')]}
    ),

    # Sample 190
    (
        'таганрог 7 с1 улица фадеев 125047',
        {'entities': [(0, 8, 'addr:city'), (14, 26, 'addr:street'), (27, 33, 'addr:postcode')]}
    ),

    # Sample 191
    (
        'иваново 4-я тверская-ямский улица 125047 16',
        {'entities': [(0, 7, 'addr:city'), (8, 33, 'addr:street'), (34, 40, 'addr:postcode'), (41, 43, 'addr:housenumber')]}
    ),

    # Sample 192
    (
        'южный-сахалинск 4-я тверская-ямский улица 22',
        {'entities': [(0, 15, 'addr:city'), (20, 41, 'addr:street'), (42, 44, 'addr:housenumber')]}
    ),

    # Sample 193
    (
        'элиста 4-я тверская-ямский улица 10 125047',
        {'entities': [(0, 6, 'addr:city'), (7, 32, 'addr:street'), (33, 35, 'addr:housenumber'), (36, 42, 'addr:postcode')]}
    ),

    # Sample 194
    (
        '125047 тула 4-я тверская-ямский улица 22 к2',
        {'entities': [(0, 6, 'addr:postcode'), (7, 11, 'addr:city'), (12, 37, 'addr:street'), (38, 43, 'addr:housenumber')]}
    ),

    # Sample 195
    (
        'первоуральск 16 к2 4-я тверская-ямский улица 125047',
        {'entities': [(0, 12, 'addr:city'), (13, 18, 'addr:housenumber'), (19, 44, 'addr:street'), (45, 51, 'addr:postcode')]}
    ),

    # Sample 196
    (
        '125047 салават 1-й тверской-ямский переулок 11',
        {'entities': [(0, 6, 'addr:postcode'), (7, 14, 'addr:city'), (15, 43, 'addr:street'), (44, 46, 'addr:housenumber')]}
    ),

    # Sample 197
    (
        'ковровый 14 с3 125047 4-я тверская-ямский улица',
        {'entities': [(9, 14, 'addr:housenumber'), (15, 21, 'addr:postcode'), (22, 47, 'addr:street')]}
    ),

    # Sample 198
    (
        'шахта 4-я тверская-ямский улица 125047 20 с1',
        {'entities': [(6, 31, 'addr:street'), (32, 38, 'addr:postcode'), (39, 44, 'addr:housenumber')]}
    ),

    # Sample 199
    (
        'первоуральск 4-я тверская-ямский улица 24 125047',
        {'entities': [(0, 12, 'addr:city'), (13, 38, 'addr:street'), (39, 41, 'addr:housenumber'), (42, 48, 'addr:postcode')]}
    ),

    # Sample 200
    (
        'южный-сахалинск миусский площадь 125047 4',
        {'entities': [(0, 15, 'addr:city'), (25, 32, 'addr:street'), (33, 39, 'addr:postcode'), (40, 41, 'addr:housenumber')]}
    ),

]
