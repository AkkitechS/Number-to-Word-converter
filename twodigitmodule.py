def twodigit(no):
    # creating dictionaries for number
    dict09 = {"0":'zero', '1':'one', '2':'two', '3':'three', '4':'four',
              '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    dict1119 = {'11':'eleven', '12':'twelve', '13':'thirteen',
                '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen',
                '18':'eighteen', '19':'ninteen'}
    dict10 = {'10':'ten', '20':'twenty', '30':'thirty', '40':'fourty',
              '50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninty'}
    wnum = ''
    extrct = 0


    # getting no and printing to word
    if no == '0':
        return 'zero'
    elif no[0] == '0':
        no = int(no) - int(no) + int(no)
    if str(no) in dict09:
        wnum = dict09.get(str(no))
    elif str(no) in dict1119:
        wnum = dict1119.get(str(no))
    elif str(no) in dict10:
        wnum = dict10.get(str(no))
    else:
        extrct = str(no[0]) + '0'
        extrct1 = int(no) - int(extrct)
        wnum = dict10[extrct] + '-' + dict09[str(extrct1)]

    return wnum


#inp = input("Enter the number")
#print(twodigit(inp))
