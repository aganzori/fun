''' Scrape & analyze venmo page '''
from dict import emoji_dict
from lxml import html
import requests
import csv

class venmo:

    def scrape(self, username):
        page = requests.get('https://venmo.com/' + username)
        tree = html.fromstring(page.content)
        result = []

        # TODO: fix tran
        #tran = tree.xpath('//div[@class="paymentpage-subline"]/text()')
        desc = tree.xpath('//div[@class="paymentpage-text m_five_t"]/text()')
        date = tree.xpath('//div[@class="date"]/text()')

        for i in range (len(desc)):
            de = desc[i].encode('unicode_escape')
            da = fixDate(date[i].encode('ascii'))

            r = analyze(de)
            if len(r) != 0:
                result.append(r)

        print 'According to our analysis...'
        print result
        return result

def analyze(d): #TODO: currently just my fav emojis
    result= []
    while '\U0001f' in d:
        begin = d.find('\U0001f')
        emutf = d[begin:begin+10]
        d = d[begin+10:]
        result.append(emoji_dict[emutf])
    return result

def fixDate(ugly):
    arr = ugly.split()
    # TODO: fix recent transactions that show up differently
    return arr[1] +' '+ arr[2] +' '+ arr[3]



def main():
    v = venmo()
    v.scrape('je-nnywong')

if __name__ == "__main__":
    main()
