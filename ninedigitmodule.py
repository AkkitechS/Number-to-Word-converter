import twodigitmodule as tg
import threedigitmodule as th
import fourdigitmodule as fg
import fivedigitmodule as fi
import sixdigitmodule as sx
import sevendigitmodule as svn
import eightdigitmodule as eg

def ninedigit(n7):

    dictcrore = {'100000000':'crore'}

    if n7 == '0' * 9:
        return 'zero ' * 9
    elif len(n7) == 1:
        return tg.twodigit(n7)
    elif len(n7) == 2:
        return tg.twodigit(n7)
    elif len(n7) == 3:
        return th.threedigit(n7)
    elif len(n7) == 4:
        return fg.fourdigit(n7)
    elif len(n7) == 5:
        return fi.fivedigit(n7)
    elif len(n7) == 6:
        return sx.sixdigit(n7)
    elif len(n7) == 7:
        return svn.sevendigit(n7)
    elif len(n7) == 8:
        return eg.eightdigit(n7)
    elif n7[0] == '0':
        n7 = int(n7) - int(n7) + int(n7)
        n7 = str(n7)

        if len(n7) == 1:
            return tg.twodigit(n7)
        elif len(n7) == 2:
            return tg.twodigit(n7)
        elif len(n7) == 3:
            return th.threedigit(n7)
        elif len(n7) == 4:
            return fg.fourdigit(n7)
        elif len(n7) == 5:
            return fi.fivedigit(n7)
        elif len(n7) == 6:
            return sx.sixdigit(n7)
        elif len(n7) == 7:
            return svn.sevendigit(n7)
        elif len(n7) == 8:
            return eg.eightdigit(n7)
    elif n7[1:] == '0' * 8:
        return tg.twodigit(n7[0:2]) + '-' + dictcrore['100000000']
    else:
        return tg.twodigit(n7[0:2]) + '-' + dictcrore['100000000'] + '-' + svn.sevendigit(n7[2:])

#inp = input("Enter the no:")
#print(ninedigit(inp))
