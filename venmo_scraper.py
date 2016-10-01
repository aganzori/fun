''' Scrape venmo page '''
from lxml import html
import requests

def fixDate(ugly):
    arr = ugly.split()
    # TODO: fix recent transactions that show up differently
    return arr[1] +' '+ arr[2] +' '+ arr[3]

username = 'je-nnywong'

page = requests.get('https://venmo.com/' + username)

tree = html.fromstring(page.content)

# TODO: fix tran
#tran = tree.xpath('//div[@class="paymentpage-subline"]/text()')
desc = tree.xpath('//div[@class="paymentpage-text m_five_t"]/text()')
date = tree.xpath('//div[@class="date"]/text()')

# Write the lists to file
fileout = open('venmo_data.tsv', 'w')

for i in range (len(desc)): 
    de = desc[i].encode('utf=8') # emojis are unicode
    da = fixDate(date[i].encode('ascii'))
    fileout.write(de + '\t' + da + '\n')

print 'finished'
fileout.close()
