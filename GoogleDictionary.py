# -*- coding: utf-8 -*-

import urllib.request
import sys

def main():
    while True:
        try:
            sw=input('Enter your search word (Type "exit" to exit): ')
            if sw.lower() == 'exit':
                print('exiting...')
                return
            sw=str('define'+'+'+sw)
            sw=sw.replace(' ','+')
            url=str('https://www.google.com/search?q='+str(sw))
            head = {}
            head['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            
            req=urllib.request.Request(url,headers=head)
            resp=urllib.request.urlopen(req)
            reqdata=resp.read()
    #        newfile=open('reqdata.txt','w')
    #        newfile.write(str(reqdata))
            print(str(reqdata).split('dfn',1)[1].split('span',3)[1].replace('>',' ').rstrip('</'))
    #        newfile.close()
        except Exception as e:
            print('Sorry! Cannot find this word in my diectionary!! Try again...')
            
if __name__ == "__main__":
    main()
