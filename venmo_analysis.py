''' do sum reading n analysis!! '''
import csv

def readVenmo():

    result = []
    desc = []
    date = []
    with open('venmo_data.tsv', 'r') as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            desc.append(unicode(line[0], 'utf-8'))
            date.append(line[1])

    for d in desc:
        dnew = d.encode('unicode_escape')
        r = analyze(dnew)
        if r != None:
            result.append(r)

    printReciept(result)

def analyze(d):
    if '\U0001f32e' in d:
        return 'You love tacos.'

def printReciept(result):
    print 'According to our analysis...'
    for l in result:
        print l

readVenmo()
