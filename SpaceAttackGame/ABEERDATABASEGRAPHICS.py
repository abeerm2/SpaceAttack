dataFile = open ("ABEERDATAPROJ.DAT","r")
import pygame #importing pygame
import math #importin math for funciton
pygame.init() #initilize
SIZE = (width,height) = (1000,700) #size of screen
screen = pygame.display.set_mode(SIZE)

## DATA FILE READINGGG ####

# creates list of student numbers after separation     
fname = [] # creates list for first names after separation of data 
lname = []# creates list for last names after separation of data 
bday = []# creates list for fbirhtdays after separation of data 
country =[] # creates list for background countries after separation of data 
live = [] # creates list for current city they live in after separation
snumber = [] 
output ="" # empty string which will be used to add various strings together 
def list (dataFile): # this function will seperate each line and form lists for each category/field 
    fname = [] # creates list for first names after separation of data 
    lname = []# creates list for last names after separation of data 
    bday = []# creates list for fbirhtdays after separation of data 
    country =[] # creates list for background countries after separation of data 
    live = [] # creates list for current city they live in after separation
    snumber = []     
    while True:
        file = dataFile.readline () # Will read in the next line from the file and assign it to the variable text
        text = file.rstrip("\n") # removes the newline character read at the end of the line
        if text =="": # checks to see if there is anymore lines if it empty this means all the lines in data file have been completed  
            break
        record = text.split (" ") # seperates each piece of info as the space indicates next piece of info
        snumber += [int(record[0])] # this is to add to the  student number list
        fname += [record[1]]# this is to add to the first name list
        lname += [record [2]] # this is to add to the last name list
        bday += [record[3]] # this is to add to the  bday list
        country += [record[4]] # this is to add to the background country list
        live += [record [5]] # this is to add to the current city list
    return snumber,fname,lname, bday,country,live
output1 = list(dataFile) # Sends data file to list functions
snumber = output1[0] # the first output was student numbers adn is making the entire list solely for student numbers
fname = output1[1] # same thing for first name 
lname = output1[2] # same thing for last name 
bday = output1[3] # same thing for bday 
country = output1[4] # same thing for background country 
live = output1[5] # same thing for current city 
total = len (fname) # this is chekcing the number of information in the list 

##ending of DATA FILE READING ##

## this is making the outputed "nICE" list, 

dataFile.close() # close file to prevent loss 



fontword = pygame.font.SysFont("Times New Roman",30) # main font used on home page
screenword = pygame.font.SysFont("Times New Roman",21) #these are the lists and some words on the other pages
titleword = pygame.font.SysFont("Times New Roman",23) #headings 
title1word = pygame.font.SysFont("Times New Roman",40) #title on inside pages 
title2word = pygame.font.SysFont("Times New Roman",60) #school database title on main screen 

## COLOURS###

ORANGE = (247, 194, 69)
BLACK = (0,0,0)
BLUE = (89, 150, 189)
RED = (240, 67, 67)
PURPLE = (152, 95, 237)
WHITE = (255,255,255)
PINK = (219, 140, 186)
GREEN = (98, 184, 90)

rectangle1 = pygame.Rect(550, 500, 200, 100) #remove
rectangle2 = pygame.Rect(250, 500, 200, 100)#modify
rectangle3 = pygame.Rect(250, 333, 200, 100) #add
rectangle4 = pygame.Rect(550, 333, 200, 100) #no changes 
# RECTANGLES ON NO CHANGES AND BEYOND SCREENS 
rectangle6 = pygame.Rect(800, 630, 190, 60)
rectangle7 = pygame.Rect(100, 630, 190, 60)
rectangle8 = pygame.Rect(400, 630, 190, 60)
rectangle9 = pygame.Rect(700, 630, 190, 60)
#wORDING ON THE BOXES ON MAIN SCREEN 
wording1 = pygame.Rect(610, 535, 100, 50) #REMOVE
wording2 = pygame.Rect(310, 535, 100, 50) #modify 
wording3 = pygame.Rect(330, 368, 100, 50)#add
wording4 = pygame.Rect(590, 368, 100, 50)#NO changes
# OUTLINE OF EACH BOX ON THE HOME PAGE 
testoutline = pygame.Rect(540, 490, 220, 120) 
testoutline2 = pygame.Rect (240,490,220,120)
testoutline3 = pygame.Rect (240,323,220,120)
testoutline4 = pygame.Rect (540,323,220,120)
# COMPILING EACH ONE OF THESE INTO CORRESPONDING LISTS TO USE IN LOOP ##
outlineList = [testoutline,testoutline2,testoutline3,testoutline4]
wordList = [wording1,wording2, wording3,wording4]
rectList = [rectangle1, rectangle2, rectangle3,rectangle4]
titleList = ["MODIFY", "REMOVE", "ADD","NO CHANGES"]

## defining values for each screen ##
MAIN_SCREEN  = 1
RED_SCREEN  = 2 # modify 
BLUE_SCREEN  = 3 #remove 
PURPLE_SCREEN = 4 #no changes
PINK_SCREEN = 5 #add
GREEN_SCREEN = 6

def writing (): #this is the rectangles that are eneded to write words 
    # creating empty lists 
    ssList = [] #snumber
    fnList = [] #fnmae
    lnList = []#kname 
    bdList =[]#bday
    ocList =[]#coountry list 
    cyList =[] #city list 
    county = 180
    countx = 200
    ## BUILDING RECTANGLES IN COLUMS SO THE LISTS CAN PRINT OUT INDIVIUDALLY IN COLUMNS 
    #Student number columns 
    for k in range (len(fname)): 
        rectsize =(120,county,200,100)
        county+=25
        ssList +=[rectsize]        
    
    #FIRST NAME COLUMNS 
    county = 180 #resets value for fname lists so they start at the saem y value 
    for k in range (len(fname)):
        rectsize =(280,county,200,100)
        county+=25
        fnList +=[rectsize]
    
    #LAST NAME COLUMN
    county = 180 #same thing
    for k in range (len(fname)):
        rectsize =(400,county,200,100)
        county+=25
        lnList +=[rectsize]
    
    #BDAY LIST COLUMN
    county = 180#same thing
    for k in range (len(fname)):
        rectsize =(512,county,200,100)
        county+=25
        bdList +=[rectsize]
    
    #COUNTRY COLUMN
    county = 180 #SAME THING
    for k in range (len(fname)):
        rectsize =(615,county,200,100)
        county+=25
        ocList +=[rectsize]
    
    #CITY COLUMN 
    county = 180#same thing
    for k in range (len(fname)):
        rectsize =(808,county,200,100)
        county+=25
        cyList +=[rectsize]
    return cyList, ocList, bdList, lnList, fnList, ssList #RETURNIGN ALL VALUES 

output1 = writing() #SENDING TO WRITING FUNCTION TO GERNATE COLUMNS 

#PUTTING ALL INFO FROM CY LISTS INTO LISTS WHICH CAN BE USED IN THE PROGRAM 
ssizeList = []
fnsizeList = []
lnsizeList = []
bdsizeList =[]
ocsizeList =[]
cysizeList =[]
ssizeList =  output1[5]  #Student rectangle list 
fnsizeList = output1[4] #first name rectangle list 
lnsizeList =output1[3] #last name rectangle list 
bdsizeList =output1[2]#bday rectangle list 
ocsizeList =output1[1]# origin country rectangle lsit 
cysizeList =output1[0]# current city rectangle lsit 



state = MAIN_SCREEN #original state that the program will start with everytime 

#DISTANCE to calculate the collisions 
def distance(pt1x, pt1y, pt2x, pt2y): #collision function 
    diffx = pt2x - pt1x
    diffy = pt2y - pt1y
    distSquared = diffx**2 + diffy**2
    return math.sqrt(distSquared)

# clear the screen, draw off screen and then display
def drawScene(screen, mx, my, button):
    global state
    screen.fill(BLACK) #start with black screen on main screen 
    # BUILDING THE SQUARES THAT CAN BE SEEN ON THE HOME SCREEN 
    for i in range(len(rectList)):
        rectangle = rectList[i] #using list to print each 
        words = wordList[i] # words list which will print on to each corresponding square
        outline = outlineList[i] # creating an outline on the box 
        pygame.draw.rect(screen, ORANGE, rectangle) # colouring int hte square snad drwating thme 
        pygame.draw.rect(screen, ORANGE, outline,1) #orange outline 
        text = fontword.render(titleList[i] , 1, (255, 0, 0))	#writing the words 
        screen.blit(text, words)#blitting the word 
         
        
        ##IF COLLIDE AND CLICK ON ONE OF THE QUEARES IT SWITCHING TO THE CORRESPONDING STATES 
        if rectangle.collidepoint(mx, my) and button == 1:
            if i == 0:
                state = RED_SCREEN #MODIFY 
            elif i == 1:
                state = BLUE_SCREEN #REMOVE
            elif i == 2:
                state = PINK_SCREEN #ADD
            elif i==3:
                state =  PURPLE_SCREEN #NO CHANGES 

              
def checkFname (checker,dig1,counter,lengths): # this looks for matching first letters depending on what letter the user enters 
    output ="" # empty string 
    
    while True: 
        namer = fname[dig1]  # creates varianle equal to the specific name as it runs through
        if checker.upper() == namer [0].upper(): # upper just bc 
            counter+=1 # this is counting amount of people 
            
            output +=  ("%8i\t*\t%-10s\t*\t%-10s\t*\t%8s\t*\t%-8s\t*\t%-11s\t*\n" #creating output 
                    %(snumber[dig1],fname[dig1],lname[dig1],bday[dig1],country[dig1],live[dig1]))
        
        lengths +=1 #
        if lengths == len(fname): #breaks if the fnamae is equal to t he amount of times run through
            break 
        dig1+=1 #to change the vlaue 
    if output =="": #if nothing 
        output = "Nobody has a name starting with",checker #then prints this 
    return output #returning output 
def checkLname (checker,dig1,counter,lengths): # this looks for matching first letters depending on what letter the user enters 
    output ="" # empty string 
    while True: 
        namer = lname[dig1]  # creates varianle equal to the specific name as it runs through
        if checker.upper() == namer[0].upper(): # upper just bc 
            counter+=1 # this is counting amount of people 
            output +=  ("%10i\t*\t%-10s\t*\t%-10s\t*\t%8s\t*\t%-8s\t*\t%-11s\t*\n"
                    %(snumber[dig1],fname[dig1],lname[dig1],bday[dig1],country[dig1],live[dig1])) # BUILDING OUtput 
        
        lengths +=1 # Adding to the number of times its been run through so it knows when its reached the end of the string 
        if lengths == len(fname):
            break # breaks if equals total
        dig1+=1 # add dig to move on to next component of list 
    if counter < 1 : # if nothign has been added to the string then it breaks nad brings nobody has...
        output = "Nobody has a name starting with",checker
    return output # sends back to program
def checkBday (checker,dig1,counter,lengths): # this looks for matching first letters depending on what letter the user enters 
    output = "" # empty string 
    while True: 
        month = bday[dig1]# creates varianle equal to the specific name as it runs through
        day = month[:2]
        if checker == day: # upper just bc 
            
            counter+=1 # this is counting amount of people
            
            output +=  "%10i\t*\t%-10s\t*\t%-10s\t*\t%8s\t*\t%-8s\t*\t%-11s\t*\n" %(snumber[dig1],fname[dig1],lname[dig1],bday[dig1],country[dig1],live[dig1]) # building string
        
        lengths +=1 # same thing as last function 
        if lengths == len(fname): #same thing if this breaks if matches the same amount run throguh
            break 
        dig1+=1 #changes value 
    if counter < 1 :
        output = "Nobody has a bday in the month",checker #prints this if nothing 
    return output #reutns output 

running = True #while running will do everythign underneath 
myClock = pygame.time.Clock()

mx = my = 0
while running:   # this is our game loop
    button = 0

    # Check all the events that happen
    for evnt in pygame.event.get():
        # if the user tries to close the window, then raise the "flag"
        if evnt.type == pygame.QUIT: #if quit is hit then running is false and programs stops 
            running = False #making running false 
        if evnt.type == pygame.MOUSEMOTION: #setting up mouse motion 
            mx, my = evnt.pos #coordinates which will be used to determine collisions 
        if evnt.type == pygame.MOUSEBUTTONDOWN: #mouse button down 
            mx, my = evnt.pos 
            button = evnt.button
            if button == 3: #if button is equal to 3 and then retuns to main screen 
                state = MAIN_SCREEN 
        
    if state == MAIN_SCREEN : # if state is in main screen 
        drawScene(screen, mx, my, button) #prints thte draw scene from above 
        pygame.draw.rect (screen, BLACK, (0, 0, width, height),10) # prints black background
        maintitle = title2word.render(("SCHOOL DATABASE"),10,ORANGE) #title on main page 
        screen.blit (maintitle,(300,175,300,300)) # prints titel in pygame 
        if rectangle1.collidepoint(mx, my): # if collides with remove
            pygame.draw.rect(screen, BLACK, rectangle1,2)  #prints a black box to make it look like it is being pressed down 
        elif rectangle2.collidepoint(mx, my): #if collides with modify 
            pygame.draw.rect(screen, BLACK, rectangle2,2) # then prints the same thing to make it look like it is being pushed 
        elif rectangle3.collidepoint(mx, my): #if it collides with add 
            pygame.draw.rect(screen, BLACK, rectangle3,2) # makes it looks like its beign pushed 
        elif rectangle4.collidepoint(mx, my): # goes on collide no change s
            pygame.draw.rect(screen, BLACK, rectangle4,2)# then makes it look like it is being pushed 
      
    elif state == BLUE_SCREEN : #if state is blue screen THIS IS THE ONE PRESSED IF WANT TO REMOVE SOMETHING 
        pygame.draw.rect(screen, BLUE, (0, 0, width, height)) #prints blue background 
        pygame.draw.rect(screen,BLACK,(800, 10, 190, 100)) #prints black exit box which dont work 
        text = fontword.render("EXIT" , 1, (255, 255, 255))
        screen.blit(text,(875, 50, 190, 100)) #prints exit in pygame 
        
        uppertitle = title1word.render(("SCHOOL DATABASE"),10,WHITE) #title shcool database 
        title = titleword.render("%s          %s          %s          %s          %s          %s" %("Student Number", "First Name","Last Name", "Birthday", "Background Country","Current City"),10,WHITE) # title for nice list 
        screen.blit(title,(120,150,200,100)) # prints title shcool database 
        screen.blit (uppertitle,(375,100,300,300))  #prints heading 
        
        #PRINTS THE NICE LIST BYUSING THE COLUMNS AND RECTANGLES PRINTING EACH LIST INDIVIDUALLY 
        for i in range(len(ssizeList)):  #STUDENT NUMBER
            size = ssizeList[i] 
            text = screenword.render("%i" %(snumber[i]),1, BLACK)	
            screen.blit(text,size) 
#FIRST NAME LIST/COLUMN
        for m in range(len(fnsizeList)):
            size = fnsizeList[m]
            text = screenword.render("%s" %(fname[m]),1, BLACK)	
            screen.blit(text,size) 
#LAST NAME LIST/COLUMN
        for m in range(len(fnsizeList)):
            size = lnsizeList[m]
            text = screenword.render("%s" %(lname[m]),1, BLACK)		
            screen.blit(text,size) 
#BDAY LIST/COLUMN
        for m in range(len(fnsizeList)):
            size = bdsizeList[m]
            text = screenword.render("%s" %(bday[m]),1, BLACK)		
            screen.blit(text,size)         
#ORIGIN COUNTRY COLUMN/LIST 
        for m in range(len(fnsizeList)):
            size = ocsizeList[m]
            text = screenword.render("%s" %(country[m]),1, BLACK)		
            screen.blit(text,size)    
#CITY CURRENT LSIT/COLUMN 
        for m in range(len(fnsizeList)):
            size = cysizeList[m]
            text = screenword.render("%s" %(live[m]),1, BLACK)		
            screen.blit(text,size) 
            
#ALL OF THESE ARE PRINGTED IN BLACK AND ARE ALIGNED 
    
        pygame.display.update()#UPDATES SCREEN 
        pygame.event.get() #UPDATES NEEDED FOR MAC DONT KNOW WHY 
        remover = input ("Please enter the unique code of the person you'd like to remove (enter no if you want to go to home page): ") # code is required
        if remover.upper() == "NO":
            state = MAIN_SCREEN
        else:
            code = snumber.index(int(remover)) #checks where the spot is located and the information o that person will be located in the same spot for all lists

            print ("You have now deleted: ",fname[code]) # output who they deleted 
            fname.remove(fname[code]) # removes name of person from fname list
            snumber.remove(snumber[code]) # removes student number from snumber list 
            lname.remove(lname[code]) # removes lastname from lname list 
            country.remove(country[code]) # removes country from background country 
            live.remove (live[code]) #removes current city from current city list 
            bday.remove(bday[code]) #removes bday of indiviudal from bday lsit 
               

        length = len(fname) #checks the length of the list as one of the lists as they would all be the same 
        newFile = open ("ABEERDATAPROJ.DAT","w") #opening new file to write 
        dig = 0            
        while True:
            if dig == length: #first checks if dig is equal to the length so knows when to break
                break     
            output = str(snumber[dig])+" "+fname[dig]+" "+lname[dig]+" "+bday[dig]+" "+country[dig]+" "+live[dig] +"\n" #creates an output in format of data files 
            newFile.write (output) #writes into ABEERDATAPROJ.DAT
            dig+=1 #adds dig to get the next piece of data 
        
        newFile.close()
        # ADDING TO THE RECTANGLES SO CAN FIT MROE RECORDS AND UPDATE AUTOMATICALLY 
        output1 = writing()
        ssizeList = [] 
        fnsizeList = []
        lnsizeList = []
        bdsizeList =[]
        ocsizeList =[]
        cysizeList =[]
        ssizeList =  output1[5] 
        fnsizeList = output1[4]
        lnsizeList =output1[3]
        bdsizeList =output1[2]
        ocsizeList =output1[1]
        cysizeList =output1[0]        
        
        
        
    elif state == RED_SCREEN: # this is IF STATE IS RED AND MODIFY IS CLICKED ON FROM HOMME PAGE 
        pygame.draw.rect(screen, RED, (0, 0, width, height)) #DRAWS RED BACKGROUND 
        pygame.draw.rect(screen,BLACK,(800, 10, 190, 100)) #ADDS EXIT IMAGE DOESNT WORK THO
        text = fontword.render("EXIT" , 1, (255, 255, 255))
        screen.blit(text,(875, 50, 190, 100)) #PRINTS EXIT INTO BOX 
        
        uppertitle = title1word.render(("SCHOOL DATABASE"),10,WHITE) #SCHOOL DATABASE TITLE 
        title = titleword.render("%s          %s          %s          %s          %s          %s" %("Student Number", "First Name","Last Name", "Birthday", "Background Country","Current City"),10,WHITE) # title for nice list 
        screen.blit(title,(120,150,200,100))  #PRINTS TITLE 
        screen.blit (uppertitle,(375,100,300,300))  #PRINTS HEADING 
        #PRINTS THE NICE LIST BYUSING THE COLUMNS AND RECTANGLES PRINTING EACH LIST INDIVIDUALLY
        # Prints the student numbers
        for i in range(len(ssizeList)):
            size = ssizeList[i]
            text = screenword.render("%i" %(snumber[i]),1, BLACK)	
            screen.blit(text,size) 
#PRINTS FIRST NAMES
        for m in range(len(fnsizeList)):
            size = fnsizeList[m]
            text = screenword.render("%s" %(fname[m]),1, BLACK)	
            screen.blit(text,size) 
#PRINTS LAST NAMES 
        for m in range(len(fnsizeList)):
            size = lnsizeList[m]
            text = screenword.render("%s" %(lname[m]),1, BLACK)		
            screen.blit(text,size) 
#PRINTS BDAY 
        for m in range(len(fnsizeList)):
            size = bdsizeList[m]
            text = screenword.render("%s" %(bday[m]),1, BLACK)		
            screen.blit(text,size)         
#PRINTS ORIGIN COUNTRY
        for m in range(len(fnsizeList)):
            size = ocsizeList[m]
            text = screenword.render("%s" %(country[m]),1, BLACK)		
            screen.blit(text,size)    
#PRINTS CITY LIST 

        for m in range(len(fnsizeList)):
            size = cysizeList[m]
            text = screenword.render("%s" %(live[m]),1, BLACK)		
            screen.blit(text,size) 
            
        #UPDATING 
        pygame.display.update()
        pygame.event.get()

        #ASKING QUESTIONS IN SHELL FOR MODIFICATION AND AUTOMATICALLY UPDATES 
        
        question = (input ("Please enter the ID number of the person you'd like to modify you would like to modify (If you'd like to go to home page enter 'no'): "))# ask for id number  
        if question == "-1" or question.upper() == "NO"  : #if person says no to above question or negative one it breaks 
            state = MAIN_SCREEN
        else:
            
            spot = snumber.index(int(question)) # checking where the spot is to find corresponding value in other list 
            name = fname[spot] # ^
            check = input("You are modifying %s. Is this who you would like to modify? "%name) # pritns who you are modifying 
            
        
            if check.upper() == "YES": # if yes does everyhting below
                modify = input ("What category would you like to modify? ") #asks category
                user = modify.upper()
                if user == "FIRST NAME": # if first name then will change the first name in the list 
                    change = input ("What would you like to change the first name to: ") # what it is being changed to
                    fname[spot] = change.capitalize() # capitalize just ot match 
                    
                    
                elif user == "STUDENT NUMBER": # if student number changes student number in list 
                    change = input ("What would you like to change the student number to: ") # user input 
                    snumber[spot] = change   # changes the spot directly in the list 
                    
                    
                elif user == "LAST NAME": # last name if enter 
                    change = input ("What would you like to change the last name to: ") #what user wants to change
                    lname[spot] = change.capitalize() # capitalizes for format and puts directly into list 
                     
                              
                elif user == "BIRTHDAY": # if user wants to change brithdy
                    change = input ("What would you like to change the birthday to (mm/dd/yy): ") # what they watn it changed to
                    bday[spot] = change  #changes directly in list
                     
                          
                elif user == "BACKGROUND COUNTRY": #wants to change country theyre from
                    change = input ("What would you like to change the background country to: ") #what to 
                    country[spot] = change.capitalize() #cap for form and then changes in list 
                     
                    
                elif user == "CURRENT CITY": #where they currently live
                    change = input ("What would you like to change the current city to: ") #changes to where the user lives now 
                    live[spot] = change.capitalize()#cap for form and replaces in list 
                    
                                 
                else: 
                    print("This is not valid") #if they enter something which is not an option pritns not valid 
                
        
        length = len(fname) #checks the length of the list as one of the lists as they would all be the same 
        newFile = open ("ABEERDATAPROJ.DAT","w") #opening new file to write 
        dig = 0            
        while True:
            if dig == length: #first checks if dig is equal to the length so knows when to break
                break     
            output = str(snumber[dig])+" "+fname[dig]+" "+lname[dig]+" "+bday[dig]+" "+country[dig]+" "+live[dig] +"\n" #creates an output in format of data files 
            newFile.write (output) #writes into ABEERDATAPROJ.DAT
            dig+=1 #adds dig to get the next piece of data 
        
        newFile.close()  #CLOSES FILE BECAUSE CHANGES IN DATA BASE 



    elif state == PURPLE_SCREEN: # PURPLE STATE THIS IS TEY CLICK ON THE NO CHANGES BOX 
        pygame.draw.rect (screen, PURPLE, (0,0,width,height))#DRAWS PURPLE BACKGROUND 
        pygame.draw.rect(screen,BLACK,(800, 10, 190, 100))#DRAWS BLACK EXIT BOX WHICH DOES NOT WORK 
        text = fontword.render("EXIT" , 1, (255, 255, 255)) #PRINTS EXIT 
        screen.blit(text,(875, 50, 190, 100)) #PRINTS EXIT ON TOT HE BOX 
        uppertitle = title1word.render(("SCHOOL DATABASE"),10,WHITE) #PRINTS SCHOOL DATA BASE TITLE 
        title = titleword.render("%s          %s          %s          %s          %s          %s" %("Student Number", "First Name","Last Name", "Birthday", "Background Country","Current City"),10,WHITE) # title for nice list 
        screen.blit(title,(120,150,200,100)) #PRINTING ON TO PYGAME BIG TITLE 
        screen.blit (uppertitle,(375,100,300,300))      #PRINGTING HEADING ON TO PYGAME
        pygame.draw.rect(screen,BLACK,(800, 630, 190, 60)) #PRINTS SMALL BLACK BOX 
        text = titleword.render("Meaningful Reports" , 1, (255, 255, 255)) #PRINTS MEANINGFUL REPORTS 
        screen.blit(text,(825, 650, 190, 100))      #PRINTS MEANINGGUL REPORT INTO BOX 
        
        #PRINTS THE NICE LIST BYUSING THE COLUMNS AND RECTANGLES PRINTING EACH LIST INDIVIDUALLY
        # Prints the student numbers        
        for i in range(len(ssizeList)):
            size = ssizeList[i]
            text = screenword.render("%i" %(snumber[i]),1, BLACK)	
            screen.blit(text,size) 
#PRINTS FIRST NAME COLUMN LIST 
        for m in range(len(fnsizeList)):
            size = fnsizeList[m]
            text = screenword.render("%s" %(fname[m]),1, BLACK)	
            screen.blit(text,size) 
#PRINTS LAST NAME COLUMN LIST 
        for m in range(len(fnsizeList)):
            size = lnsizeList[m]
            text = screenword.render("%s" %(lname[m]),1, BLACK)		
            screen.blit(text,size) 
#PRINTS BDAY COLUMN LSIT 
        for m in range(len(fnsizeList)):
            size = bdsizeList[m]
            text = screenword.render("%s" %(bday[m]),1, BLACK)		
            screen.blit(text,size)         
# PRINTS ORIGIN CITY LIST 
        for m in range(len(fnsizeList)):
            size = ocsizeList[m]
            text = screenword.render("%s" %(country[m]),1, BLACK)		
            screen.blit(text,size)    
# PRITNS CITY LIST 
        for m in range(len(fnsizeList)):
            size = cysizeList[m]
            text = screenword.render("%s" %(live[m]),1, BLACK)		
            screen.blit(text,size) 
        if rectangle6.collidepoint(mx, my) and button ==1  : # IF COLLIDES WITH MEANINGFUL REPORT AND LEFT CLICK THEN ANOTHER SCREEN WILL OPEN 
            state = GREEN_SCREEN #THAT IS GREEN SCREEN
        pygame.display.update() #UPDATES 
        pygame.event.get()        
    elif state == GREEN_SCREEN: #THIS IS AFTER SOMEONE CLICKS ON THE EMANINGFUL  REPORT BUTTON IT IS SENT TO THIS STATE 
        pygame.draw.rect (screen, GREEN, (0,0,width,height)) #DRAWS GREEN BACKGROUND
        pygame.draw.rect(screen,BLACK,(100, 630, 190, 60)) #DRAWS BLACK SQUARE (1)
        text = titleword.render("First Name Reports" , 1, (255, 255, 255)) #PRINTS FIRST NAME REPORTS ON TO THE BOX ONE
        screen.blit(text,(125, 650, 190, 100)) #PRINTS THE FIRST NAME INTO PYTHON
        pygame.draw.rect(screen,BLACK,(400, 630, 190, 60)) #PRINTS BOX 2 FOR LAST NAEM REPORTS 
        text = titleword.render("Last Name Reports" , 1, (255, 255, 255))
        screen.blit(text,(425, 650, 190, 100))        #PRINTS LAST NAME REPORTS INTO PYTHON
        pygame.draw.rect(screen,BLACK,(700, 630, 190, 60)) #PRINTS THE LAST BOX FOR BIRHTDYA REPORTS 
        text = titleword.render("Birthday Reports" , 1, (255, 255, 255)) #PRINTS BDAY REPORTS INTO THE THIRD BOX 
        screen.blit(text,(735, 650, 190, 100))   
        dig1 = 0
        counter = 0 
        lengths = 0    
        uppertitle = title1word.render(("SCHOOL DATABASE"),10,WHITE) #TITLE 
        screen.blit(uppertitle,(120,150,200,100)) #PRINTING ON TO PYGAME BIG TITLE 
                       

        if rectangle7.collidepoint(mx, my) and button ==1  : #IF HITS FIRST NAME REPORT 
            text = fontword.render(("Your New generated list is in python shell"),1, BLACK)                  
            screen.blit(text,(100,200,200,300))   
            pygame.display.update()
            pygame.event.get() 

            checker = input ("What first letter are you looking for (enter no if you want to go to home page): ") #asks user to enter first letter of person theyre looking for  
            if checker.upper() =="NO": #IF SAY NO SENDS BACK TO MAIN SCREEN
                state = MAIN_SCREEN         
            
            else:
                final = checkFname(checker,dig1,counter,lengths) #sends to function
                print ("Record of people whose first names start with %s: "%(checker))
                print (final)
         
        elif rectangle8.collidepoint(mx, my) and button ==1  : #IF HITS LAST NAME REPORTS 
            text = fontword.render(("Your New generated list is in python shell"),1, BLACK)                  
            screen.blit(text,(100,200,200,300))   
            pygame.display.update()
            pygame.event.get() 
            checker = input ("What first letter are you looking for(enter no if you want to go to home page): ") #asks for first LAST
            if checker.upper() =="NO":
                state = MAIN_SCREEN            

            else:
                final = checkLname (checker,dig1,counter,lengths) #sends to function
                print ("Record of people whose last names start with %s: "%(checker)) #print statement 
                print (final)
        elif rectangle9.collidepoint(mx, my) and button ==1  : #IF HITS BIRTHDAY REPORT 
            text = fontword.render(("Your New generated list is in python shell"),1, BLACK)                  
            screen.blit(text,(100,200,200,300))   
            pygame.display.update()
            pygame.event.get() 
            question2 = input ("What month are you looking for within the records (please enter as mm and enter no if you want to go to home page): ") #asks for month
            if question2.upper() =="NO":
                state = MAIN_SCREEN
            else:
                checker = question2 #just makes it easier for me
                final = checkBday (checker,dig1,counter,lengths) #sends to function
                print ("Record of people whose birthday month is",checker) #print statement 
                print (final)                      

    else: #THIS IS IF ADD IS HIT 
        
        pygame.draw.rect (screen, PINK, (0,0,width,height)) #PRINTS PINKISH BACKGROUND ON SCREEN
        pygame.draw.rect(screen,BLACK,(800, 10, 190, 100)) # EXIT BOX WHICH DOESNT WORK JUST FOR DESIGN 
        text = fontword.render("EXIT" , 1, (255, 255, 255)) #PRINTS EXIT BOX WORDS 
        screen.blit(text,(875, 50, 190, 100)) #PRINTS WORDS ON TO PYGAME
    
        uppertitle = title1word.render(("SCHOOL DATABASE"),10,WHITE) #TITLE 
        title = titleword.render("%s          %s          %s          %s          %s          %s" %("Student Number", "First Name","Last Name", "Birthday", "Background Country","Current City"),10,WHITE) # title for nice list 
        screen.blit(title,(120,150,200,100)) #HEADINGS FOR LISTS 
        screen.blit (uppertitle,(375,100,300,300))  #TITLE SCHOOL DATABASE
        #PRINTS THE NICE LIST BYUSING THE COLUMNS AND RECTANGLES PRINTING EACH LIST INDIVIDUALLY
        # Prints the student numbers                
        for i in range(len(ssizeList)):
            size = ssizeList[i]
            text = screenword.render("%i" %(snumber[i]),1, BLACK)	
            screen.blit(text,size) 
#PRINTS FIRST NAME COLUMN LIST
        for m in range(len(fnsizeList)):
            size = fnsizeList[m]
            text = screenword.render("%s" %(fname[m]),1, BLACK)	
            screen.blit(text,size) 
#PRINTS LAST NAME COLUMN LIST
        for m in range(len(fnsizeList)):
            size = lnsizeList[m]
            text = screenword.render("%s" %(lname[m]),1, BLACK)		
            screen.blit(text,size) 
#PRINTS BDAY COLUMN LSIT 
        for m in range(len(fnsizeList)):
            size = bdsizeList[m]
            text = screenword.render("%s" %(bday[m]),1, BLACK)		
            screen.blit(text,size)         
# PRINTS ORIGIN CITY LIST 
        for m in range(len(fnsizeList)):
            size = ocsizeList[m]
            text = screenword.render("%s" %(country[m]),1, BLACK)		
            screen.blit(text,size)    
# PRITNS CITY LIST 
        for m in range(len(fnsizeList)):
            size = cysizeList[m]
            text = screenword.render("%s" %(live[m]),1, BLACK)		
            screen.blit(text,size) 
            

    
        pygame.display.update() #UPDATES 
        pygame.event.get() 
        question = input("Would you like to enter a new person (if you'd like to go back to home page enter no): ") # ASKS PROMPT IF NO TAKE BACKS TO MAIN SCREEN
        if question =="no":
            state = MAIN_SCREEN #CHANGES STATE IF NO
        else:
            student = int(input("Please input (up to 10 digits) for the student number of the individual: ")) # asks number
            snumber+=[student] #just adds to the student number list
            name1 = input ("Please enter the first name of the individual: ") #same thing
            fname+=[name1]#adds to fname list
            name2 = input ("Please enter the last name of the individual: ") # same thing
            lname+=[name2]# adds to lname list
            birthday = input("Please enter the birthday of the individual(mm/dd/yy): ")#smae thing 
            bday+=[birthday]# adds to bday list
            backc = input("Please enter the background country of the individual: ") # same thing 
            country+=[backc] # adds to backroung country lsit 
            city = input ("Please enter the current city in which the individual resides: ") # same hting 
            live+=[city] #add to current city list 
                
           

        length = len(fname) #checks the length of the list as one of the lists as they would all be the same 
        newFile = open ("ABEERDATAPROJ.DAT","w") #opening new file to write 
        dig = 0            
        while True:
            if dig == length: #first checks if dig is equal to the length so knows when to break
                break     
            output = str(snumber[dig])+" "+fname[dig]+" "+lname[dig]+" "+bday[dig]+" "+country[dig]+" "+live[dig] +"\n" #creates an output in format of data files 
            newFile.write (output) #writes into ABEERDATAPROJ.DAT
            dig+=1 #adds dig to get the next piece of data 
        
        newFile.close() 
        output1 = writing() #ADDING NEW RECORD INTO THE DISPLAY AUTOMATICALLY BY ADDING ANOTHER ECTANGLE 
        ssizeList = []
        fnsizeList = []
        lnsizeList = []
        bdsizeList =[]
        ocsizeList =[]
        cysizeList =[]
        ssizeList =  output1[5] 
        fnsizeList = output1[4]
        lnsizeList =output1[3]
        bdsizeList =output1[2]
        ocsizeList =output1[1]
        cysizeList =output1[0]        
        
        
        
        
     
    pygame.display.flip() #UPDATE
    
    # waits long enough to have 60 fps
    myClock.tick(60)


newFile.close()     


pygame.quit() #QUIT 