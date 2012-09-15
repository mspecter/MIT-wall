from bs4 import BeautifulSoup
import requests
import pyNotificationCenter
import time

def main():
    website = "http://scripts.mit.edu/~mitoc/wall/"
    current_results = []

    secs = 360

    while 1:
        
        request = requests.get(website) 

        if request.status_code != 200:
            print "fail! no access to website!"

        soup = BeautifulSoup(request.content)

        blah = soup.findAll('table', {"class":"timeline"})
        blah = blah[0]
        blah2 = blah.findAll('div', {'class': "entry open "})
        blah2 = [i.strings for i in blah2]
        out = ""
        for i in blah2:
            for j in i:
                if j.strip():
                    out += j
            out += '\n'

        timeline = out
        print timeline
        if timeline == current_results:
            print "NO NEWS!"
        elif timeline:
            # NOTIFY
            print timeline
            if current_results != timeline:
                current_results = timeline
            
                print "NEWS!"
                pyNotificationCenter.notify("NEWS!", "New Wall Climbing Times", timeline )
        else:
            print "NO NEWS!"

        time.sleep(secs)

if __name__ == "__main__":
   main() 
