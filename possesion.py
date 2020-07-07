def possesion(matchId,HomeTeam,AwayTeam):
    import math
    import json
    import pandas as pd
    HomePosMin=[]
    AwayPosMin=[]
    file_name=str(matchId)+".json"
    with open('Statsbomb/data/events/'+file_name,errors='ignore') as data_file:
        data = json.load(data_file)
    df = pd.json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
    possesionsHome= df.loc[df['possession_team_name'] == str(HomeTeam)].set_index('id')
    for i,pos in possesionsHome.iterrows():
        HomePosMin.append(pos["minute"])
    possesionsAway= df.loc[df['possession_team_name'] == str(AwayTeam)].set_index('id')
    for i,pos in possesionsAway.iterrows():
        AwayPosMin.append(pos["minute"])
    home=(len(HomePosMin)/(len(AwayPosMin)+len(HomePosMin)))*100
    away=(len(AwayPosMin)/(len(AwayPosMin)+len(HomePosMin)))*100
    return home,away    
    #CroatiaPos=[x for x in CroatiaPos if str(x)!='nan']  
#(x,y)=possesion(8658,"France","Croatia")
def PassCount(matchId,HomeTeam,AwayTeam):
    import pandas as pd
    HomePassCount=0
    AwayPassCount=0
    import csv
    df = pd.read_csv("C:/Users/dibya/Desktop/Website/ALLpass.csv", encoding='latin-1')
    headers=["Team_Name","Player_Name","XcorBig","YcorBig","XcorEnd","YcorEnd","MatchId","Pass_Type","Cross","Cross_outcome","Pass_length"]
    df.columns=headers
    df.dropna(subset = ["Team_Name"], inplace=True)
    Pass=df.loc[:]
    #print(Pass)
    for i,plot in Pass.iterrows():
        #print(plot)
        if int(plot["MatchId"])==matchId:
            if plot["Team_Name"]==HomeTeam:
                HomePassCount=HomePassCount+1
            else:
                AwayPassCount=AwayPassCount+1
        elif int(plot["MatchId"])>matchId:
            break
    return HomePassCount,AwayPassCount
#(x,y)=PassCount(8658,"France","Croatia")    
def shotCount(matchId,HomeTeam,AwayTeam):
    import pandas as pd
    HomeShotCount=0
    AwayShotCount=0
    HomeSucShotCount=0
    AwaySucShotCount=0
    import csv
    df = pd.read_csv("C:/Users/dibya/Desktop/Website/ALLGoals.csv", encoding='latin-1')
    headers=["Team_Name","Player_Name","Xcor","Ycor","Time_stamp","Outcome","MatchId","Home_team","Away_team","Body_part"]
    df.columns=headers
    df.dropna(subset = ["Team_Name"], inplace=True)
    shot=df.loc[:]
    for i,plot in shot.iterrows():
        #print(plot)
        if int(plot["MatchId"])==matchId:
            if plot["Team_Name"]==HomeTeam:
                if plot["Outcome"]=="Goal" or plot["Outcome"]=="Saved" or plot["Outcome"]=="Post":
                    HomeSucShotCount=HomeSucShotCount+1
                    HomeShotCount=HomeShotCount+1
                else:
                    HomeShotCount=HomeShotCount+1    
            else:
                if plot["Outcome"]=="Goal" or plot["Outcome"]=="Saved" or plot["Outcome"]=="Post":
                    AwaySucShotCount=AwaySucShotCount+1
                    AwayShotCount=AwayShotCount+1
                else:
                    AwayShotCount=AwayShotCount+1    

        elif int(plot["MatchId"])>matchId:
            break
    return HomeShotCount,AwayShotCount,HomeSucShotCount,AwaySucShotCount
#(a,b,c,d)=shotCount(8658,"France","Croatia")
#print(a)
#print(b)
#print(c)
#print(d)
#print(x)
#print(y)
def matchResultriter(compId):
    import json
    import csv
    datalist=[]
    describe_text = "home_team_name,away_team_name,home_score,away_score,match_date,kick_off,match_id_required,competition_stage_name,Home_Possesion,Away_Posession,Home_Shots,Away_Shot,Home_on_target,Away_away_on_target,Home_pass,Away_pass"
    datalist.append(describe_text.split(','))
    with open('Statsbomb/data/matches/'+str(compId)+'/3.json') as f:
        matches = json.load(f)
    for match in matches:
        home_team_name=match['home_team']['home_team_name']
        away_team_name=match['away_team']['away_team_name']
        home_score=match['home_score']
        away_score=match['away_score']
        match_id_required = match['match_id']
        (x,y)=possesion(match_id_required,home_team_name,away_team_name)
        (a,b,c,d)=shotCount(match_id_required,home_team_name,away_team_name)
        (g,h)=PassCount(match_id_required,home_team_name,away_team_name)
        describe_text = home_team_name+","+away_team_name+","+ str(home_score) +","+ str(away_score)+","+str(match['match_date'])+","+str(match['kick_off'])+","+str(match_id_required)+","+match["competition_stage"]["name"]+","+str(x)+","+str(y)+","+str(a)+","+str(b)+","+str(c)+","+str(d)+","+str(g)+","+str(h)
        datalist.append(describe_text.split(','))
        print(match_id_required)
    with open("C:/Users/dibya/Desktop/Website/Match"+str(compId)+".csv", "a") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in datalist:
                writer.writerow(line) 
matchResultriter(43)