def get_cs():
    a = input('Enter : ')
    return a


def cs_to_lot(cs):
    data = list()
    a = cs.split(';')
    if '' in a:
        a.remove('')
    for ele in a:
        t = ele.split('=')
        t = tuple(t)
        data.append(t)
    return data


def lot_to_cs(lot):
    a = ''
    for t in lot:
        if t == lot[(len(lot)-1)]:
            a = a+t[0]+'='+t[1]
            continue
        a = a+t[0]+'='+t[1]+';'
    return a


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
