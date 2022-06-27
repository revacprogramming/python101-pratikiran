
def get_cs():
    a = input()
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


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


main()
