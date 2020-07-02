def createPitch(length,width, unity,linecolor):
    """
    Created on Wed Mar 25 17:32:00 2020

    @author: davsu428
    """
    import matplotlib.pyplot as plt
    from matplotlib.patches import Arc
    if unity == "yards":
        #check boundaries again
        if length <= 95:
            return(str("Didn't you mean meters as unity?"))
        elif length >= 131 or width >= 101:
            return(str("Field dimensions are too big. Maximum length is 130, maximum width is 100"))
        #Run program if unity and boundaries are accepted
        else:
            #Create figure
            fig=plt.figure()
            #fig.set_size_inches(7, 5)
            ax=fig.add_subplot(1,1,1)
           
            #Pitch Outline & Centre Line
            plt.plot([0,0],[0,width], color=linecolor)
            plt.plot([0,length],[width,width], color=linecolor)
            plt.plot([length,length],[width,0], color=linecolor)
            plt.plot([length,0],[0,0], color=linecolor)
            plt.plot([length/2,length/2],[0,width], color=linecolor)
            
            #Left Penalty Area
            plt.plot([18 ,18],[(width/2 +18),(width/2-18)],color=linecolor)
            plt.plot([0,18],[(width/2 +18),(width/2 +18)],color=linecolor)
            plt.plot([18,0],[(width/2 -18),(width/2 -18)],color=linecolor)
            
            #Right Penalty Area
            plt.plot([(length-18),length],[(width/2 +18),(width/2 +18)],color=linecolor)
            plt.plot([(length-18), (length-18)],[(width/2 +18),(width/2-18)],color=linecolor)
            plt.plot([(length-18),length],[(width/2 -18),(width/2 -18)],color=linecolor)
            
            #Left 6-yard Box
            plt.plot([0,6],[(width/2+7.32/2+6),(width/2+7.32/2+6)],color=linecolor)
            plt.plot([6,6],[(width/2+7.32/2+6),(width/2-7.32/2-6)],color=linecolor)
            plt.plot([6,0],[(width/2-7.32/2-6),(width/2-7.32/2-6)],color=linecolor)
            
            #Right 6-yard Box
            plt.plot([length,length-6],[(width/2+7.32/2+6),(width/2+7.32/2+6)],color=linecolor)
            plt.plot([length-6,length-6],[(width/2+7.32/2+6),width/2-7.32/2-6],color=linecolor)
            plt.plot([length-6,length],[(width/2-7.32/2-6),width/2-7.32/2-6],color=linecolor)
            
            #Prepare Circles; 10 yards distance. penalty on 12 yards
            centreCircle = plt.Circle((length/2,width/2),10,color=linecolor,fill=False)
            centreSpot = plt.Circle((length/2,width/2),0.8,color=linecolor)
            leftPenSpot = plt.Circle((12,width/2),0.8,color=linecolor)
            rightPenSpot = plt.Circle((length-12,width/2),0.8,color=linecolor)
            
            #Draw Circles
            ax.add_patch(centreCircle)
            ax.add_patch(centreSpot)
            ax.add_patch(leftPenSpot)
            ax.add_patch(rightPenSpot)
            
            #Prepare Arcs
            leftArc = Arc((11,width/2),height=20,width=20,angle=0,theta1=312,theta2=48,color=linecolor)
            rightArc = Arc((length-11,width/2),height=20,width=20,angle=0,theta1=130,theta2=230,color=linecolor)
            
            #Draw Arcs
            ax.add_patch(leftArc)
            ax.add_patch(rightArc)
                
    #Tidy Axes
    plt.axis('off')
    
    return fig,ax
def plotter(fileName):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    pitchLengthX=120
    pitchWidthY=80
    (fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','black')
    file_Name=str(fileName)+".csv"
    df = pd.read_csv("C:/Users/dibya/Desktop/Website/"+file_Name, encoding='latin-1')
    headers=["Team_Name","Player_Name","Xcor","Ycor","Time_stamp","Outcome","MatchId","Home_team","Away_team"]
    df.columns=headers
    df.dropna(subset = ["Team_Name"], inplace=True)
    cordinate=df.loc[:]
    #print(cordinate['Xcor'])
    for i,plot in cordinate.iterrows():
        #print(plot)
        if plot["Outcome"]=="Goal":
            shotCircle=plt.Circle((pitchLengthX-int(plot['Xcor']),int(plot['Ycor'])),.5,color="red")
            shotCircle.set_alpha(.3)
        elif plot["Outcome"]=="Own Goal":
            shotCircle=plt.Circle((int(plot['Xcor']),(pitchWidthY- int(plot['Ycor']))),.5,color="red")
            shotCircle.set_alpha(.3)
        else:
            shotCircle=plt.Circle((pitchLengthX-int(plot['Xcor']),int(plot['Ycor'])),.75,color="blue")
            shotCircle.set_alpha(.3)
        ax.add_patch(shotCircle)
    fig.set_size_inches(10, 7)
    fig.savefig('c:/Users/dibya/Documents/WCGoals.png', dpi=100) 
    plt.show()
plotter("Goals")
#plotter("OnlyGoals")    
