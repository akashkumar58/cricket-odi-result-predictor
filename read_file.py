import pandas as pd
import sys

def read_data(fileName):

    # Creating the dataframe from file
    df = pd.read_csv(fileName)	
    X = pd.DataFrame()
    
    #X = pd.concat([X, pd.get_dummies(df['date'], prefix = 'date')], axis = 1)
    X = pd.concat([X, pd.get_dummies(df['team1'], prefix = 'team1')], axis = 1)
    X = pd.concat([X, pd.get_dummies(df['team2'], prefix = 'team2')], axis = 1)
    X = pd.concat([X, pd.get_dummies(df['city'], prefix = 'city')], axis = 1)
    X = pd.concat([X, df['toss_winner'].to_frame() ], axis = 1)
    X = pd.concat([X, df['first_batting'].to_frame() ], axis = 1)

    #Team1_players_info
    Team1 = pd.DataFrame()
    Team1 = pd.concat([Team1, df['team1_player1_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player1_bowl_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player2_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player2_bowl_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player3_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player3_bowl_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player4_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player4_bowl_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player5_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player5_bowl_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player6_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player6_bowl_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player7_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player7_bowl_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player8_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player8_bowl_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player9_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player9_bowl_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player10_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player10_bowl_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player11_bat_rank'].to_frame()], axis = 1)
    Team1 = pd.concat([Team1, df['team1_player11_bowl_rank'].to_frame()], axis = 1)

    Team2 = pd.DataFrame()
    Team2 = pd.concat([Team2, df['team2_player1_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player1_bowl_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player2_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player2_bowl_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player3_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player3_bowl_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player4_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player4_bowl_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player5_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player5_bowl_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player6_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player6_bowl_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player7_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player7_bowl_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player8_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player8_bowl_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player9_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player9_bowl_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player10_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player10_bowl_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player11_bat_rank'].to_frame()], axis = 1)
    Team2 = pd.concat([Team2, df['team2_player11_bowl_rank'].to_frame()], axis = 1)
    
    X = pd.concat([X, Team1], axis = 1)
    X = pd.concat([X, Team2], axis = 1)
    
    # Read the output column
    y = df['match_winner']
    
    # Return the features and target
    return X, y


def read_team_data(file_name):
    
    df = pd.read_csv(file_name)
    Y = df['match_winner']
    df.drop('match_winner', axis=1, inplace=True)

    X = pd.DataFrame()
    df['team1'] = df['team1'].astype('category')
    df['team2'] = df['team2'].astype('category')
    df['city'] = df['city'].astype('category')
    category_column = df.select_dtypes(['category']).columns
    X = pd.concat( [ X, df[category_column].apply(lambda ele: ele.cat.codes) ], axis = 1)
    
    X = pd.concat([ X, df[ 'toss_winner' ] ], axis = 1)
    X = pd.concat([ X, df[ 'first_batting' ] ], axis = 1)

    X = pd.concat([ X, df[ 'team1_bat_score' ] ], axis = 1)
    X = pd.concat([ X, df[ 'team1_bowl_score' ] ], axis = 1)
    X = pd.concat([ X, df[ 'team2_bat_score' ] ], axis = 1)
    X = pd.concat([ X, df[ 'team2_bowl_score' ] ], axis = 1)

    X = pd.concat([ X, df[ 'team1_bat_score' ] ], axis = 1)
    X = pd.concat([ X, df[ 'team1_bowl_rank_score' ] ], axis = 1)
    X = pd.concat([ X, df[ 'team2_bat_score' ] ], axis = 1)
    X = pd.concat([ X, df[ 'team2_bowl_rank_score' ] ], axis = 1)
    
    for i in range(X.iloc[:5].shape[0]):
        X.iloc[i, 9] = (X.iloc[i, 9] * X.iloc[i, 9])
        X.iloc[i, 10] = (X.iloc[i, 10] * X.iloc[i, 10])
        X.iloc[i, 11] = (X.iloc[i, 11] * X.iloc[i, 11])
        X.iloc[i, 12] = (X.iloc[i, 12] * X.iloc[i, 12])

    return X, Y
