import twodigitmodule as tg
import threedigitmodule as th
def fourdigit(n2):
    dict1000 = {'1000':'thousand'}
    if n2 == '0000':
        return 'zero ' * 4
    elif len(n2) == 1:
        return tg.twodigit(n2)
    elif len(n2) == 2:
        return tg.twodigit(n2)
    elif len(n2) == 3:
        return th.threedigit(n2)
    elif str(n2[0]) == '0':
        n2 = int(n2) - int(n2) + int(n2)
        n2 = str(n2)
        if len(str(n2)) == 1:
            return tg.twodigit(str(n2))
        elif len(str(n2)) == 2:
            return tg.twodigit(str(n2))
        elif len(str(n2)) == 3:
            return th.threedigit(str(n2))
    if str(n2[1:]) == '000':
        return tg.twodigit(n2[0]) + '-' + dict1000['1000']

    else:
        return tg.twodigit(str(n2[0])) + '-' + dict1000.get('1000') + '-' + th.threedigit(str(n2[1:]))
    #elif str(n2[1:]) == '000':
     #   return tg.twodigit(n2[0]) + '-' + dict1000['1000']

#inp = input("Enter the no:")
#print(fourdigit(inp))
