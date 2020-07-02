def shotPlotter(matchId,home_team_name,away_team_name):
    import csv
    import json
    import pandas as pd
    datalist=[]
    file_name=str(matchId)+".json"
    with open('Statsbomb/data/events/'+file_name,errors='ignore') as data_file:
        data = json.load(data_file)
    df = pd.json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
    shots = df.loc[df['type_name'] == 'Shot'].set_index('id')
    OwnGoals = df.loc[df['type_name'] == 'Own Goal Against'].set_index('id')
    write ="Team_Name,Player_Name,Xcor,Ycor,TimeStamp,Outcome,MatchId,Home_team,Away_team"
    datalist.append(write.split(','))  
    for i,shot in shots.iterrows():
        x=shot['location'][0]
        y=shot['location'][1]
        goal=shot['shot_outcome_name']=='Goal'
        team_name=shot['team_name']
        player_name=shot['player_name']
        time_stamp=str(shot['minute'])+":"+str(shot['second'])
        if goal:
            write=team_name+","+player_name+","+str(x)+","+str(y)+","+time_stamp+","+"Goal"+","+str(matchId)+","+home_team_name+","+away_team_name
            datalist.append(write.split(','))        
        else:
            write=team_name+","+player_name+","+str(x)+","+str(y)+","+time_stamp+","+"No Goal"+","+str(matchId)+","+home_team_name+","+away_team_name
            datalist.append(write.split(','))        
    #with open("C:/Users/dibya/Desktop/Website/Shotsin"+str(matchId)+".csv", "a",errors='ignore') as csv_file:
    #with open("C:/Users/dibya/Desktop/Website/OnlyGoals.csv", "a",errors='ignore') as csv_file:
    for i,Owngoal in OwnGoals.iterrows():
        x=Owngoal['location'][0]
        y=Owngoal['location'][1]
        team_name=Owngoal['team_name']
        player_name=Owngoal['player_name']
        time_stamp=str(shot['minute'])+":"+str(shot['second'])
        write=team_name+","+player_name+","+str(x)+","+str(y)+","+time_stamp+","+"Own Goal"+","+str(matchId)+","+home_team_name+","+away_team_name
        datalist.append(write.split(','))
    with open("C:/Users/dibya/Desktop/Website/ALLGoals.csv", "a",errors='ignore') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in datalist:
            writer.writerow(line)    
def matchResultriter(compId):
    import json
    import csv
    datalist=[]
    describe_text = "home_team_name,away_team_name,home_score,away_score,match_date,kick_off,match_id_required,competition_stage_name"
    datalist.append(describe_text.split(','))
    with open('Statsbomb/data/matches/'+str(compId)+'/3.json') as f:
        matches = json.load(f)
    for match in matches:
        home_team_name=match['home_team']['home_team_name']
        away_team_name=match['away_team']['away_team_name']
        home_score=match['home_score']
        away_score=match['away_score']
        match_id_required = match['match_id']
        describe_text = home_team_name+","+away_team_name+","+ str(home_score) +","+ str(away_score)+","+str(match['match_date'])+","+str(match['kick_off'])+","+str(match_id_required)+","+match["competition_stage"]["name"]
        datalist.append(describe_text.split(','))
    with open("C:/Users/dibya/Desktop/Website/Match"+str(compId)+".csv", "a") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in datalist:
                writer.writerow(line) 
def matchIdProv(compId):
    import json
    import csv
    with open('Statsbomb/data/matches/'+str(compId)+'/3.json') as f:
        matches = json.load(f)
        matchId=[]
    for match in matches:
        match_id_required = match['match_id']
        matchId.append(match_id_required)
    return matchId
def parameterProvider(compId,matchId):
    import json
    with open('Statsbomb/data/matches/'+str(compId)+'/3.json',errors= 'ignore') as f:
        matches = json.load(f)
    for match in matches:
        if(match['match_id']==matchId):
            home_team_name=match['home_team']['home_team_name']
            away_team_name=match['away_team']['away_team_name']
    shotPlotter(matchId,home_team_name,away_team_name)

a=matchIdProv(43)
a.sort()
i=0
length=len(a)
for i in range(0,length):
    match=(a[i]) 
    parameterProvider(43,match)
    print(a[i])

matchResultriter(43)

#matchIDProv(43)
#shotPlotter(8658,"France","Croatia")
