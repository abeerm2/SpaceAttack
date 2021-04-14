#imporitng required functions 
import pygame 
pygame.init() #initalizing pygame 
import random
import os
from time import time

SIZE=(width,height) = (1000,700) #size of screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20) #mkaing window appear in the same window 

#FONTS FOR TEXT 
fontHello = pygame.font.SysFont("Helvetica Neue",30) #font used for the main menu 
fontPoints = pygame.font.SysFont("Helvetica Neue",40)
fontword = pygame.font.SysFont("Helvetica Neue",30) # main font used on final page
fontpower = pygame.font.SysFont("Helvetica Neue",30)
fonttext = pygame.font.SysFont("Helvetica Neue",25)
fonttext2 = pygame.font.SysFont("Helvetica Neue",23)

#COLOURS used throughout the game#
YELLOW=(255, 230, 0) 
BLACK=(0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (247, 194, 69)
PURPLE = (152, 95, 237)
PINK = (219, 140, 186)

text3= 0
finalMessage = ""
screen = pygame.display.set_mode(SIZE) #setting pygame window 
screen.fill(WHITE) 

#STATES#
STATE_MAIN = 1 #home screen 
STATE_GAME = 2 #playing the game screen
STATE_INSTR = 3 #help menu
STATE_FINISH = 4 #losing screen
STATE_STORY = 5 #Story page that will be played before the start of the game 
STATE_HIGHSCORE = 6 
state = STATE_MAIN #starting state of game
# Home Screen variables for play and instructions button
wording1 = pygame.Rect(295, 368, 100, 50)#play game 
wording2 = pygame.Rect(590, 368, 100, 50)#quit 
wording5 = pygame.Rect(840, 45, 90, 25)#highscore
testoutline1 = pygame.Rect (240,323,220,120) #outline for boxes 
testoutline2 = pygame.Rect (540,323,220,120)
testoutline5 = pygame.Rect (790,20,200,70)
testRect1 = pygame.Rect(250, 333, 200, 100) #play game button
testRect2 = pygame.Rect(550, 333, 200, 100) # instructions button 
testRect3 = pygame.Rect(800, 30, 180, 50) # highscores button 
outlineList = [testoutline1,testoutline2,testoutline5]
wordList = [wording1,wording2,wording5]
rectList = [testRect1, testRect2,testRect3]
titleList = ["Play Game", "Instructions", "HighScores"]

#MOTIONS 
running =True #would need to be switched to false when game is done 
movingRight=False
movingDown=False
movingUp=False
movingLeft=False 
shootingball = False #if true then can shoot laser/balls

# starting place of spaceship 
herox = 500 #starting x 
heroy = 600#starting y 
heroRadius = 20 #size of spaceship is moving
heroSpeed = 7 #speed at which spaceship is moving 

gameTime = 0 #the amount of time the game is runnign variable 

#bullet variables
bulletxList = [] #x list of bullet
bulletyList = [] #ylist of bullet 
dig = 0 #used for deleting the bullet when reaches top of screen 

# IMAGES##
titlePic = pygame.image.load("abeerspaceship.png") #SPACESHIP
FirePic = pygame.image.load("explosion.png") #EXPLOSION WHEN e waste AND SPACESHIP COLLIDE 
backgroundPic = pygame.image.load("spacebackground.png") #background of entire game 
obstaclespaceship = pygame.image.load("abeerufo.png") #these are the sapceships whcih pass by every 1000 points 
liveImage = pygame.image.load("abeerufo.png")
mainImage = pygame.image.load("mainmenubackground.png")
winningImage =  pygame.image.load("autowin1.png") #if this is hit then it will cause an automatic win
arrowImage = pygame.image.load("arrowkeys.png") # all arrow keys image 
arrowright = pygame.image.load("arrowright.png")
arrowup = pygame.image.load("arrowup.png")
arrowdown = pygame.image.load("arrowdown.png")
arrowleft = pygame.image.load("arrowleft.png")
spacebar = pygame.image.load("spacebar.png")
titleBack = pygame.image.load("title.png")
aKey = pygame.image.load("lettera.png")
storyImage = pygame.image.load("story.png")
highscoreImage = pygame.image.load("highscores.png")
blockx = 0 #x defined for falling e waste
blocky = 0 #y defined for falling e waste

variable = 0 #bulletx
my = 0 #bullety 

obstaclexList= [] #position x for obstacle (ewaste)
obstacleyList =[] #position y for obstacle (ewaste)
imageList = [pygame.image.load("cellphone.png"),pygame.image.load("cellphone2.png"),pygame.image.load("oldtv.png")] #ewaste pictures 
obstacleSpeed = 5 #speed which they pass on the screen 
droppingSpeed = 1000 #speed which they are released (new one is created) 

itemList = [] #empty list which will be used to contain a random order of ewaste meaning it will ebr andomized in whcih ones are bieng displayed 
pic = () #empty variable which will be used to randomize the pictures being put on screen

x = 0 # x value which will alllow the spaceship obstacle to move across the screen 
spaceshipxList = [] # x position of the spaceship obstacle 
spaceshipyList = []# y position of the spaceship obstacle 
amount = 0 #this will increase and add more spaceships 
spaceSpeed = 5 #spaceship obstacel speed 

# AUDIO USED
endAudio = pygame.mixer.Sound("ade.wav") #that is very much adequate when u lose 
shootingAudio = pygame.mixer.Sound ("shootsound.wav") #everytime u hit the spacebar 
explosionAudio = pygame.mixer.Sound ("spaceexplosion.wav")#this is when an ewaste object and the main hero ship collide 
shipAudio = pygame.mixer.Sound ("shipexplosion.wav")#when the hero ship hits the obstacle ship causign automatic loss 
winningAudio = pygame.mixer.Sound ("winningAudio.wav") #winnign audio 
introAudio = pygame.mixer.Sound ("intromusic.wav") # intromusic of game 
storyAudio = pygame.mixer.Sound ("storyaudio.wav") # intromusic of game 
# RECTANGELS FOR END SCREEN
rectangle3 = pygame.Rect(250, 333, 200, 100) #play again
rectangle4 = pygame.Rect(550, 333, 200, 100) #quit
wording3 = pygame.Rect(310, 368, 100, 50)#play game 
wording4 = pygame.Rect(620, 368, 100, 50)#quit 
wording6 = pygame.Rect(825, 45, 90, 25) #highscore
testoutline3 = pygame.Rect (240,323,220,120) #outline for boxes 
testoutline4 = pygame.Rect (540,323,220,120)
outlineList2 = [testoutline3,testoutline4,testoutline5]
wordList2 = [wording3,wording4,wording6]
rectList2 = [rectangle3,rectangle4,testRect3]
titleList2 = ["REPLAY","QUIT", "HIGHSCORES"] #titles 

#used for points system
pointTime = 0  
points = 0  #points that are gathered from shootingn objects 
newPoints = 0 #amount of points which will be displayed on screen 
count =0 # life lost counter 
totalLives = 3 # total amount of lives possible 
# coordinates of where images for life system will be lcoated 
livexList = [] 
liveyList = [] 

number = 1000 # increases in difficulty every 1000 points 
LastTime = pygame.time.get_ticks() #used for the speed at which objects are dropped 
ywin = 0 # this is for the automatic win robot 
winningChance = True # if this is true it allows the robot to drop 
winNum = 6000 #the robot drops at 6000 points 
xwin = random.randint (120,700) # this is the random x at which the robot will drop 
numBef = 0 #this is used to make winning chance true again 

## SPECIAL POWER VARIABLES 
slowingPower = False #original state of special power 
number1 = 4000 # this is when the super power shows up 
slowmotion = False #slowmotion is what is being used so if true then will slow down obstacles 
seconds = 0 # is seconds equals 15 slowmotion = done 
pointTimer = pygame.time.get_ticks () # used to calc the number of seconds which will have passed (15)
currentSpeed = 0 # this is being used to save the speed at which the current stte of the program is so aftter 15 seconds it will go back to this 

adder = 0 
yval2 = 700 
xval = 0 #spaceship object x value 
spaceship = True #original state of spaceship 
yval1 = 200 
ufo2Time = pygame.time.get_ticks() #when the spaceship is released on main screen 
ufoTime = 0 
dataFile = open ("ABEERHIGHSCORE.DAT","r") #highscore datafile 
snumber = [] #empty highscore list 

# WRITING INTO FILE VARIABLES 
output1 = ""
wordy = 200
y4=0
ssizeList =[(450,240,100,100),(450,280,100,100),(450,320,100,100),(450,360,100,100),(450,400,100,100)] #top five highscore spots 
# Shooting a bullet/laser thing after hitting spacebar 

def shootball ():
    global dig,blockx,blocky,variable,my,obstaclexList,obstacleyList,itemList,obstaclePic,pic,obstacleSpeed,pointTime,points,spaceshipxList,spaceshipyList,obstaclespaceship,state,liveImage,finalMessage,xwin,ywin1,xwin,winningChance
    
    
    #if bullet is less than 25 on y axis it is deleted 
    for i in range (len(bulletxList)-1,-1,-1): 
        dig = 0 
        if bulletyList[dig] < 25 :
            del bulletyList[dig] #deleting the bullets if less than 25 
            del bulletxList[dig]
            
        #while it is not less than 25 it sends the bullet and travels accross screen
        else:   
            bulletyList[i]-=10   
            my = bulletyList[i]
            variable= bulletxList[i]+45
            
            pygame.draw.rect(screen, RED, (variable, my,  10 , 25))
            
            # this  is if you hit another spaceship which flies by periodically throughout the game 
            for l in range (len(spaceshipxList)-1,-1,-1):
                x = spaceshipxList[l]
                y = spaceshipyList[l]  
                rectangle = pygame.Rect(x, y,55,60)
                bullet =  pygame.Rect(variable, my,  10 , 25)
                if rectangle.colliderect(bullet) == True: # if bullet touches the obstacle then deletes the object and bullet 
                    shipAudio.play() #crash audio 
                    state= STATE_FINISH #gameover cause automatic death
                    finalMessage = "YOU HIT A SPACESHIP! YOU LOSE!" #sends this as final message adn sends to final screen 
            
            #this is if bullet and object collides then it deletes both the bullet and object 
            for j in range (len(obstaclexList)-1,-1,-1):
                blockx = obstaclexList[j]
                blocky = obstacleyList[j]            
                if blockx-15 <= variable <= blockx+60 and my- 25<=blocky: # if bullet touches the obstacle then deletes the object and bullet 
                    del bulletyList[i]
                    del bulletxList[i] #deletes bullet 
                    del obstaclexList[j] #deletes object
                    del obstacleyList[j] 
                    del itemList[j] # it also deletes the item from the randomized list from which it is printing 
                    points+=200   #u gain 200 points when you hit one of these objects 

    # THIS IS WHERE THE OBSTACLES ARE PRINTING 
    for i in range (len(obstaclexList)-1,-1,-1):
        blockx = obstaclexList[i]
        blocky = obstacleyList[i]
        obstacleyList[i]+=obstacleSpeed
        
        # drawing the falling images 
        obstaclePic = itemList[i] #grabs the image from randomized image list, which loads the image 
        obstaclePic = pygame.transform.scale(obstaclePic,(60,40)) #sizing image 
        screen.blit(obstaclePic,pygame.Rect(blockx, blocky,55,60)) #drawing image             
        
        if blocky>700: #if the image is less than 700 on the y axis (u missed it) it deletes the image and item from item list 
            LastTime = 0 
            del obstaclexList[i]
            del obstacleyList[i]  
            del itemList[i] 
            points-=5 #lose five points when missed 
        
            
    # Drawing the spaceships which come in every 1000 points it increases in amount everytime 
    for i in range (len(spaceshipxList)-1,-1,-1):
        x = spaceshipxList [i]
        y = spaceshipyList[i]
        spaceshipxList[i]+=spaceSpeed
        obstaclespaceship = pygame.transform.scale(obstaclespaceship,(50,30))
        screen.blit(obstaclespaceship,pygame.Rect(x, y,55,60)) 
        
        #If spaceship obstacle reaches right sdie of the screen it deletes
        if x >1000:
            del spaceshipxList [i]
            del spaceshipyList[i]
    #This is drawing the three lives in the corner 
    for k in range (len (livexList)-1,-1,-1):
        livex = livexList[k]
        livey = liveyList [k]
        liveImage = pygame.transform.scale(liveImage,(30,30))
        screen.blit(liveImage,pygame.Rect(livex, livey,55,60))  
        

# THIS creating the x and y list of the spaceship images in the corner 
def lives ():
    global adder,totalLives
    for i in range (totalLives):
        liveX = 880 + adder 
        liveY = 30
        livexList.append(liveX)
        liveyList.append (liveY)
        adder += 40
        
# THIS IS CHECKING IF THE OBJECT AND THE HERO COLLIDE, DELETING THE ITEM, THE X AND Y OF THE OBSTACLES AND DELETING A LIFE EACH TIME
def check ():
    global blockx,blocky,variable,my,bulletyList,bulletxList,dig,i,FirePic,LastTime2,count,itemList
  
    for i in range (len(obstaclexList)-1,-1,-1):
        blockx = obstaclexList[i]
        blocky = obstacleyList[i]        

    # IF THE falling obstacles and hero collide deletes the required items 
        if blockx>herox-30 and blockx<herox+80 and blocky>heroy-20 and blocky<heroy+80:
            del obstaclexList[i]
            del obstacleyList[i]  
            del itemList[i]
            del livexList[i]
            del liveyList[i]
            ey = heroy-60
            FirePic = pygame.transform.scale(FirePic,(100,100))
            screen.blit(FirePic,pygame.Rect(herox, ey,55,60))    
            count+=1
            explosionAudio.play() #plays proper audio 

#CREATING THE RANDOM LOCATIONS OF THE OBSTACLES AND THE RANDOMIZED THE ITEMLIST WHICH CHANGES THE OBJECTS COMING DOWN 
def obstacle ():
    global obstaclexList, obstacleyList,pic
    
    blockx = random.randint(0,width-120)
    blocky = 25
    obstaclexList.append(blockx)
    obstacleyList.append(blocky)
    pic = random.choice (imageList)
    itemList.append (pic)
  
    
# THIS DEFINITION IS TO RESET ALL MY VARIABLES AFTER SOMEONE HITS REPLAY 
def setup():
    global bulletxList, bulletyList,obstaclexList, obstacleyList, heroSpeed,droppingSpeed, newPoints,points,obstacleSpeed,itemList,count,pointTime,herox,heroy,spaceshipxList,spaceshipyLisy,amount,number,spaceSpeed,adder,livexList,liveyList,winNum,winningChance,ywin,xwin,numBef,ywin1,slowingPower,number1,slowmotion,currentPoint,newerPoints,seconds,currentSpeed,yval2,wordy,y4

    bulletxList = []
    bulletyList =[]
    count = 0 
    itemList = []
    obstaclexList = []
    obstacleyList = []
    heroSpeed = 7 #speed at which spaceship is moving 
    newPoints = 0 
    herox = 500 
    heroy = 600    
    points = 0 
    obstacleSpeed = 5
    droppingSpeed = 1000    
    pointTime = 0 
    amount = 0
    spaceshipxList =[]
    spaceshipyList = []
    newPoints = 0 
    number = 1000
    spaceSpeed = 7
    adder = 0
    xval = 0 
    spaceship = True 
    yval1 = 200
    ufo2Time = pygame.time.get_ticks() 
    ufoTime = 0     
    livexList =[]
    liveyList =[]
    lives()
    finalMessage =""
    ywin = 0 
    ywin1 = 0
    winningChance = True
    winNum = 6000
    xwin = random.randint (120,700)
    numBef = 0     
    slowingPower = False 
    number1 = 4000
    slowmotion = False 
    seconds = 0 
    pointTimer = pygame.time.get_ticks ()
    currentSpeed = 0     
    yval2 = 700
    wordy = 200
    y4=0    
    
# CREATING the x and y list for the spaceship on the MAIN SCREEN 
def drawufo():
    global x,spaceshipxList,spaceshipyList,obstaclespaceship, amount 
    for i in range (amount):
        x = 0 
        y = random.randint(0,400)
        spaceshipxList.append(x)
        spaceshipyList.append (y)
    
    
    
# this creates the x and y list of the bullet 
def addBullet(mx,my):
    global bulletxList, bulletyList

    xStart = mx
    bulletxList.append(xStart)
    yStart= my
    bulletyList.append(yStart)
    


# if state = STATE_GAME then goes to this definition 
def playGame(screen, mx1, my1, button):
    global state, herox, heroy, heroRadius,my,shootingball, titlePic,variable,blockx,blocky,blockwidth,LastTime,droppingSpeed,pointTime,points,heroSpeed,obstacleSpeed,number,backgroundPic,spaceshipxList,spaceshipyList,obstaclespaceship,amount,spaceSpeed,text3,finalMessage,winningImage,winNum,winningChance,ywin,xwin,numBef,FirePic,slowingPower,number1,slowmotion,currentPoint,newerPoints,seconds,currentSpeed  
   
    # SETTING MOVEMENT ADN HOW MUCH HERO WILL MOVE BY 
    if movingRight == True and herox + heroRadius+60 < width:
        herox+=heroSpeed

    elif movingLeft== True and herox - heroRadius +40 > 0 :
        herox-=heroSpeed

    elif movingDown == True and heroy + heroRadius+60< height:
        heroy+=heroSpeed

    elif movingUp== True and heroy - heroRadius+60  > 600:
        heroy-=heroSpeed
        
    # drawing the background picture on the screen
    backgroundPic = pygame.transform.scale(backgroundPic,(1000, 700))
    screen.blit(backgroundPic,pygame.Rect(0, 0,1000,700))   
    #drawing THE HERO
    titlePic = pygame.transform.scale(titlePic,(100,100))
    screen.blit(titlePic,pygame.Rect(herox, heroy,55,60))
    # TURNING THIS INTO A RECT TO TEST COLLISION
    spaceshipImage = pygame.Rect(herox, heroy,55,60)
    shootball() #shootbal is running making bullets and checking collision 
    check()#checking for the hero and obstacles to collide 

    gameTime = pygame.time.get_ticks () #this is going to be used in allowing an object to be dropped at dropping speed which starts at 1 second 
    if gameTime - LastTime > droppingSpeed : #checking if one second has passed
        LastTime = pygame.time.get_ticks() #resets last time 
        obstacle() #creates x and y for obstacle allowing them to be drawn 
        
    pointTime = pygame.time.get_ticks() #timing hoe long has passed
    newPoints = (pygame.time.get_ticks() - pointTime) // 1000 + points #creates the amount of points recieved 
   
    if newPoints >= number : #if the points supersedes 1000 it increases the speed at whcih things are moving 
        amount +=1 
        drawufo()
        if droppingSpeed == 0:
            state = STATE_FINISH 
            finalMessage = "You WON!"
        else:
            droppingSpeed-=50
        heroSpeed+=1
        obstacleSpeed +=1
        number+=1000 #increases number by 1000 so the speed and difficulty increases every 1000 points 
        spaceSpeed+=1
    
    
    if newPoints>=number1 : # if  number of points is greater than or equal to 4000 then special power starts 
        slowingPower = True 
    if slowingPower == True: # prints this 
        insText = fontpower.render("Hit \"a\" Key to access slow power",1,RED)
        screen.blit (insText,(600, 0, 100, 10))
        number1 +=1000    
    if slowmotion == True :# if slowmotion is true then outputs to the user that they can use it and then changes the speed  
        obstacleSpeed = 2 
        seconds= (pygame.time.get_ticks()-pointTimer)/1000
        if seconds > 10 : #changes speed for 10 seconds and then returns to speed before slow power
            slowmotion = False
            obstacleSpeed = currentSpeed #returning to original spee d

  
    text3 = newPoints #saving new points so once dead can be used to display number of points recieved 
    text1 = fontPoints.render("Points: " + str(newPoints) , 1, YELLOW)	 #printing the amount of points on screen

    # this IS THE AUTOMATIC WIN ROBOT FALLING IF THIS GETS HIT THEN WILL BE AUTOMATIC WIN 
    if newPoints >= winNum and winningChance == True : #if your points is greater than or equal to 6000 then u have opportunity for automatic win
        numBef = winNum #saves winnum before it increases by 2000
        ywin+= 10
        ywin1 = 0 
        winningImage = pygame.transform.scale(winningImage,(120,120)) #winning image is robot, draws robot 
        screen.blit(winningImage,pygame.Rect(xwin,ywin1+ywin ,70,90))  
        rectangle = pygame.Rect(xwin,ywin1+ywin ,70,90) #saving image coordinates to be used in collision testing 
        for j in range (len(bulletxList)-1,-1,-1): #if bullet collides with robot then u win 
            blockx = bulletxList[j]
            blocky = bulletyList[j]    
            bullet = pygame.Rect(blockx, blocky,  10 , 25)
            if rectangle.colliderect (bullet) == True:
                state = STATE_FINISH
                finalMessage = "YOU HIT THE E-WASTE ROBOT, You WIN! I hope you FEEL proud" #sent to end game screen 
    
        if rectangle.colliderect(spaceshipImage): #checking if the hero and robot collide, if they do then automatic loss
            FirePic = pygame.transform.scale(FirePic,(100,100))
            screen.blit(FirePic,pygame.Rect(herox, heroy-60,55,60))  
            explosionAudio.play()
            state = STATE_FINISH 
            finalMessage = "THE E-WASTE ROBOT DESTROYED YOUR SHIP, YOU LOSE!" #u lost and sent to end game screen 
                
        
        if ywin > 710: #if the robot reaches bottom of screen then turns winning chance to false and does not drop robot 
            winningChance = False 
            ywin = 0 
            ywin1 = 0
            winNum +=2000
            
            
            
    if newPoints >= numBef+2000: #if new points if the newnum before +2000 then does it again, so oppportunity for automatic win every 2000 points 
        winningChance = True 
        xwin = random.randint (120,700)
    screen.blit(text1, (width//3, 0, 100, 10))


# DRAWING END GAME SCREEN 
def endScreen (screen, mx, my, button):
    global state,count,running,newPoints,endAudio,text3,mainImage,finalMessage
    mainImage = pygame.transform.scale(mainImage,(1000,700))
    screen.blit(mainImage,pygame.Rect(0, 0,width,height))         
    for i in range(len(rectList2)):
        rectangle2 = rectList2[i] #using list to print each 
        words2 = wordList2[i] # words list which will print on to each corresponding square
        outline2 = outlineList2[i] # creating an outline on the box 
        pygame.draw.rect(screen, RED, rectangle2) # colouring int hte square snad drwating thme 
        pygame.draw.rect(screen, RED, outline2,1) #orange outline 
        text2 = fontword.render(titleList2[i] , 1, YELLOW)	#writing the words 
        pointText = fontPoints.render(("Points: %i"%text3), 1, RED)
        finalText = fontPoints.render(finalMessage,1,YELLOW)
        #FIGURING OUT TH EPOSITION AND LOCATION OF THE WORDS DEPENDING ON TEXT3 AND WHAT OUTCOME U RECEIVED ALSO CHOOSES AUDIO DEPENDING ON OUTCOME
        if finalMessage == "YOU HIT A SPACESHIP! YOU LOSE!":
            screen.blit(finalText, (280, 200, 100, 10))
            endAudio.play()
        elif finalMessage == "You WON!":
            screen.blit(finalText, (440, 200, 100, 10))
            winningAudio.play()
        elif finalMessage == "YOU HIT THE E-WASTE ROBOT, You WIN! I hope you FEEL proud" :
            screen.blit(finalText, (70, 200, 100, 10))
            winningAudio.play()        
        elif finalMessage == "THE E-WASTE ROBOT DESTROYED YOUR SHIP, YOU LOSE!": 
            screen.blit(finalText, (100, 200, 100, 10))
            endAudio.play()
        else:
            screen.blit(finalText, (440, 200, 100, 10))
            endAudio.play()
        #FIGURING OUT TH EPOSITION AND LOCATION OF THE WORDS DEPENDING ON TEXT3 AND WHAT OUTCOME U RECEIVED.^ 
        screen.blit(pointText, (425, height//3, 100, 10))   
        screen.blit(text2, words2)#blitting the word     
        if rectangle2.collidepoint(mx, my) and button == 1:
            if i == 0:
                state = STATE_GAME #playing the game screen 
            elif i == 1:
                running = False 
            else:
                state = STATE_HIGHSCORE 
        if rectangle2.collidepoint(mx, my): # if collides with remove
            pygame.draw.rect(screen, RED, rectangle2,4)  #prints a black box to make it look like it is being pressed down 
            
    ## SAVIING HIGH SCORE TO FILE AND REPLACING LAST ONE TO UPDATE ON HIGHSCORE LIST IN GAME 
    output1 =  (str(text3))
    for i in range (len(snumber)):
        output1 +="\n"+str(snumber[i]) #ADDING THE NUMBERS THAT WERE ALREADY IN GAME 
        snumber[-1] = text3
    newFile = open ("ABEERHIGHSCORE.DAT","w")
    newFile.write (output1) #writes into ABEERDATAPROJ.DAT
    newFile.close()        
      

# INSTRUCTIONS SCREEN 
def instructions(screen, mx, my, button):
    global state,arrowImage,arrowDown ,arrowUp,arrowLeft,arrowRight,arrowup,arrowdown,arrowleft,arrowright,spacebar,aKey 
    screen.fill (RED)
    arrowImage = pygame.transform.scale(arrowImage,(250,200))
    screen.blit(arrowImage,pygame.Rect(200,220 ,55,60))  
    # ARROW DOWN 
    arrowdown = pygame.transform.scale(arrowdown,(50,50)) # for arrow down 
    screen.blit(arrowdown,pygame.Rect(300,430 ,55,60))
    arrowdownText1 = fonttext.render("Moving Spaceship",1,YELLOW)
    arrowdownText2 = fonttext.render("        DOWN",1,YELLOW)#WORDS ARROW UP
    screen.blit (arrowdownText1, (250,490,40,40))
    screen.blit (arrowdownText2, (260,510,40,40))   
    #LEFT ARROW 
    arrowleft = pygame.transform.scale(arrowleft,(50,50)) # for arrow left 
    screen.blit(arrowleft,pygame.Rect(140,350 ,55,60)) 
    arrowleftText1 = fonttext.render("Moving Spaceship",1,YELLOW)
    arrowleftText2 = fonttext.render("        to LEFT",1,YELLOW)
    screen.blit (arrowleftText1, (0,350,40,40)) #WORDS FOR ARROW LEFT
    screen.blit (arrowleftText2, (0,380,40,40))
    # ARROW UP
    arrowup = pygame.transform.scale(arrowup,(50,50)) #for arrow up 
    screen.blit(arrowup,pygame.Rect(300,160 ,55,60)) 
    arrowupText1 = fonttext.render("Moving Spaceship",1,YELLOW)
    arrowupText2 = fonttext.render("            UP",1,YELLOW)
    screen.blit (arrowupText1, (260,120,40,40))
    screen.blit (arrowupText2, (260,140,40,40))    
    #RIGHT ARROW 
    arrowright = pygame.transform.scale(arrowright,(50,50)) # for arrow right 
    screen.blit(arrowright,pygame.Rect(460,350 ,55,60))
    arrowrightText1 = fonttext.render("Moving Spaceship",1,YELLOW)
    arrowrightText2 = fonttext.render("        to RIGHT",1,YELLOW)
    screen.blit (arrowrightText1, (510,350,40,40)) #WORDS FOR ARROW right
    screen.blit (arrowrightText2, (510,380,40,40))    
    #SPACEBAR 
    spacebar = pygame.transform.scale(spacebar,(400,200)) # for spacebad 
    screen.blit(spacebar,pygame.Rect(650,150 ,55,60))    
    arrowdown = pygame.transform.scale(arrowdown,(50,50)) # for spacebar
    screen.blit(arrowdown,pygame.Rect(790,290 ,55,60))    
    spacebarText1 = fonttext.render("Hit the Spacebar",1,YELLOW)
    spacebarText2 = fonttext.render("    to SHOOT ",1,YELLOW)  
    screen.blit (spacebarText1, (755,350,40,40)) #WORDS FOR spacebar 
    screen.blit (spacebarText2, (755,370,40,40))       
    # A KEYBOARD KEY 
    aKey = pygame.transform.scale(aKey,(100,100)) #letter a key 
    screen.blit(aKey,pygame.Rect(600,450 ,55,60)) 
    arrowright = pygame.transform.scale(arrowright,(50,50)) # for arrow right 
    screen.blit(arrowright,pygame.Rect(720,475 ,55,60))
    AText1 = fonttext.render("Hit the A Key When it Becomes",1,YELLOW)
    AText2 = fonttext.render("    Available to Unlock",1,YELLOW)  
    AText3 = fonttext.render("    SPECIAL POWERS",1,YELLOW)  
    screen.blit (AText1, (735,455,40,40)) #WORDS FOR A KEY  
    screen.blit (AText2, (755,485,40,40))    
    screen.blit (AText3, (755,515,40,40))    
    # RETURN TO MAIN MENU 
    rectangle2 = pygame.Rect(800, 630, 180, 50)
    outline2 = pygame.Rect (790,620,200,70)
    wording = pygame.Rect(830, 645, 90, 25)
    pygame.draw.rect(screen, YELLOW, rectangle2) # colouring int hte square snad drwating thme 
    pygame.draw.rect(screen, YELLOW, outline2,1) 
    words = fontword.render("MAIN MENU" , 1, RED)
    screen.blit(words, wording )
    if rectangle2.collidepoint(mx, my) and button == 1: #CHECKING IF THE MAINMENU OBJECT IS CLICKED 
        state = STATE_MAIN #goint to main screen 
    if rectangle2.collidepoint(mx, my): # if collides with main menu 
        pygame.draw.rect(screen, YELLOW, rectangle2,4)  #prints a yellow box  to make it look like it is being pressed down 

# LETTING USERS UNDERSTAND THE STORY OF THE GAME 
def storyscreen (screen,mx,my,button):
    global yval2,storyImage,state
    screen.fill (BLACK)
    yval2-=1 #MOVING IMAGE UP THE SCREEN 
    storyImage = pygame.transform.scale(storyImage,(1000,700)) #MAKING BACKGROUND  FOR STORY SCREEN 
    screen.blit(storyImage,pygame.Rect(0, yval2,width,height)) 
    #MAKING ARE U READY BUTTON 
    rectangle2 = pygame.Rect(770, 630, 180, 50) 
    outline2 = pygame.Rect (760,620,200,70)
    wording = pygame.Rect(790, 645, 90, 25)
    pygame.draw.rect(screen, YELLOW, rectangle2) # colouring int hte square snad drwating thme 
    pygame.draw.rect(screen, YELLOW, outline2,1) 
    words = fonttext2.render("ARE YOU READY..." , 1, RED)
    screen.blit(words, wording )
    # CHECKS IF ARE U READY BUTTON IS HIT 
    if rectangle2.collidepoint(mx, my) and button == 1:
        state = STATE_GAME #point to game screen 
    if rectangle2.collidepoint(mx, my): # if collides with button then
        pygame.draw.rect(screen, YELLOW, rectangle2,4)  #prints a yellow box  to make it look like it is being pressed down     
        
#READING DATAFILE AND MAKING THE VALUES STORED IN DATAFILE TO HIGHSCORELIST VARIABLE 
def listw():
    global snumber
    while True:
        file = dataFile.readline () # Will read in the next line from the file and assign it to the variable text
        text = file.rstrip(" ") # removes the newline character read at the end of the line
        if text =="": # checks to see if there is anymore lines if it empty this means all the lines in data file have been completed  
            break
        record = text.split (" ") # seperat 
        snumber += [int(record[0])]
       
      

# MAKING THE HIGHSCORE SCREEN 
def highscorescreen (screen, mx, my, button):
    global state,text3,snumber, output1,wordy,y4,highscoreImage,mainImage
    #BACKGROUND SCREEN 
    mainImage = pygame.transform.scale(mainImage,(1000,700))
    screen.blit(mainImage,pygame.Rect(0, 0,width,height))    
    #HIGHSCORE TITLE IMAGE 
    highscoreImage = pygame.transform.scale(highscoreImage,(500,100))
    screen.blit(highscoreImage,pygame.Rect(250, 100,50,50))    
    #SORTS THE HIGHSCORE LSIT FROM HIGH TO LOW AND OUTPUTS TOP 5 
    snumber.sort()
    snumber.reverse()
    for i in range (len(ssizeList)):
        AText1 = fontPoints.render(str(snumber[i])+" pts",1,RED)
        size = ssizeList [i]
        screen.blit(AText1,size)  
    #MAIN MENU BUTTON 
    rectangle2 = pygame.Rect(800, 630, 180, 50)
    outline2 = pygame.Rect (790,620,200,70)
    wording = pygame.Rect(830, 645, 90, 25)  
    pygame.draw.rect(screen, RED, rectangle2) # colouring int hte square snad drwating thme 
    pygame.draw.rect(screen, RED, outline2,1) 
    words = fontword.render("MAIN MENU" , 1, BLACK)
    screen.blit(words, wording )    
    #IF COLLIDES WITH MAIN MENU BUTTON THEN IT SENDS TO MAIN MENU 
    if rectangle2.collidepoint(mx, my) and button == 1:
        state = STATE_MAIN #goint to main screen 
    if rectangle2.collidepoint(mx, my): # if collides with main menu 
        pygame.draw.rect(screen, RED, rectangle2,4)  #prints a yellow box  to make it look like it is being pressed down     
    
# DRAWING MAIN MENU SCREEN AND ITS FUNCTIONS 
def drawScene(screen, mx, my, button):
    global state, mainImage,xval,obstaclespaceship,spaceship,ufo2Time,ufoTime,titleBack
    introAudio.play() #PLAYS OPENING AUDIO 
    #DRAWS BACKGROUND 
    mainImage = pygame.transform.scale(mainImage,(1000,700))
    screen.blit(mainImage,pygame.Rect(0, 0,width,height))     
    #DRAWS TITLE OF GAME 
    titleBack = pygame.transform.scale(titleBack,(500,100))
    screen.blit(titleBack,pygame.Rect(250, 100,50,50))
    # DRAWING THE THREE BUTTON OPTIONS 
    for i in range(len(rectList)):
        rectangle = rectList[i]
        pygame.draw.rect(screen, RED, rectangle)
        words = wordList[i] # words list which will print on to each corresponding square
        outline = outlineList[i] # creating an outline on the box 
        pygame.draw.rect(screen, RED, rectangle) # colouring int hte square snad drwating thme 
        pygame.draw.rect(screen, RED, outline,1) #orange outline        
        text = fontHello.render(titleList[i] , 1, YELLOW)	
        screen.blit(text, words)
        
        if rectangle.collidepoint(mx, my) and button == 1: # IF COLES WITH PLAY GAME THEN SENDS TO THE STORY AND THEN FROM STORY IT GOES TO THE GAME 
            if i == 0:
                state = STATE_STORY
            elif i == 1: #IF COLLIDES WITH INSTRUCTIONS 
                state = STATE_INSTR
            elif i ==2: #IF COLLIDES WITH HIGHSCORE TAB 
                state = STATE_HIGHSCORE
        if rectangle.collidepoint(mx, my): # if collides with remove
            pygame.draw.rect(screen, RED, rectangle,4)  #prints a black box to make it look like it is being pressed down 
    # DRAWING THE PASSING BY SPACESHIPS PERIODICALLY 
    if spaceship == True:
        xval+=10
        xval1=0
        yval = 200
        yval1 = 550
        obstaclespaceship = pygame.transform.scale(obstaclespaceship,(50,30))
        screen.blit(obstaclespaceship,pygame.Rect(0+xval, yval,55,60))   
        obstaclespaceship = pygame.transform.scale(obstaclespaceship,(50,30))
        screen.blit(obstaclespaceship,pygame.Rect(0+xval, yval1,55,60))               
        if xval+xval1 >990 : # IF REACHES EN OF SCREEN THEN DELETES IT 
            spaceship = False
            xval = 0 
            xval1 = 0 
           
    ufoTime = pygame.time.get_ticks ()
    if ufoTime - ufo2Time > 2000: # EVERY 2 SECONDS DRAWS MORE SPACESHIPS 
        ufo2Time = pygame.time.get_ticks() 
        spaceship= True
        xval1=0
        yval = 200        
myClock = pygame.time.Clock()
lives()  #creates the x and y list in for the lives and allows them to be drawn 
listw ()
# BASIC TOOLS AND FUNCTIONS OF INPUTS FROM USER 
while running:
    button = 0
    
    events = pygame.event.get()
# IF EVENTS ARE QUITTING, OR PLAYING THE GAME AND BUTTON IS DOWN 
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if state == STATE_GAME:
                    movingLeft=True 
            if event.key == pygame.K_RIGHT:
                if state == STATE_GAME:
                    movingRight=True 
            if event.key == pygame.K_UP:
                if state == STATE_GAME:
                    movingUp=True
            if event.key == pygame.K_DOWN:
                if state == STATE_GAME:
                    movingDown= True
            if event.key == pygame.K_SPACE:
                shootingball = True #IF SPACEBAR IS HIT THEN BALLS ARE SHOT 
                mx=herox #USED FOR HERO SPACESHIP 
                my=heroy
                if state == STATE_GAME: #IF THE STATE IS GAME THEN DRAWS A BULLET 
                    addBullet(mx,my)
                    shootingAudio.play()   #PLAYS THE SHOOTING AUDIO 
            if event.key == pygame.K_a and slowingPower == True :#IF THE KEY IS A AND THE SLOW POWER IS TRUE THEN WILL ALLOW FOR THE SLOW POWER TO ACTUALLY BE USED 
                slowingPower = False 
                slowmotion = True 
                pointTimer = pygame.time.get_ticks ()
                currentSpeed = obstacleSpeed 
                
        #IF KEY IS UP THEN STOPS MOVEMENT F HERO SPACESHIP 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if state == STATE_GAME:
                    movingLeft=False
            if event.key == pygame.K_RIGHT:
                if state == STATE_GAME:
                    movingRight=False
            if event.key == pygame.K_UP:
                if state == STATE_GAME:
                    movingUp=False
            if event.key == pygame.K_DOWN:
                if state == STATE_GAME:
                    movingDown= False
     
        #MOUSE INPUT (SAVING LOCATIONS OF MOUSE TO VARIABLES 
        if event.type == pygame.MOUSEMOTION:
            mx1, my1 = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx1, my1 = event.pos
            button = event.button
    # traffic cop AND DIFFERNET STATES 
    if state == STATE_MAIN:
        drawScene(screen, mx1, my1, button)
    elif state == STATE_GAME:
        playGame(screen, mx1, my1, button)
        
        if count == 3:
            state = STATE_FINISH   
            movingRight=False
            movingDown=False
            movingUp=False
            movingLeft=False             
            
            finalMessage = "YOU LOST!"
    
    elif state == STATE_FINISH:
        
        endScreen (screen, mx1, my1, button)
        setup() #SETS UP ENTIRE GAME AGAIN WHEN ITS ON END SCREEN 
        movingRight=False
        movingDown=False
        movingUp=False
        movingLeft=False          
    elif state == STATE_INSTR:
        instructions (screen, mx1, my1, button)
    elif state == STATE_STORY:
        storyAudio.play()
        storyscreen(screen,mx1,my1,button)
          
    else:
        highscorescreen(screen,mx1,my1,button)

    pygame.display.flip()       
    
    myClock.tick(60)

pygame.event.get()
pygame.quit()
