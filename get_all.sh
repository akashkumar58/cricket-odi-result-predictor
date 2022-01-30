echo "team1,team2,city,date,toss_winner,first_batting,team1_player1,team1_player2,team1_player3,team1_player4,team1_player5,team1_player6,team1_player7,team1_player8,team1_player9,team1_player10,team1_player11,team2_player1,team2_player2,team2_player3,team2_player4,team2_player5,team2_player6,team2_player7,team2_player8,team2_player9,team2_player10,team2_player11,match_winner"

for i in links/links_1990.csv links/links_1991.csv links/links_1992.csv links/links_1993.csv links/links_1994.csv links/links_1995.csv links/links_1996.csv links/links_1997.csv links/links_1998.csv links/links_1999.csv links/links_2000.csv links/links_2001.csv links/links_2002.csv links/links_2003.csv links/links_2004.csv links/links_2005.csv links/links_2006.csv links/links_2007.csv links/links_2008.csv links/links_2009.csv links/links_2010.csv links/links_2011.csv links/links_2012.csv links/links_2013.csv links/links_2014.csv links/links_2015.csv links/links_2016.csv
do
        python3 data-extractor.py $i
done
