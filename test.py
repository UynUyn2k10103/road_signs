def traffic_sign():
    dic = {}

    with open("traffic_sign.txt", mode='r', encoding='utf-8-sig') as f:
        while True:
            s = f.readline().strip()
            if s == '':
                break
            s1 = f.readline().strip()
            dic.update({s:s1})

    return dic

