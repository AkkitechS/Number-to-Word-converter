import twodigitmodule as tg

def threedigit(n1):
    dict100 = {'100':'hundred'}
    wnum = ''

    if n1 == '000':
        wnum = 'zero zero zero'
    elif len(str(n1)) == 1:
        return tg.twodigit(n1)
    elif len(str(n1)) == 2:
        return tg.twodigit(n1)

    elif n1[0] == '0':
        n1 = int(n1) - int(n1) + int(n1)
        if len(str(n1)) == 1:
            return tg.twodigit(str(n1))
        elif len(str(n1)) == 2:
            return tg.twodigit(str(n1))
    if int(n1) % 100 == 0:
        wnum = tg.twodigit(str(n1[0])) + '-' + dict100.get('100')
    elif int(n1) % 100 != 0:
        wnum = tg.twodigit(str(n1[0])) + '-' + dict100['100'] + '-' + tg.twodigit(str(n1[1:]))
    return wnum
#inp = input("ENter the no:")
#print(threedigit(inp))
