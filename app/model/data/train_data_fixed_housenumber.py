"""
Training Data for Address NER
Generated: 2025-11-16 05:36:27.844007
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
        {'entities': [(0, 17, 'addr:street'), (18, 24, 'addr:postcode'), (25, 28, 'addr:housenumber'), (29, 31, 'addr:buildingnumber')]}
    ),

    # Sample 3
    (
        'нежинский улица 119501 5 с1',
        {'entities': [(10, 15, 'addr:street'), (16, 22, 'addr:postcode'), (23, 24, 'addr:housenumber'), (25, 27, 'addr:buildingnumber')]}
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
        {'entities': [(0, 2, 'addr:housenumber'), (3, 20, 'addr:street'), (21, 24, 'addr:city')]}
    ),

    # Sample 8
    (
        'волоколамский шоссе 73',
        {'entities': [(0, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 9
    (
        'улица маршал катуков 21 к2',
        {'entities': [(0, 20, 'addr:street'), (21, 23, 'addr:housenumber'), (24, 26, 'addr:corpusnumber')]}
    ),

    # Sample 10
    (
        'строгинский бульвар 123458 14 к5 казань',
        {'entities': [(0, 19, 'addr:street'), (20, 26, 'addr:postcode'), (27, 29, 'addr:housenumber'), (30, 32, 'addr:corpusnumber'), (33, 39, 'addr:city')]}
    ),

    # Sample 11
    (
        'бескудниковский бульвар 59а с2а улан уд',
        {'entities': [(0, 23, 'addr:street'), (24, 27, 'addr:housenumber'), (28, 31, 'addr:buildingnumber')]}
    ),

    # Sample 12
    (
        'дмитровский шоссе 60а 127474',
        {'entities': [(0, 17, 'addr:street'), (18, 21, 'addr:housenumber'), (22, 28, 'addr:postcode')]}
    ),

    # Sample 13
    (
        '17 к2 улица кулаковый',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 21, 'addr:street')]}
    ),

    # Sample 14
    (
        'севастопольский проспект 24а сколково',
        {'entities': [(0, 24, 'addr:street'), (25, 28, 'addr:housenumber'), (29, 37, 'addr:city')]}
    ),

    # Sample 15
    (
        '87 к1 улица удальцов',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 20, 'addr:street')]}
    ),

    # Sample 16
    (
        '15 шенкурский проезд',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 20, 'addr:street')]}
    ),

    # Sample 17
    (
        'ленинградский проспект 37 к1 москва',
        {'entities': [(0, 22, 'addr:street'), (23, 25, 'addr:housenumber'), (26, 28, 'addr:corpusnumber'), (29, 35, 'addr:city')]}
    ),

    # Sample 18
    (
        '127253 псковский улица 12 к3',
        {'entities': [(0, 6, 'addr:postcode'), (7, 22, 'addr:street'), (23, 25, 'addr:housenumber'), (26, 28, 'addr:corpusnumber')]}
    ),

    # Sample 19
    (
        'улица плещеев 127560 26а',
        {'entities': [(0, 13, 'addr:street'), (14, 20, 'addr:postcode'), (21, 24, 'addr:housenumber')]}
    ),

    # Sample 20
    (
        '4а 127560 улица конёнкова брянск',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 9, 'addr:postcode'), (10, 25, 'addr:street'), (26, 32, 'addr:city')]}
    ),

    # Sample 21
    (
        '25а улица лесков',
        {'entities': [(0, 3, 'addr:housenumber'), (4, 16, 'addr:street')]}
    ),

    # Sample 22
    (
        'шипиловский улица 17 к1',
        {'entities': [(0, 17, 'addr:street'), (18, 20, 'addr:housenumber'), (21, 23, 'addr:corpusnumber')]}
    ),

    # Sample 23
    (
        'роман переулок 5 липецк',
        {'entities': [(0, 14, 'addr:street'), (15, 16, 'addr:housenumber'), (17, 23, 'addr:city')]}
    ),

    # Sample 24
    (
        '7/5 с3 улица больший дмитровка',
        {'entities': [(0, 3, 'addr:housenumber'), (4, 6, 'addr:buildingnumber'), (7, 30, 'addr:street')]}
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
        {'entities': [(0, 2, 'addr:housenumber'), (3, 18, 'addr:street')]}
    ),

    # Sample 28
    (
        'мерзляковский переулок 15',
        {'entities': [(0, 22, 'addr:street'), (23, 25, 'addr:housenumber')]}
    ),

    # Sample 29
    (
        'улица твардовский 2 к2',
        {'entities': [(0, 17, 'addr:street'), (18, 19, 'addr:housenumber'), (20, 22, 'addr:corpusnumber')]}
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
        {'entities': [(0, 3, 'addr:housenumber'), (4, 19, 'addr:street')]}
    ),

    # Sample 35
    (
        'улица островитянов 1',
        {'entities': [(0, 18, 'addr:street'), (19, 20, 'addr:housenumber')]}
    ),

    # Sample 36
    (
        '101 к6 проспект вернадский 119526',
        {'entities': [(0, 3, 'addr:housenumber'), (4, 6, 'addr:corpusnumber'), (7, 26, 'addr:street'), (27, 33, 'addr:postcode')]}
    ),

    # Sample 37
    (
        '2 к2 улица кулаковый',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 4, 'addr:corpusnumber'), (5, 20, 'addr:street')]}
    ),

    # Sample 38
    (
        'улица кулаковый 3 к1',
        {'entities': [(0, 15, 'addr:street'), (16, 17, 'addr:housenumber'), (18, 20, 'addr:corpusnumber')]}
    ),

    # Sample 39
    (
        '58 кантемировский улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 23, 'addr:street')]}
    ),

    # Sample 40
    (
        '7 к4 клязьминский улица',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 4, 'addr:corpusnumber'), (5, 23, 'addr:street')]}
    ),

    # Sample 41
    (
        'профсоюзный улица 61',
        {'entities': [(0, 17, 'addr:street'), (18, 20, 'addr:housenumber')]}
    ),

    # Sample 42
    (
        '61 к1 профсоюзный улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 23, 'addr:street')]}
    ),

    # Sample 43
    (
        '35 мосфильмовский улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 23, 'addr:street')]}
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
        {'entities': [(0, 2, 'addr:housenumber'), (3, 20, 'addr:street')]}
    ),

    # Sample 48
    (
        '16 больший бронный улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 24, 'addr:street')]}
    ),

    # Sample 49
    (
        '115569 улица маршал захаров 8 к1',
        {'entities': [(0, 6, 'addr:postcode'), (7, 27, 'addr:street'), (28, 29, 'addr:housenumber'), (30, 32, 'addr:corpusnumber')]}
    ),

    # Sample 50
    (
        'улица санников 3 к3 127562',
        {'entities': [(0, 14, 'addr:street'), (15, 16, 'addr:housenumber'), (17, 19, 'addr:corpusnumber'), (20, 26, 'addr:postcode')]}
    ),

    # Sample 51
    (
        'мохов улица 125009 15/1 с1',
        {'entities': [(6, 11, 'addr:street'), (12, 18, 'addr:postcode'), (19, 23, 'addr:housenumber'), (24, 26, 'addr:buildingnumber')]}
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
        {'entities': [(0, 6, 'addr:postcode'), (7, 11, 'addr:corpusnumber')]}
    ),

    # Sample 55
    (
        'к810 117648',
        {'entities': [(0, 4, 'addr:corpusnumber'), (5, 11, 'addr:postcode')]}
    ),

    # Sample 56
    (
        'проспект вернадский 78 с2',
        {'entities': [(0, 19, 'addr:street'), (20, 22, 'addr:housenumber'), (23, 25, 'addr:buildingnumber')]}
    ),

    # Sample 57
    (
        'проспект вернадский 78 с3',
        {'entities': [(0, 19, 'addr:street'), (20, 22, 'addr:housenumber'), (23, 25, 'addr:buildingnumber')]}
    ),

    # Sample 58
    (
        '78 с6 проспект вернадский',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:buildingnumber'), (6, 25, 'addr:street')]}
    ),

    # Sample 59
    (
        '13 улица академик глушко',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 24, 'addr:street')]}
    ),

    # Sample 60
    (
        'феодосийский улица 1 к1 117628',
        {'entities': [(13, 18, 'addr:street'), (19, 20, 'addr:housenumber'), (21, 23, 'addr:corpusnumber'), (24, 30, 'addr:postcode')]}
    ),

    # Sample 61
    (
        '49 ярославский шоссе',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 20, 'addr:street')]}
    ),

    # Sample 62
    (
        '94 алтуфьевский шоссе',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 21, 'addr:street')]}
    ),

    # Sample 63
    (
        '28',
        {'entities': [(0, 2, 'addr:housenumber')]}
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
        {'entities': [(0, 6, 'addr:postcode'), (7, 29, 'addr:street'), (30, 33, 'addr:housenumber'), (34, 36, 'addr:corpusnumber')]}
    ),

    # Sample 67
    (
        '9 с9 улица образец',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 4, 'addr:buildingnumber'), (5, 18, 'addr:street')]}
    ),

    # Sample 68
    (
        '2 театральный площадь',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 21, 'addr:street')]}
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
        {'entities': [(0, 17, 'addr:street'), (18, 24, 'addr:postcode'), (25, 27, 'addr:housenumber'), (28, 30, 'addr:corpusnumber')]}
    ),

    # Sample 72
    (
        '35 к2 улица юный ленинец',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 24, 'addr:street')]}
    ),

    # Sample 73
    (
        'площадь академик курчатов 1 с20а 123098',
        {'entities': [(0, 25, 'addr:street'), (26, 27, 'addr:housenumber'), (28, 32, 'addr:buildingnumber'), (33, 39, 'addr:postcode')]}
    ),

    # Sample 74
    (
        'улица миклухо-маклай 21а',
        {'entities': [(0, 20, 'addr:street'), (21, 24, 'addr:housenumber')]}
    ),

    # Sample 75
    (
        '12 к1 улица академик волгин',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 27, 'addr:street')]}
    ),

    # Sample 76
    (
        'улица академик волгин 12',
        {'entities': [(0, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 77
    (
        '100 проспект вернадский',
        {'entities': [(0, 3, 'addr:housenumber'), (4, 23, 'addr:street')]}
    ),

    # Sample 78
    (
        '76 проспект вернадский',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 22, 'addr:street')]}
    ),

    # Sample 79
    (
        'варшавский шоссе 170г',
        {'entities': [(0, 16, 'addr:street'), (17, 21, 'addr:housenumber')]}
    ),

    # Sample 80
    (
        '117405 156б варшавский шоссе',
        {'entities': [(0, 6, 'addr:postcode'), (7, 11, 'addr:housenumber'), (12, 28, 'addr:street')]}
    ),

    # Sample 81
    (
        '110 с62 дмитровский шоссе',
        {'entities': [(0, 3, 'addr:housenumber'), (4, 7, 'addr:buildingnumber'), (8, 25, 'addr:street')]}
    ),

    # Sample 82
    (
        'шоссейный улица 4д',
        {'entities': [(0, 15, 'addr:street'), (16, 18, 'addr:housenumber')]}
    ),

    # Sample 83
    (
        '105568 1 к1 улица чечулина',
        {'entities': [(0, 6, 'addr:postcode'), (7, 8, 'addr:housenumber'), (9, 11, 'addr:corpusnumber'), (12, 26, 'addr:street')]}
    ),

    # Sample 84
    (
        'больший пироговский улица 17 с1',
        {'entities': [(8, 25, 'addr:street'), (26, 28, 'addr:housenumber'), (29, 31, 'addr:buildingnumber')]}
    ),

    # Sample 85
    (
        'улица лужники 24 с9 119048',
        {'entities': [(0, 13, 'addr:street'), (14, 16, 'addr:housenumber'), (17, 19, 'addr:buildingnumber'), (20, 26, 'addr:postcode')]}
    ),

    # Sample 86
    (
        '8 с2 трубецкой улица',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 4, 'addr:buildingnumber'), (5, 20, 'addr:street')]}
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
        {'entities': [(0, 2, 'addr:housenumber'), (3, 22, 'addr:street')]}
    ),

    # Sample 90
    (
        'тверская улица 125009 7',
        {'entities': [(0, 14, 'addr:street'), (15, 21, 'addr:postcode'), (22, 23, 'addr:housenumber')]}
    ),

    # Sample 91
    (
        'тверская улица 6 с6',
        {'entities': [(0, 14, 'addr:street'), (15, 16, 'addr:housenumber'), (17, 19, 'addr:buildingnumber')]}
    ),

    # Sample 92
    (
        '2/14 старый площадь',
        {'entities': [(0, 4, 'addr:housenumber'), (5, 19, 'addr:street')]}
    ),

    # Sample 93
    (
        '4 старый площадь',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 16, 'addr:street')]}
    ),

    # Sample 94
    (
        'старый площадь 8/5',
        {'entities': [(7, 14, 'addr:street'), (15, 18, 'addr:housenumber')]}
    ),

    # Sample 95
    (
        '12 новорязанский улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 22, 'addr:street')]}
    ),

    # Sample 96
    (
        '43 с1 сосинский улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:buildingnumber'), (6, 21, 'addr:street')]}
    ),

    # Sample 97
    (
        'марксистский улица 24',
        {'entities': [(0, 18, 'addr:street'), (19, 21, 'addr:housenumber')]}
    ),

    # Sample 98
    (
        '35б к2 воронцовский улица',
        {'entities': [(0, 3, 'addr:housenumber'), (4, 6, 'addr:corpusnumber'), (7, 25, 'addr:street')]}
    ),

    # Sample 99
    (
        'улица щипка 5/3',
        {'entities': [(0, 11, 'addr:street'), (12, 15, 'addr:housenumber')]}
    ),

    # Sample 100
    (
        '11 улица петровка',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 17, 'addr:street')]}
    ),

    # Sample 101
    (
        'улица больший дмитровка 125009 15',
        {'entities': [(6, 23, 'addr:street'), (24, 30, 'addr:postcode'), (31, 33, 'addr:housenumber')]}
    ),

    # Sample 102
    (
        '3 с2 улица кузнецкий мост',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 4, 'addr:buildingnumber'), (5, 25, 'addr:street')]}
    ),

    # Sample 103
    (
        'улица кузнецкий мост 19 с1',
        {'entities': [(0, 20, 'addr:street'), (21, 23, 'addr:housenumber'), (24, 26, 'addr:buildingnumber')]}
    ),

    # Sample 104
    (
        'армянский переулок 2 101000',
        {'entities': [(0, 18, 'addr:street'), (19, 20, 'addr:housenumber'), (21, 27, 'addr:postcode')]}
    ),

    # Sample 105
    (
        '33 с1 улица талалихин',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:buildingnumber'), (6, 21, 'addr:street')]}
    ),

    # Sample 106
    (
        'лубянский проезд 5 с1',
        {'entities': [(0, 16, 'addr:street'), (17, 18, 'addr:housenumber'), (19, 21, 'addr:buildingnumber')]}
    ),

    # Sample 107
    (
        'улица маросейка 7/8 с1',
        {'entities': [(0, 15, 'addr:street'), (16, 19, 'addr:housenumber'), (20, 22, 'addr:buildingnumber')]}
    ),

    # Sample 108
    (
        '25 121359 улица маршал тимошенко',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 9, 'addr:postcode'), (10, 32, 'addr:street')]}
    ),

    # Sample 109
    (
        '6 улица генерал белов',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 21, 'addr:street')]}
    ),

    # Sample 110
    (
        '4 115563 улица генерал белов',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 8, 'addr:postcode'), (9, 28, 'addr:street')]}
    ),

    # Sample 111
    (
        'лесной улица 1/2 125047',
        {'entities': [(0, 12, 'addr:street'), (13, 16, 'addr:housenumber'), (17, 23, 'addr:postcode')]}
    ),

    # Sample 112
    (
        '9/23 с1 2-я бауманский улица 105005',
        {'entities': [(0, 4, 'addr:housenumber'), (5, 7, 'addr:buildingnumber'), (8, 28, 'addr:street'), (29, 35, 'addr:postcode')]}
    ),

    # Sample 113
    (
        '3 2-я бауманский улица',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 22, 'addr:street')]}
    ),

    # Sample 114
    (
        'проспект вернадский 101 к1',
        {'entities': [(0, 19, 'addr:street'), (20, 23, 'addr:housenumber'), (24, 26, 'addr:corpusnumber')]}
    ),

    # Sample 115
    (
        '2 андреевский набережная',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 24, 'addr:street')]}
    ),

    # Sample 116
    (
        '117519 кировоградский улица 30а',
        {'entities': [(0, 6, 'addr:postcode'), (7, 27, 'addr:street'), (28, 31, 'addr:housenumber')]}
    ),

    # Sample 117
    (
        '132 к1 варшавский шоссе',
        {'entities': [(0, 3, 'addr:housenumber'), (4, 6, 'addr:corpusnumber'), (7, 23, 'addr:street')]}
    ),

    # Sample 118
    (
        '117534 кировоградский улица 42б',
        {'entities': [(0, 6, 'addr:postcode'), (7, 27, 'addr:street'), (28, 31, 'addr:housenumber')]}
    ),

    # Sample 119
    (
        '107497 иркутский улица 11 к1',
        {'entities': [(0, 6, 'addr:postcode'), (7, 22, 'addr:street'), (23, 25, 'addr:housenumber'), (26, 28, 'addr:corpusnumber')]}
    ),

    # Sample 120
    (
        'улица крылатский холм 45 к2 121614',
        {'entities': [(0, 21, 'addr:street'), (22, 24, 'addr:housenumber'), (25, 27, 'addr:corpusnumber'), (28, 34, 'addr:postcode')]}
    ),

    # Sample 121
    (
        '45 к1 121614 улица крылатский холм',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 12, 'addr:postcode'), (13, 34, 'addr:street')]}
    ),

    # Sample 122
    (
        '45 с1 волгоградский проспект',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:buildingnumber'), (6, 28, 'addr:street')]}
    ),

    # Sample 123
    (
        'балаклавский проспект 48 к1',
        {'entities': [(0, 21, 'addr:street'), (22, 24, 'addr:housenumber'), (25, 27, 'addr:corpusnumber')]}
    ),

    # Sample 124
    (
        '48 к1 балаклавский проспект',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 27, 'addr:street')]}
    ),

    # Sample 125
    (
        'улица адмирал лазарев 35 к1',
        {'entities': [(0, 21, 'addr:street'), (22, 24, 'addr:housenumber'), (25, 27, 'addr:corpusnumber')]}
    ),

    # Sample 126
    (
        'большой черкасский переулок 15',
        {'entities': [(0, 27, 'addr:street'), (28, 30, 'addr:housenumber')]}
    ),

    # Sample 127
    (
        '15 с1 улица ильинка',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:buildingnumber'), (6, 19, 'addr:street')]}
    ),

    # Sample 128
    (
        '3а 117546 востряковский проезд',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 9, 'addr:postcode'), (10, 30, 'addr:street')]}
    ),

    # Sample 129
    (
        '5 щукинскай улица',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 17, 'addr:street')]}
    ),

    # Sample 130
    (
        '3-я улица ямский поле 9 125040',
        {'entities': [(4, 21, 'addr:street'), (22, 23, 'addr:housenumber'), (24, 30, 'addr:postcode')]}
    ),

    # Sample 131
    (
        '14 с1 бумажный проезд',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:buildingnumber'), (6, 21, 'addr:street')]}
    ),

    # Sample 132
    (
        'бумажный проезд 14 с2',
        {'entities': [(0, 15, 'addr:street'), (16, 18, 'addr:housenumber'), (19, 21, 'addr:buildingnumber')]}
    ),

    # Sample 133
    (
        '34 к4 скаковой улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 20, 'addr:street')]}
    ),

    # Sample 134
    (
        '34 к3 скаковой улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 20, 'addr:street')]}
    ),

    # Sample 135
    (
        'пятницкий улица 1/2 с1',
        {'entities': [(0, 15, 'addr:street'), (16, 19, 'addr:housenumber'), (20, 22, 'addr:buildingnumber')]}
    ),

    # Sample 136
    (
        'вл112 проспект мир',
        {'entities': [(0, 5, 'addr:housenumber'), (6, 18, 'addr:street')]}
    ),

    # Sample 137
    (
        '6а угличский улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 18, 'addr:street')]}
    ),

    # Sample 138
    (
        'волоколамский шоссе 77',
        {'entities': [(0, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 139
    (
        '103073',
        {'entities': [(0, 6, 'addr:postcode')]}
    ),

    # Sample 140
    (
        '103073',
        {'entities': [(0, 6, 'addr:postcode')]}
    ),

    # Sample 141
    (
        '103073',
        {'entities': [(0, 6, 'addr:postcode')]}
    ),

    # Sample 142
    (
        '103073',
        {'entities': [(0, 6, 'addr:postcode')]}
    ),

    # Sample 143
    (
        '103073',
        {'entities': [(0, 6, 'addr:postcode')]}
    ),

    # Sample 144
    (
        '103073',
        {'entities': [(0, 6, 'addr:postcode')]}
    ),

    # Sample 145
    (
        '103073',
        {'entities': [(0, 6, 'addr:postcode')]}
    ),

    # Sample 146
    (
        '29',
        {'entities': [(0, 2, 'addr:housenumber')]}
    ),

    # Sample 147
    (
        '2-я брестский улица 125047 6',
        {'entities': [(0, 19, 'addr:street'), (20, 26, 'addr:postcode'), (27, 28, 'addr:housenumber')]}
    ),

    # Sample 148
    (
        '2-я брестский улица 8',
        {'entities': [(0, 19, 'addr:street'), (20, 21, 'addr:housenumber')]}
    ),

    # Sample 149
    (
        '17 к2 мичуринский проспект',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 26, 'addr:street')]}
    ),

    # Sample 150
    (
        '2/2 с6 125040 бумажный проезд',
        {'entities': [(0, 3, 'addr:housenumber'), (4, 6, 'addr:buildingnumber'), (7, 13, 'addr:postcode'), (14, 29, 'addr:street')]}
    ),

    # Sample 151
    (
        '36/40 3-я тверская-ямский улица',
        {'entities': [(0, 5, 'addr:housenumber'), (6, 31, 'addr:street')]}
    ),

    # Sample 152
    (
        '26 1-я тверская-ямский улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 28, 'addr:street')]}
    ),

    # Sample 153
    (
        'лесной улица 5 сб 125047',
        {'entities': [(0, 12, 'addr:street'), (13, 14, 'addr:housenumber'), (15, 17, 'addr:buildingnumber'), (18, 24, 'addr:postcode')]}
    ),

    # Sample 154
    (
        '125047 лесной улица 4 с1',
        {'entities': [(0, 6, 'addr:postcode'), (7, 19, 'addr:street'), (20, 21, 'addr:housenumber'), (22, 24, 'addr:buildingnumber')]}
    ),

    # Sample 155
    (
        '4 125047 улица бутырский вал',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 8, 'addr:postcode'), (9, 28, 'addr:street')]}
    ),

    # Sample 156
    (
        '8/3 с1 улица бутырский вал',
        {'entities': [(0, 3, 'addr:housenumber'), (4, 6, 'addr:buildingnumber'), (7, 26, 'addr:street')]}
    ),

    # Sample 157
    (
        'улица земляной вал 105064 29',
        {'entities': [(0, 18, 'addr:street'), (19, 25, 'addr:postcode'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 158
    (
        '125047 46 2-я брестский улица',
        {'entities': [(0, 6, 'addr:postcode'), (7, 9, 'addr:housenumber'), (10, 29, 'addr:street')]}
    ),

    # Sample 159
    (
        '125047 7 улица бутырский вал',
        {'entities': [(0, 6, 'addr:postcode'), (7, 8, 'addr:housenumber'), (9, 28, 'addr:street')]}
    ),

    # Sample 160
    (
        '125047 1-я тверская-ямский улица 36 с1',
        {'entities': [(0, 6, 'addr:postcode'), (7, 32, 'addr:street'), (33, 35, 'addr:housenumber'), (36, 38, 'addr:buildingnumber')]}
    ),

    # Sample 161
    (
        '34 1-я тверская-ямский улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 28, 'addr:street')]}
    ),

    # Sample 162
    (
        '1-я тверская-ямский улица 30',
        {'entities': [(0, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 163
    (
        'улица александр невский 1',
        {'entities': [(0, 23, 'addr:street'), (24, 25, 'addr:housenumber')]}
    ),

    # Sample 164
    (
        '32 125047 1-я тверская-ямский улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 9, 'addr:postcode'), (10, 35, 'addr:street')]}
    ),

    # Sample 165
    (
        '4-й лесной переулок 6',
        {'entities': [(0, 19, 'addr:street'), (20, 21, 'addr:housenumber')]}
    ),

    # Sample 166
    (
        '18 улица бутырский вал',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 22, 'addr:street')]}
    ),

    # Sample 167
    (
        'улица бутырский вал 7 к2',
        {'entities': [(0, 19, 'addr:street'), (20, 21, 'addr:housenumber'), (22, 24, 'addr:corpusnumber')]}
    ),

    # Sample 168
    (
        '22 улица бутырский вал',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 22, 'addr:street')]}
    ),

    # Sample 169
    (
        '24 улица бутырский вал',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 22, 'addr:street')]}
    ),

    # Sample 170
    (
        '2-й лесной переулок 11 с1',
        {'entities': [(0, 19, 'addr:street'), (20, 22, 'addr:housenumber'), (23, 25, 'addr:buildingnumber')]}
    ),

    # Sample 171
    (
        'улица бутырский вал 20',
        {'entities': [(0, 19, 'addr:street'), (20, 22, 'addr:housenumber')]}
    ),

    # Sample 172
    (
        '4-я тверская-ямский улица 125047 12 с2',
        {'entities': [(0, 25, 'addr:street'), (26, 32, 'addr:postcode'), (33, 35, 'addr:housenumber'), (36, 38, 'addr:buildingnumber')]}
    ),

    # Sample 173
    (
        '125047 5 с19 улица фадеев',
        {'entities': [(0, 6, 'addr:postcode'), (7, 8, 'addr:housenumber'), (9, 12, 'addr:buildingnumber'), (13, 25, 'addr:street')]}
    ),

    # Sample 174
    (
        '9 125047 улица фадеев',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 8, 'addr:postcode'), (9, 21, 'addr:street')]}
    ),

    # Sample 175
    (
        '5 с6 улица фадеев',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 4, 'addr:buildingnumber'), (5, 17, 'addr:street')]}
    ),

    # Sample 176
    (
        '4-я тверская-ямский улица 125047 16 к3',
        {'entities': [(0, 25, 'addr:street'), (26, 32, 'addr:postcode'), (33, 35, 'addr:housenumber'), (36, 38, 'addr:corpusnumber')]}
    ),

    # Sample 177
    (
        '12 с1 125047 4-я тверская-ямский улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:buildingnumber'), (6, 12, 'addr:postcode'), (13, 38, 'addr:street')]}
    ),

    # Sample 178
    (
        '125047 7 с3 улица фадеев',
        {'entities': [(0, 6, 'addr:postcode'), (7, 8, 'addr:housenumber'), (9, 11, 'addr:buildingnumber'), (12, 24, 'addr:street')]}
    ),

    # Sample 179
    (
        '4-я тверская-ямский улица 16 к1 125047',
        {'entities': [(0, 25, 'addr:street'), (26, 28, 'addr:housenumber'), (29, 31, 'addr:corpusnumber'), (32, 38, 'addr:postcode')]}
    ),

    # Sample 180
    (
        '125047 10 с1 улица чаяновый',
        {'entities': [(0, 6, 'addr:postcode'), (7, 9, 'addr:housenumber'), (10, 12, 'addr:buildingnumber'), (13, 27, 'addr:street')]}
    ),

    # Sample 181
    (
        '5 125047 улица фадеев',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 8, 'addr:postcode'), (9, 21, 'addr:street')]}
    ),

    # Sample 182
    (
        '125047 5 с1 улица фадеев',
        {'entities': [(0, 6, 'addr:postcode'), (7, 8, 'addr:housenumber'), (9, 11, 'addr:buildingnumber'), (12, 24, 'addr:street')]}
    ),

    # Sample 183
    (
        '10 с2 улица чаяновый 125047',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:buildingnumber'), (6, 20, 'addr:street'), (21, 27, 'addr:postcode')]}
    ),

    # Sample 184
    (
        'улица фадеев 7 с2 125047',
        {'entities': [(0, 12, 'addr:street'), (13, 14, 'addr:housenumber'), (15, 17, 'addr:buildingnumber'), (18, 24, 'addr:postcode')]}
    ),

    # Sample 185
    (
        'улица фадеев 13/5 с15',
        {'entities': [(0, 12, 'addr:street'), (13, 17, 'addr:housenumber'), (18, 21, 'addr:buildingnumber')]}
    ),

    # Sample 186
    (
        '4-я тверская-ямский улица 125047 8/9',
        {'entities': [(0, 25, 'addr:street'), (26, 32, 'addr:postcode'), (33, 36, 'addr:housenumber')]}
    ),

    # Sample 187
    (
        'улица фадеев 125047 5 с1',
        {'entities': [(0, 12, 'addr:street'), (13, 19, 'addr:postcode'), (20, 21, 'addr:housenumber'), (22, 24, 'addr:buildingnumber')]}
    ),

    # Sample 188
    (
        '125047 улица чаяновый 12',
        {'entities': [(0, 6, 'addr:postcode'), (7, 21, 'addr:street'), (22, 24, 'addr:housenumber')]}
    ),

    # Sample 189
    (
        '5а с1 улица фадеев',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:buildingnumber'), (6, 18, 'addr:street')]}
    ),

    # Sample 190
    (
        '7 с1 улица фадеев 125047',
        {'entities': [(0, 1, 'addr:housenumber'), (2, 4, 'addr:buildingnumber'), (5, 17, 'addr:street'), (18, 24, 'addr:postcode')]}
    ),

    # Sample 191
    (
        '4-я тверская-ямский улица 125047 16',
        {'entities': [(0, 25, 'addr:street'), (26, 32, 'addr:postcode'), (33, 35, 'addr:housenumber')]}
    ),

    # Sample 192
    (
        '4-я тверская-ямский улица 22',
        {'entities': [(0, 25, 'addr:street'), (26, 28, 'addr:housenumber')]}
    ),

    # Sample 193
    (
        '4-я тверская-ямский улица 10 125047',
        {'entities': [(0, 25, 'addr:street'), (26, 28, 'addr:housenumber'), (29, 35, 'addr:postcode')]}
    ),

    # Sample 194
    (
        '125047 4-я тверская-ямский улица 22 к2',
        {'entities': [(0, 6, 'addr:postcode'), (7, 32, 'addr:street'), (33, 35, 'addr:housenumber'), (36, 38, 'addr:corpusnumber')]}
    ),

    # Sample 195
    (
        '16 к2 4-я тверская-ямский улица 125047',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:corpusnumber'), (6, 31, 'addr:street'), (32, 38, 'addr:postcode')]}
    ),

    # Sample 196
    (
        '125047 1-й тверской-ямский переулок 11',
        {'entities': [(0, 6, 'addr:postcode'), (7, 35, 'addr:street'), (36, 38, 'addr:housenumber')]}
    ),

    # Sample 197
    (
        '14 с3 125047 4-я тверская-ямский улица',
        {'entities': [(0, 2, 'addr:housenumber'), (3, 5, 'addr:buildingnumber'), (6, 12, 'addr:postcode'), (13, 32, 'addr:street'), (33, 38, 'addr:street')]}
    ),

    # Sample 198
    (
        '4-я тверская-ямский улица 125047 20 с1',
        {'entities': [(0, 25, 'addr:street'), (26, 32, 'addr:postcode'), (33, 35, 'addr:housenumber'), (36, 38, 'addr:buildingnumber')]}
    ),

    # Sample 199
    (
        '4-я тверская-ямский улица 24 125047',
        {'entities': [(0, 25, 'addr:street'), (26, 28, 'addr:housenumber'), (29, 35, 'addr:postcode')]}
    ),

    # Sample 200
    (
        'миусский площадь 125047 4',
        {'entities': [(9, 16, 'addr:street'), (17, 23, 'addr:postcode'), (24, 25, 'addr:housenumber')]}
    ),
]
