import twodigitmodule as tg
import threedigitmodule as th
import fourdigitmodule as fg
import fivedigitmodule as fi

def sixdigit(n4):
    dictlakh = {'100000':'lakh'}
    if n4 == '0' * 6:
        return 'zero ' * 6
    elif len(n4) == 1:
        return tg.twodigit(n4)
    elif len(n4) == 2:
        return tg.twodigit(n4)
    elif len(n4) == 3:
        return th.threedigit(n4)
    elif len(n4) == 4:
        return fg.fourdigit(n4)
    elif len(n4) == 5:
        return fi.fivedigit(n4)
    elif n4[0] == '0':
        n4 = int(n4) - int(n4) + int(n4)
        n4 = str(n4)
        if len(n4) == 1:
            return tg.twodigit(n4)
        elif len(n4) == 2:
            return tg.twodigit(n4)
        elif len(n4) == 3:
            return th.threedigit(n4)
        elif len(n4) == 4:
            return fg.fourdigit(n4)
        elif len(n4) == 5:
            return fi.fivedigit(n4)

    elif n4[1:] == '00000':
        return tg.twodigit(n4[0]) + '-' + dictlakh['100000']
    else:
        return tg.twodigit(n4[0]) + '-' + dictlakh['100000'] + '-' + fi.fivedigit(n4[1:])

#inp = input("Enter the no:")
#print(sixdigit(inp))
