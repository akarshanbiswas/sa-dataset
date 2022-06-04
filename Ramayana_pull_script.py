import requests
from bs4 import BeautifulSoup

ayodhyalink = "https://www.valmikiramayan.net/utf8/ayodhya/ayodhya_contents.htm"
aranyalink = "https://www.valmikiramayan.net/utf8/aranya/aranya_contents.htm"
kishkindalink = "https://www.valmikiramayan.net/utf8/kish/kishkindha_contents.htm"
sundaralink = "https://www.valmikiramayan.net/utf8/sundara/sundara_contents.htm"
yuddhalink = "https://www.valmikiramayan.net/utf8/yuddha/yuddha_contents.htm"


def contentlinksgrabber(mainlink):
    print("Getting all links from the main page")
    page = requests.get(mainlink)
    print("parsing the html...")
    soup = BeautifulSoup(page.content, 'html.parser')
    print("Finding all links")
    #links = soup.find_all('a')
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    return links


def framesourcegrabber(framesourcelink):
    framepage = requests.get(framesourcelink)
    soup = BeautifulSoup(framepage.content, 'html.parser')
    Sanslinks = soup.find_all('frame')
    for sanlink in Sanslinks:
            actualurl = framesourcelink.rsplit('/', 1)[0]+'/'+sanlink['src']
            return actualurl






def datagrabber(link):
    print("getting page....")
    page = requests.get(link)
    print("Parsing page...")
    datasoup = BeautifulSoup(page.content, 'html.parser')
    print("selecting Sanskrit shlokas")
    SanSloka = datasoup.select(".SanSloka")

    for shloka in SanSloka:
        print("operating on file raamasan.txt")
        filesan = open("raamasan.txt", "a")
        print("Writing to file")
        filesan.write(shloka.get_text().replace('\n','').replace("|", '।'))
        filesan.write('\n')
        print("closing file raamasan.txt")
        filesan.close
    print("selecting english translation")
    EngTrans = datasoup.select(".tat")

    for trans in EngTrans:
        print("Operating on file raamaeng.txt")
        fileeng = open("raamaeng.txt", "a")
        print("Writing to file")
        fileeng.write(trans.get_text().replace('\n',''))
        fileeng.write('\n')
        print("closing file raamaeng.txt")
        fileeng.close()


def main():

    for link in contentlinksgrabber(ayodhyalink):
        if "sarga" in link:
             datagrabber(framesourcegrabber(f"https://www.valmikiramayan.net/utf8/ayodhya/{link}"))
        
    for link in contentlinksgrabber(aranyalink):
        if "sarga" in link:
             datagrabber(framesourcegrabber(f"https://www.valmikiramayan.net/utf8/aranya/{link}"))

    for link in contentlinksgrabber(kishkindalink):
        if "sarga" in link:
             datagrabber(framesourcegrabber(f"https://www.valmikiramayan.net/utf8/kishkinda/{link}"))

    for link in contentlinksgrabber(sundaralink):
        if "sarga" in link:
             datagrabber(framesourcegrabber("https://www.valmikiramayan.net/utf8/sundara/{link}"))

    for link in contentlinksgrabber(yuddhalink):
        if "sarga" in link:
             datagrabber(framesourcegrabber(f"https://www.valmikiramayan.net/utf8/yuddha/{link}"))

if __name__ == "__main__":
    main()
