from bs4 import BeautifulSoup
import urllib.request

URL = 'https://www.dndbeyond.com/characters/'

class Character:
    def __init__(self, ID):
        self.ID = ID
        self.loadPage()


    def loadPage(self):
        charURL = f'{URL}{self.ID}' 
        print(charURL)
        
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
        request = urllib.request.Request(charURL,None,headers)
        page = urllib.request.urlopen(request)
        soup = BeautifulSoup(page, features="lxml")

        self.Name = soup.find('div',{'class':'ct-character-tidbits__name'})
        print(self.Name)
