import urllib.request, re
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import sys

month = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]

half_url_batsmen = "http://www.relianceiccrankings.com/datespecific/odi/?stattype=batting&"
half_url_bowlers = "http://www.relianceiccrankings.com/datespecific/odi/?stattype=bowling&"

filename = sys.argv[1]
fP = open(filename, "r")

for line in fP.readlines()[1:]:
    cols = line.split(",")
    date = cols[3].split(" ")
    dd = date[0]
    mm = str(month.index(date[1]) + 1)
    yy = date[2]

    bat_url = half_url_batsmen + "day=" + dd + "&month=" + mm + "&year=" + yy
    bowl_url = half_url_bowlers + "day=" + dd + "&month=" + mm + "&year=" + yy
    
    request = urllib.request.Request(bat_url)
    page = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(page, "lxml")

    row = "" + dd
    row += " " + month[ int(mm) - 1]
    row += " " + yy.rstrip()
    
    rankings = soup.find_all('td', {"class": "top100name"})
    for ranks in rankings:
        player = ranks.find('a').text.lstrip().rstrip().replace(".", "")
        row += "," + player.replace("'", "")
        
    request = urllib.request.Request(bowl_url)
    page = urllib.request.urlopen(request).read()
    soup = BeautifulSoup(page, "lxml")
    
    rankings = soup.find_all('td', {"class": "top100name"})
    for ranks in rankings:
        player = ranks.find('a').text.lstrip().rstrip().replace(".", "")
        row += "," + player.replace("'", "")

    print(row)

fP.close()
