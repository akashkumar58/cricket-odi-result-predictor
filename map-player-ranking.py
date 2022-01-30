import sys

def search(name,listName):
	for  i in range(len(listName)):
		if(listName[i] == name):
			return (i + 1)

# Printing the header of dataset file
print("team1,team2,city,date,toss_winner,first_batting,team1_player1_bat_rank,team1_player1_bowl_rank,team1_player2_bat_rank,team1_player2_bowl_rank,team1_player3_bat_rank,team1_player3_bowl_rank,team1_player4_bat_rank,team1_player4_bowl_rank,team1_player5_bat_rank,team1_player5_bowl_rank,team1_player6_bat_rank,team1_player6_bowl_rank,team1_player7_bat_rank,team1_player7_bowl_rank,team1_player8_bat_rank,team1_player8_bowl_rank,team1_player9_bat_rank,team1_player9_bowl_rank,team1_player10_bat_rank,team1_player10_bowl_rank,team1_player11_bat_rank,team1_player11_bowl_rank,team2_player1_bat_rank,team2_player1_bowl_rank,team2_player2_bat_rank,team2_player2_bowl_rank,team2_player3_bat_rank,team2_player3_bowl_rank,team2_player4_bat_rank,team2_player4_bowl_rank,team2_player5_bat_rank,team2_player5_bowl_rank,team2_player6_bat_rank,team2_player6_bowl_rank,team2_player7_bat_rank,team2_player7_bowl_rank,team2_player8_bat_rank,team2_player8_bowl_rank,team2_player9_bat_rank,team2_player9_bowl_rank,team2_player10_bat_rank,team2_player10_bowl_rank,team2_player11_bat_rank,team2_player11_bowl_rank,match_winner")

with open('data/rankings_on_date.csv') as file1:
	 content = file1.readlines()
	 for i in range(len(content)):
                line = str(content[i].strip("\n")).split(",")[1:]
                batsmen = line[0:100]
                bowler = line[100:200]
                count = 0
                line_data = ""
                with open('data/dataset.csv') as file2:
                        line_data = file2.readlines();
                        team1_player = str(line_data[i+1]).split(",")[6:17]
                        team2_player = str(line_data[i+1]).split(",")[17:28]
                        for k in range(len(team1_player)):
                                player = team1_player[k]
                                bat_rank = 101
                                ball_rank = 101
                                if player in batsmen:
                                        bat_rank = search(player,batsmen)
                                if player in bowler:
                                        ball_rank = search(player,bowler)
                                    
                                line_data[i + 1] = line_data[i + 1].replace(player, str(bat_rank) + "," + str(ball_rank))
                        for k in range(len(team2_player)):
                                player = team2_player[k];
                                bat_rank = 101
                                ball_rank = 101
                                if player in batsmen:
                                        bat_rank = search(player, batsmen)
                                        
                                if player in bowler:
                                        ball_rank = search(player, bowler)
                                
                                line_data[i + 1] = line_data[i + 1].replace(player, str(bat_rank) + "," + str(ball_rank))
                                
                        line_data[i + 1].rstrip()
                        print( line_data[i+1].rstrip() )
