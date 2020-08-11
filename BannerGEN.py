def BannerScraper(webpage):
    import bs4
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import csv
    i=0
    j=0
    MatchUnclean = [] #stores the unclean match data
    Match=[]#stores the clean match data
    Scores=[]#stores the scores of the matches
    Datalist=[]#file writing variable
    headers = "Home_Team,Home_Score,Away_Team,Away_Score,MatchDay"
    Datalist.append(headers.split(','))
    #opening the webpage
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webPage = requests.get(webpage, headers = headers).text
    soup = BeautifulSoup(webPage, 'lxml')
    
    #since the team names are in  'a' tags with class vereinprofil_tooltip we extract all the tags and put them in a datalist which also have unclean data
    #after cleaning the data we store it in the match data set
    
    for tag in soup.find_all('a',class_ = 'vereinprofil_tooltip'):
        MatchUnclean.append(tag.text.strip())
    for Name in MatchUnclean:
        if Name!='':
            Match.append(Name)
    
    
    #since the team names are in  'a' tags with class ergebnis-link we extract all the tags and put them in a datalist
    for tag in soup.find_all('a',class_ = 'ergebnis-link'):
        Scores.append(tag.text.strip())

    #we create a dataset by splitting the score and creating a dataset with one match in one row
    while(j<len(Scores)):
        HT=i
        AT=i+1
        if len(Scores)==306:
            write=Match[HT]+","+Scores[j].split(':')[0]+","+Match[AT]+","+Scores[j].split(':')[1]+","+str(int((j/9))+1)
        else:
            write=Match[HT]+","+Scores[j].split(':')[0]+","+Match[AT]+","+Scores[j].split(':')[1]+","+str(int((j/10))+1)
        Datalist.append(write.split(','))
        i=i+2
        j=j+1
    #writing the data in a csv file 
    with open("Data/"+str(webpage.split('/')[3]+webpage.split('/')[-1])+".csv", "a",errors='ignore') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in Datalist:
            writer.writerow(line)
    csv_file.close()
#webpages to scrape
webpages=['https://www.transfermarkt.co.in/laliga/gesamtspielplan/wettbewerb/ES1/saison_id/2019','https://www.transfermarkt.co.in/premier-league/gesamtspielplan/wettbewerb/GB1/saison_id/2019','https://www.transfermarkt.co.in/serie-a/gesamtspielplan/wettbewerb/IT1/saison_id/2019','https://www.transfermarkt.co.in/bundesliga/gesamtspielplan/wettbewerb/L1/saison_id/2019','https://www.transfermarkt.co.in/ligue-1/gesamtspielplan/wettbewerb/FR1/saison_id/2019']
for webpage in webpages: 
    BannerScraper(webpage)