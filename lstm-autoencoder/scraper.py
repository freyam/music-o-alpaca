from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import time

save_dir = "./audios/"

url0 = "https://www.mutopiaproject.org/cgibin/make-table.cgi?startat="
url1 = "&searchingfor=&Composer=&Instrument=Guitar&Style=&collection=&id=&solo=&recent=&timelength=&timeunit=&lilyversion=&preview="

songNumber = 0
linkCount = 10

while linkCount > 0:
    url = url0 + str(songNumber) + url1
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "html.parser")
    links = soup.find_all("a")
    linkCount = 0
    for link in links:
        href = link["href"]
        if href.find(".mid") >= 0:
            linkCount = linkCount + 1
            urlretrieve(href, save_dir + href[href.rfind("/") + 1 :])
    songNumber += 10
    time.sleep(10.0)

    print("Downloaded " + str(songNumber) + " songs")
