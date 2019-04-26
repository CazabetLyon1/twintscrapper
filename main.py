import twint
import re
import os
import json
import sys
import argparse

def check(text):
    if not re.match("RT", text):
        exp = re.compile(r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}')
        return exp.search(text)
    else:
        return None

def outputAdresses(tweetsOutput):
    dict = {}
    for i in tweetsOutput :
        if check(i.tweet) != None :
            address = check(i.tweet)
            #print('\t '+address.group() + ' ' + i.username  +'\r\n')
            dict['username'] = i.username
            dict['address'] = address.group()
    with open('data.json', 'w') as outfile:
        json.dump(dict, outfile)
            


def main():
   
    parser = argparse.ArgumentParser(description='search bitcoin adress in tweeter')

    parser.add_argument('-n', type=int, nargs='?',
                    help='number of threads. 10 by default')
    parser.add_argument('-s', nargs='?',
                    help="search value. 'search bictoin address' by default")

    args = parser.parse_args()
    
    c = twint.Config()

    # equivalent to `-s` 
    c.Search = "my bitcoin address"

    # equivalent to '-n'
    c.Limit = 10

    if args.n : 
        c.Limit = args.n
    if args.s :
        c.Search = args.s


    c.Store_object = True
    c.Custom['tweet'] = ['tweet']
    twint.run.Search(c)

    #Pour juste afficher les adresses scrap
    os.system('clear')

    print('[ - ] : adresses trouvés : \r\n')
    tweets = twint.output.tweets_object
    outputAdresses(tweets) 

main()