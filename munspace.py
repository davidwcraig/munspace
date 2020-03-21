# munspace.py
# munsell colors module

# dwc 2020-03-19T13:49 

#initialization code:

import csv #needed for reading the munsell chips csv database
with open('munsell_chips.csv') as fl:
    reader = csv.reader(fl)

L = []   #will be list of [hue, value, chroma, rgb hex string]
with open('munsell_chips.csv') as fl:
    reader = csv.reader(fl)
    for row in reader:
        L.append(row)

#this makes a dictionary keyed by (hue, value) with empty entries
dhues = { (row[0], int(row[1])) : {} for row in L[1:] }  # skips header row

# this updates each key in dhues with values {chroma, hex}
# gives a dictionary with a hierarchy:
# top level is keys (hue, value)
# next level is key: munsell chroma, value: rgb hexstring
# so you can get munsell chromas available for a given (hue, value) pair.
for row in L[1:]:   #skip the header row
    dhues[(row[0], int(row[1]))].update({ int(row[2]) : row[3]})
     
# Some lists that may be useful for imports:
hue_compass = ['R', 'YR', 'Y', 'GY', 'G', 'BG', 'B', 'PB', 'P', 'RP']
nms = ['2.5', '5', '7.5', '10']
hues = [n+c for c in hue_compass for n in nms ]
midhues = ['5'+c for c in hue_compass ]

def hvc(h, v = 5, c = 'middle'):
    """
    returns rbg hex string of 'high', 'middle' or 'low' chroma=c for munsell
    h=hue, v=value.
    
    defaults to 'middle' chroma.
    """
    clist = list(dhues[(h,v)].keys())
    clist.sort() # precaution to guarantee ordering
    mdc = len(clist)//2 # Crude median
    loc = 0             # low chroma
    hic = len(clist)-1  # high chroma
    d = {'low' : loc, 'middle' : mdc, 'high' : hic} #dictionary of arguments for c
    
    return dhues[(h,v)][clist[ d[c] ]]
   
