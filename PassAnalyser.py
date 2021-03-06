def Pass(matchId,HomeTeam,AwayTeam):
    import csv
    import json
    import pandas as pd
    datalist=[]
    file_name=str(matchId)+".json"
    with open('Statsbomb/data/events/'+file_name,errors='ignore') as data_file:
        data = json.load(data_file)
    df = pd.json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
    Passes = df.loc[df['type_name'] == 'Pass'].set_index('id')
    for i,Pass in Passes.iterrows():
        xBig=Pass['location'][0]
        yBig=Pass['location'][1]
        xEnd=Pass["pass_end_location"][0]
        yEnd=Pass["pass_end_location"][1]
        team_name=Pass['team_name']
        player_name=Pass['player_name']
        length=Pass["pass_length"]
        typeP=Pass["pass_height_name"]
        if(Pass['pass_cross']==True):
            CrOutcome=Pass["pass_outcome_name"]
            write=team_name+","+player_name+","+str(xBig)+","+str(yBig)+","+str(xEnd)+","+str(yEnd)+","+str(matchId)+","+typeP+","+"Cross"+","+str(CrOutcome)+","+str(length)
            datalist.append(write.split(','))        
        else:
            write=team_name+","+player_name+","+str(xBig)+","+str(yBig)+","+str(xEnd)+","+str(yEnd)+","+str(matchId)+","+typeP+","+"No Cross"+","+"NA"+","+str(length)
            datalist.append(write.split(','))
    with open("C:/Users/dibya/Desktop/Website/ALLPass.csv", "a",errors='ignore') as csv_file:
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
    Pass(matchId,home_team_name,away_team_name)

a=matchIdProv(43)
a.sort()
i=0
length=len(a)
for i in range(0,length):
    match=(a[i]) 
    parameterProvider(43,match)
    print(a[i])
