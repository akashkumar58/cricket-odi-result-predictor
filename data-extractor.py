import urllib.request, re
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import sys

url = "http://www.espncricinfo.com/"
file_name = sys.argv[1]
with open(file_name) as f:
    for line in f:
        complete_url = url + line
        request = urllib.request.Request(complete_url)
        page = urllib.request.urlopen(request).read()
        soup = BeautifulSoup(page, "lxml")

        row = ""
        
        """
            finding Team Names
        """
        teams = soup.find('div', {'class': 'team-1-name'}).text.split(' v ')
        team1 = teams[0].lstrip()
        team2 = teams[1].rstrip()

        row += team1 + ","
        row += team2 + ","

        venue = soup.find_all('a', {'class': 'headLink'})[3].text
        city = ""
        if venue.find(',') >= 0:
            city += venue.split(',')[1].lstrip().rstrip()
        else:
            city += venue

        row += city + ","

        date_list = soup.find_all('div', {'class': 'space-top-bottom-5'})[-1].text
        if date_list.find(',') >= 0:
            date_list = date_list.split(',')[1]
        date = ' '.join(date_list.split()[0:3])
        
        row += date + ","

        toss = soup.find_all('div', {'class': "match-information"})[1].\
                        find('span').text

        if toss == team1:
            row += "0,"
        else:
            row += "1,"
        
        first_bat = soup.find_all('th', {"class":\
            "th-innings-heading"})[0].text.split('innings')[0].rstrip()

        if (first_bat == team1):
            row += "0,"
        else:
            row += "1,"

        regex = re.compile('[^a-zA-Z ]')
        team1_players = []
        players1 = soup.find_all('table', {"class": "batting-table innings"})[0].\
                find_all('td',{"class": "batsman-name"})
        for player in players1:
            player_name = player.text.rstrip()
            p = regex.sub("", player_name)
            team1_players.append(p)
            row += p + ","

        if len(team1_players) != 11:
            rem_players = soup.find_all('div', {"class": "more-match-stats"})[0].\
                        find_all('a', {"class": "playerName"})
            for each in rem_players:
                player_name = each.text.rstrip()
                p = regex.sub("", player_name)
                team1_players.append(p)
                row += p + ","

        team2_players = []
        players1 = soup.find_all('table', {"class": "batting-table innings"})[1].\
                find_all('td',{"class": "batsman-name"})
        for player in players1:
            player_name = player.text.rstrip()
            p = regex.sub('', player_name)
            team2_players.append(p)
            row += p + ","

        if len(team2_players) != 11:
            rem_players = soup.find_all('div', {"class": "more-match-stats"})[1].\
                        find_all('a', {"class": "playerName"})
            for each in rem_players:
                player_name = each.text.rstrip()
                p = regex.sub('', player_name)
                team2_players.append(p)
                row += p + ","

        winner_info = soup.find('div', {"class": "innings-requirement"}).text
        winner = ""
        
        if winner_info.find("won") >= 0:
            winner = winner_info.split(" won ")[0]
        elif winner_info.find("No result") >= 0:
            winner = "no result"
            continue
        elif winner_info.find("Match tied") >= 0:
            winner = "tie"

        if winner == team1:
            row += "0"
        elif winner == team2:
            row += "1"
        elif winner == "tie":
            row += "2"

        if row.find(",,") >= 0:
            continue

        print(row)
