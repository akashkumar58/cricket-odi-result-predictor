import urllib.request, re
from html.parser import HTMLParser

data = ""

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global data
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    matched_data = re.search('/ci/engine/match/[0-9]+\.html', value)
                    if matched_data is not None:
                        data += str( matched_data.group(0) )  + "\n"


url = "http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id="

for yr in range(1990, 2017):
    
    last_part = str(yr) + ";type=year"
    fP = open("links/links_"+ str(yr) + ".csv", "w")
    data = ""
    
    request = urllib.request.Request(url + last_part)
    response = urllib.request.urlopen(request).read()
    parser = MyHTMLParser()
    parser.feed(str(response))
    
    fP.write(data)
    fP.close()
