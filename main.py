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
    array = []
    for i in tweetsOutput :
        if check(i.tweet) != None :
            address = check(i.tweet)
            object =  {'username' : i.username , 'address' : address.group()}
            array.append(object)
   # print(array)
    #dump = json.dumps(array)
    '''with open('data.json', 'w') as outfile:
        for obj in array:
            dump = json.dumps(obj)
            json.dump(dump, outfile)'''
    #dump = json.dumps(array)
   # print(dump)
    with open('data.json', 'w') as outfile:
        json.dump(array, outfile)
    print('keys 🔑 has been added to data.json file 💾')
        
            


def main():
   
    parser = argparse.ArgumentParser(description='search bitcoin address in twitter')

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