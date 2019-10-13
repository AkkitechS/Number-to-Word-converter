import twodigitmodule as tg
import threedigitmodule as th
import fourdigitmodule as fg
import fivedigitmodule as fi
import sixdigitmodule as sx

def sevendigit(n5):
    dictlakh = {'100000':'lakh'}

    if n5 == '0' * 7:
        return 'zer0 ' * 7
    elif len(n5) == 1:
        return tg.twodigit(n5)
    elif len(n5) == 2:
        return tg.twodigit(n5)
    elif len(n5) == 3:
        return th.threedigit(n5)
    elif len(n5) == 4:
        return fg.fourdigit(n5)
    elif len(n5) == 5:
        return fi.fivedigit(n5)
    elif len(n5) == 6:
        return sx.sixdigit(n5)
    elif n5[0] == '0':
        n5 = int(n5) - int(n5) + int(n5)
        n5 = str(n5)
        if len(n5) == 1:
            return tg.twodigit(n5)
        elif len(n5) == 2:
            return tg.twodigit(n5)
        elif len(n5) == 3:
            return th.threedigit(n5)
        elif len(n5) == 4:
            return fg.fourdigit(n5)
        elif len(n5) == 5:
            return fi.fivedigit(n5)
        elif len(n5) == 6:
            return sx.sixdigit(n5)

    elif n5[2:] == '00000':
        return tg.twodigit(n5[0:2]) + '-' + dictlakh['100000']
    else:
        return tg.twodigit(n5[0:2]) + '-' + dictlakh['100000'] + '-' + fi.fivedigit(n5[2:])

#inp = input("Enter the no:")
#print(sevendigit(inp))
