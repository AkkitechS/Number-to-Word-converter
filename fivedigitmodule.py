import twodigitmodule as tg
import threedigitmodule as th
import fourdigitmodule as fg

def fivedigit(n3):
    dict1000 = {'1000':'thousand'}

    if n3 == '00000':
        return 'zero ' * 5
    elif len(n3) == 1:
        return tg.twodigit(n3)
    elif len(n3) == 2:
        return tg.twodigit(n3)
    elif len(n3) == 3:
        return th.threedigit(n3)
    elif len(n3) == 4:
        return fg.fourdigit(n3)
    elif n3[0] == '0':
        n3 = int(n3) - int(n3) + int(n3)
        n3 = str(n3)
        if len(n3) == 1:
            return tg.twodigit(n3)
        elif len(n3) == 2:
            return tg.twodigit(n3)
        elif len(n3) == 3:
            return th.threedigit(n3)
        elif len(n3) == 4:
            return fg.fourdigit(n3)
    elif n3[2:] == '000':
        return tg.twodigit(n3[0:2]) + '-' + dict1000['1000']
    else:
        return tg.twodigit(n3[0:2]) + '-' + dict1000['1000'] + '-' + th.threedigit(n3[2:])

#inp = input("ENter the no:")
#print(fivedigit(inp))
