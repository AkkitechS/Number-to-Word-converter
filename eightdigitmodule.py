import twodigitmodule as tg
import threedigitmodule as th
import fourdigitmodule as fg
import fivedigitmodule as fi
import sixdigitmodule as sx
import sevendigitmodule as svn

def eightdigit(n6):

    dictcrore = {'10000000':'crore'}

    if n6 == '0' * 8:
        return 'zero ' * 8
    elif len(n6) == 1:
        return tg.twodigit(n6)
    elif len(n6) == 2:
        return tg.twodigit(n6)
    elif len(n6) == 3:
        return th.threedigit(n6)
    elif len(n6) == 4:
        return fg.fourdigit(n6)
    elif len(n6) == 5:
        return fi.fivedigit(n6)
    elif len(n6) == 6:
        return sx.sixdigit(n6)
    elif len(n6) == 7:
        return svn.sevendigit(n6)
    elif n6[0] == '0':
        n6 = int(n6) - int(n6) + int(n6)
        n6 = str(n6)
        if len(n6) == 1:
            return tg.twodigit(n6)
        elif len(n6) == 2:
            return tg.twodigit(n6)
        elif len(n6) == 3:
            return th.threedigit(n6)
        elif len(n6) == 4:
            return fg.fourdigit(n6)
        elif len(n6) == 5:
            return fi.fivedigit(n6)
        elif len(n6) == 6:
            return sx.sixdigit(n6)
        elif len(n6) == 7:
            return svn.sevendigit(n6)
    elif n6[1:] == '0000000':
        return tg.twodigit(n6[0]) + '-' + dictcrore['10000000']
    else:
        return tg.twodigit(n6[0]) + '-' + dictcrore['10000000'] + '-' + svn.sevendigit(n6[1:])

#inp = input("Enter the no:")
#print(eightdigit(inp))
