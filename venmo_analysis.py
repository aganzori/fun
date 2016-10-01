''' do sum reading n analysis!! '''
import csv

def readVenmo():

    desc = []
    date = []
    with open('venmo_data.tsv', 'r') as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"):
            desc.append(unicode(line[0], 'utf-8'))
            date.append(line[1])
    print 'file read'

    print desc
    print date

readVenmo()
