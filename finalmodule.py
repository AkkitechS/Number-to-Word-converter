import twodigitmodule as tg
import threedigitmodule as th
import fourdigitmodule as fg
import fivedigitmodule as fi
import sixdigitmodule as sx
import sevendigitmodule as svn
import eightdigitmodule as eg
import ninedigitmodule as nn

def final(num):
    if len(num) == 1:
        return tg.twodigit(num)
    elif len(num) == 2:
        return tg.twodigit(num)
    elif len(num) == 3:
        return th.threedigit(num)
    elif len(num) == 4:
        return fg.fourdigit(num)
    elif len(num) == 5:
        return fi.fivedigit(num)
    elif len(num) == 6:
        return sx.sixdigit(num)
    elif len(num) == 7:
        return svn.sevendigit(num)
    elif len(num) == 8:
        return eg.eightdigit(num)
    elif len(num) == 9:
        return nn.ninedigit(num)
