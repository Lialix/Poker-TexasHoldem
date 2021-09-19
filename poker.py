from random import *
from tkinter import *
from time import *
from PIL import ImageTk, Image
from threading import *
from treys import Card, evaluator
from os import *
chdir('Z:\\travail\projects\poker\image')
print(getcwd())

#--------
#CLASSE
#--------

class Player():
    
    def __init__(self):
        self.jeton = jetonStart
        self.mise = 0
        self.miseGlobal = 0

    def getJeton(self):
        return self.jeton
    
    def getMise(self):
        return self.mise
    
    def setMise(self,x):
        self.mise = x

class Carte():

    def __init__(self,num:str,sign:str):

        self.cardSign = sign
        self.cardNum = num
        self.cardID = self.cardNum+self.cardSign

    def getSign(self):
        return self.cardSign
    
    def getNum(self):
        return self.cardNum

    def getCardID(self):
        return self.cardID
    
    def showCard(self,fen:Tk,x:int,y:int):
        
        imageVar = ImageTk.PhotoImage(Image.open(self.cardID+'.png').resize((90, 120), Image.ANTIALIAS))
        self.img1 = Label(fen,image=imageVar)
        self.img1.place(x = x, y = y)
        return imageVar

    def showFlip(self,fen:Tk,x:int,y:int):
        
        imageVar = ImageTk.PhotoImage(Image.open('dos.png').resize((90, 120), Image.ANTIALIAS))
        self.img1 = Label(fen,image=imageVar)
        self.img1.place(x = x, y = y)
        return imageVar

    def showGreen(self,fen:Tk,x:int,y:int):
        
        imageVar = ImageTk.PhotoImage(Image.open('color.png').resize((100, 130), Image.ANTIALIAS))
        self.img1 = Label(fen,image=imageVar,borderwidth=0, highlightthickness=0)
        self.img1.place(x = x, y = y)
        return imageVar

class Deck():

    def __init__(self):
        self.deck = []
        signR = ["h","d","s","c"]
        number = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        for sign in signR :
                for num in number :
                    self.deck.append(Carte(num,sign))
    
    def shuffle(self):
        self.deck = sample(self.deck, len(self.deck))
    
    def draw(self):
        place = randint(0,(len(self.deck)-2))
        card = self.deck[place]
        self.deck.remove(card)
        return card

class Hand():
    
    def __init__(self,deck:Deck):
            
            self.hand = []
            self.myDeck = deck
    
    def drawCard(self):

        cardDrawn1:Carte = self.myDeck.draw()
        self.hand.append(cardDrawn1)
        return self.myDeck

    def getCard(self,x)-> Carte:
        
        return self.hand[x]

class Boutton():

    def __init__(self,nom:str):

        if nom == "start" :
            self.button = Button(fen,text = "Commencer la partie",command=lambda:initialisation(),bd=10,
            bg="grey",
            fg="red",
            activeforeground="Orange",
            activebackground="blue",
            font="Andalus",
            height=5,
            highlightcolor="purple",
            justify="right",
            padx=40,
            pady=20,
            relief="groove",)
            self.button.place(x=418,y=270)
        
        if nom == "raise" :
            self.button = Button(fen,text = "Raise",command=bidRaise,bd=5,
            bg="grey",
            fg="red",
            activeforeground="Orange",
            activebackground="blue",
            font="Andalus",
            height=1,
            highlightcolor="purple",
            justify="right",
            padx=20,
            pady=10,
            relief="groove")
            self.button.place(x=695,y=600)

        if nom == "fault" :
            self.button = Button(fen,text = "Fault",command=fault,bd=5,
            bg="grey",
            fg="red",
            activeforeground="Orange",
            activebackground="blue",
            font="Andalus",
            height=1,
            highlightcolor="purple",
            justify="right",
            padx=20,
            pady=10,
            relief="groove")
            self.button.place(x=850,y=600)
        
        if nom == "call" :
            self.button = Button(fen,text = "Call",command=call,bd=5,
            bg="grey",
            fg="red",
            activeforeground="Orange",
            activebackground="blue",
            font="Andalus",
            height=1,
            highlightcolor="purple",
            justify="right",
            padx=20,
            pady=10,
            relief="groove")
            self.button.place(x=986,y=600)

        if nom == "leave":
            self.button = Button(fen,text = "Leave table",command = leave,bd=5,
            bg="grey",
            fg="red",
            activeforeground="Orange",
            activebackground="blue",
            font="Andalus",
            height=1,
            highlightcolor="purple",
            justify="right",
            padx=20,
            pady=10,
            relief="groove")
            self.button.place(x=950,y=50)

        if nom == "Rejouer":
            self.button = Button(fen,text = "Rejouer",command = lambda:start(),bd=5,
            bg="grey",
            fg="red",
            activeforeground="Orange",
            activebackground="blue",
            font="Andalus",
            height=1,
            highlightcolor="purple",
            justify="right",
            padx=20,
            pady=10,
            relief="groove")
            self.button.place(x=5000,y=5000)
    
    def displace(self,posx,posy):
        self.button.place(x=posx,y=posy)

    def destroy(self):
        self.button.destroy()
    
    def disableButtons(self):
        self.button['state'] = DISABLED

    def enableButtons(self):
        self.button['state'] = NORMAL
    
    def checkAndCall(self):
        if player1.mise == 0 :
            self.button['text'] = "Check"
        else :
            self.button['text'] = "Call"
        
class ourLabel():
    
    def __init__(self,nom,joueur:Player,posx,posy):
        self.posx = posx
        self.posy = posy
        if nom == 'score' :
            self.label = Label(fen,text="Jetons : " + str(joueur.getJeton()))
            self.label.place(x= posx,y=posy)
            self.label.config(font=("Courier", 20))

        if nom == "pot" :
            self.label = Label(fen,text="Pot : "+ str(round.pot))
            self.label.place(x = posx, y = posy)
            self.label.config(font=("Courier", 20))
        
        if nom == "mise" :
            self.label = Label(fen,text="Mise = " + str(joueur.mise))
            self.label.place(x = posx, y = posy)
            self.label.config(font=("Courier", 20))

    def update(self,joueur:Player):
            self.label.destroy()
            if joueur.mise > joueur.jeton :
                self.label = Label(fen,text="Jetons : 0" )
            else :
                self.label = Label(fen,text="Jetons : " + str(joueur.getJeton()))
            self.label.place(x= self.posx,y=self.posy)
            self.label.config(font=("Courier", 20))

    def updatePot(self):
        self.label.destroy()
        self.label = Label(fen,text="Pot : "+ str(round.pot))
        self.label.place(x = self.posx, y = self.posy)
        self.label.config(font=("Courier", 20))
    
    def updateMise(self,joueur:Player):
        self.label.destroy()
        self.label = Label(fen,text="Mise = " + str(joueur.mise))
        self.label.place(x = self.posx, y = self.posy)
        self.label.config(font=("Courier", 20))
 
class Round():

    def __init__(self):
        self.pot = 0
        if randint(0,1) == 1 :
            self.highBidPlayer = True
        else :
            self.highBidPlayer = False

    def nextRound(self):
        self.highBidPlayer = not self.highBidPlayer
    
    def updatePot(self,joueur1:Player,joueur2:Player):
        self.pot = joueur1.getMise + joueur2.getMise
    
    def reset(self):
        self.pot = 0
        self.highBidPlayer = not self.highBidPlayer

#---------
#FONCTIONS
#---------

#>>>ESSENTIEL

def initialisation():

    global player1
    global player2
    global round
    global listeBoutons
    global buttonCall
    global buttonLeave
    global ennemyMise
    global myMise
    global myLabel
    global tour
    global ennemyLabel
    global pot
    global entryRaise

    player1 = Player()
    player2 = Player()
    tour = 0
    listeBoutons = []

    entryRaise = Entry(fen)
    entryRaise.place(x=680,y=550)
    round = Round()

    buttonRaise = Boutton("raise")
    listeBoutons.append(buttonRaise)
    buttonFault = Boutton("fault")
    listeBoutons.append(buttonFault)
    buttonCall = Boutton("call")
    listeBoutons.append(buttonCall)
    buttonLeave = Boutton("leave")
    buttonStart.destroy()

    myLabel = ourLabel("score",player1,150,550)
    ennemyLabel = ourLabel("score",player2,150,50)
    pot = ourLabel("pot",player1,100,300)
    myMise = ourLabel("mise",player1,170,510)
    ennemyMise = ourLabel("mise",player2,170,90)

    myLabel.update(player1)
    ennemyLabel.update(player2)
    imgJeton()
    start()

def start():
    
    resetBoard()
    for i in listeBoutons:
        i:Boutton
        i.enableButtons()
    buttonFin.displace(5000,5000)
    global numStep
    numStep = 0

    round.reset()
    miseInitiale()
    player1.jeton -= player1.mise
    player2.jeton -= player2.mise

    myDeck = Deck()
    myDeck.shuffle()

    global board
    board = Hand(myDeck)

    global myHand
    global ennemyHand
    myHand = Hand(myDeck)
    ennemyHand = Hand(myDeck)


    myDeck = myHand.drawCard()
    stockImg.append(myHand.getCard(0).showCard(fen,550,510))

    myDeck = myHand.drawCard()
    stockImg.append(myHand.getCard(1).showCard(fen,440,510))

    myDeck = ennemyHand.drawCard()
    stockImg.append(ennemyHand.getCard(0).showFlip(fen,550,20))

    myDeck = ennemyHand.drawCard()
    stockImg.append(ennemyHand.getCard(1).showFlip(fen,440,20))

    allLabelUpdate()

def step():
    
    global numStep
    global board

    round.pot = player1.miseGlobal + player2.miseGlobal
    
    if numStep==0:
        buttonCall.checkAndCall()
        myDeck = board.drawCard()
        stockImg.append(board.getCard(0).showCard(fen,300,250))
        myDeck = board.drawCard()
        stockImg.append(board.getCard(1).showCard(fen,450,250))
        myDeck = board.drawCard()
        stockImg.append(board.getCard(2).showCard(fen,600,250))

    elif numStep==1:
        myDeck = board.drawCard()
        stockImg.append(board.getCard(3).showCard(fen,750,250))

    elif numStep==2:
        myDeck = board.drawCard()
        stockImg.append(board.getCard(4).showCard(fen,900,250))
    
    else :
        verification()
        checkEnd()
   
    numStep = numStep + 1
    allLabelUpdate()
    player1.mise = 0
    player2.mise = 0

def getParam():

    global entryMise
    global entryJeton

    text1 = Label(root,text ="Entrez la mise minimale :", background="#3372AD")
    text1.config(font=("Courier", 10))
    text1.pack(pady = 20)

    entryMise = Entry(root)
    entryMise.pack()

    text2 = Label(root,text ="Entrez les jetons de départ :", background= "#3372AD")
    text2.config(font=("Courier", 10))
    text2.pack(pady = 20)

    entryJeton = Entry(root)
    entryJeton.pack()
    button = Button(root,command=getInfo,text = " START ",width=10,height=3)
    button.pack(pady = 60)

def getInfo():

    global miseMin
    global jetonStart
    global entryJeton
    global entryMise
    miseMin = int(entryMise.get())
    jetonStart = int(entryJeton.get())
    if jetonStart >= miseMin*5:
        root.destroy()
    
def miseInitiale():


    if round.highBidPlayer :
        mise1 = miseMin*2
        mise2 = miseMin*2

    else :
        mise1 = miseMin
        mise2 = miseMin*2

    player1.setMise(mise1)
    player2.setMise(mise2)
    player1.miseGlobal = mise1
    player2.miseGlobal = mise2
    round.pot = (player1.miseGlobal+player2.miseGlobal)

#>>>BOUTON

def bidRaise():

    global entryRaise
    newBid = int(entryRaise.get())
    try :
        
        if player1.mise+newBid > 2*miseMin and newBid <= player1.jeton and newBid >= player1.mise and newBid <= player2.jeton :

            player1.miseGlobal += newBid
            player1.jeton -= newBid

            if player1.mise != 0 :
                player1.mise += newBid

            else :
                player1.mise = newBid
  
            if player2.jeton < player1.mise :

                if player2.mise != 0 :

                    player2.miseGlobal += player2.jeton
                    player2.mise += player2.jeton
                    player2.jeton -= player2.jeton
                    

                else :

                    player2.miseGlobal += newBid
                    player2.jeton -= newBid
                    player2.mise = newBid


            else :
        
                player2.miseGlobal += newBid
                player2.jeton -= newBid

                if player2.mise != 0 :
                    player2.mise += newBid

                else :
                    player2.mise = newBid

            step()

    except :
        print("Bid is not correct !")

def call():

    if player1.mise != 0 and player1.mise < player2.mise:
        diffMise = player2.mise - player1.mise
        player1.jeton -= diffMise
        player1.miseGlobal += diffMise
        player1.mise = player2.mise

    step()
    
def fault():

    lose()

#>>>VISUAL

def showEnnemyCard():

    stockImg.append(ennemyHand.getCard(0).showCard(fen,550,20))
    stockImg.append(ennemyHand.getCard(1).showCard(fen,440,20))

def allLabelUpdate():

    myLabel.update(player1)
    ennemyLabel.update(player2)
    pot.updatePot()
    myMise.updateMise(player1)
    ennemyMise.updateMise(player2)
    swapJeton(img1)

def resetBoard():

    global board
    for i in range (len(board.hand)):
        if i >= 1 :
            stockImg.append(board.getCard(i).showGreen(fen,300,250))
            stockImg.append(board.getCard(i).showGreen(fen,450,250))
            stockImg.append(board.getCard(i).showGreen(fen,600,250))
            if i >= 3 :
                stockImg.append(board.getCard(i).showGreen(fen,750,250))
                if i >= 4 :
                    stockImg.append(board.getCard(i).showGreen(fen,900,250))

def imgJeton():

    global imageVar
    global img1
    imageVar = ImageTk.PhotoImage(Image.open('jeton.png').resize((50, 50), Image.ANTIALIAS))
    img1 = Label(fen,image=imageVar)
    if round.highBidPlayer :
        img1.place(x = 220, y = 450)
    else :
        img1.place(x = 220, y = 135)

def swapJeton(img1:Label):

    if round.highBidPlayer :
        img1.place(x = 220, y = 450)
    else :
        img1.place(x = 220, y = 135)

#>>>END

def verification():

    evaluateur = evaluator.Evaluator()
    boardCard = []
    for i in range (len(board.hand)) :
        carteTemp = board.getCard(i)
        newCarte = carteTemp.cardID
        boardCard.append(Card.new(f"{newCarte}"))
    
    myCard = []

    for i in range (len (myHand.hand)) :
        carteTemp = myHand.getCard(i)
        newCarte = carteTemp.cardID
        myCard.append(Card.new(f"{newCarte}"))

    ennemyCard = []
    
    for i in range (len(ennemyHand.hand)) :
        carteTemp = ennemyHand.getCard(i)
        newCarte = carteTemp.cardID
        ennemyCard.append(Card.new(f"{newCarte}"))

    myScore = evaluateur.evaluate(boardCard,myCard)
    ennemyScore = evaluateur.evaluate(boardCard,ennemyCard)
    print(ennemyScore, myScore)
    if myScore == ennemyScore :
        draw()
    elif myScore > ennemyScore :
        lose()
    else :
        win( )

def lose():
    
    thread = Thread(target = showEnnemyCard)
    thread.start()

    player2.jeton += round.pot
    for i in listeBoutons:
        i:Boutton
        i.disableButtons()

    buttonFin.displace(800,50)

def win():
    
    thread = Thread(target = showEnnemyCard)
    thread.start()

    player1.jeton += round.pot
    for i in listeBoutons:
        i:Boutton
        i.disableButtons()

    buttonFin.displace(800,50)

def draw():

    thread = Thread(target = showEnnemyCard)
    thread.start()

    player1.jeton += player1.miseGlobal
    player2.jeton += player2.miseGlobal
    for i in listeBoutons:
        i:Boutton
        i.disableButtons()

    buttonFin.displace(800,50)

def checkEnd():

    if player1.jeton <= 0 or player2.jeton <= 0 :
            leave()
            buttonFin.destroy()
            buttonLeave.destroy()
    
def leave():

    leaveTable = Toplevel(fen)
    if player1.jeton-player1.mise <= 0 :
        msgLeave = Label(leaveTable, text = "Vous n'avez plus assez de jetons pour jouer... ",width=50)
        imageVar = ImageTk.PhotoImage(Image.open('Defeat.png').resize((600,500), Image.ANTIALIAS))
        victoire = Label(leaveTable,image=imageVar)
        victoire.pack()
        


    else :
        msgLeave = Label(leaveTable, text = "Vous avez réussi à partir avec " + str(player1.jeton+player1.mise)+" jetons!!!",width=50)
        imageVar = ImageTk.PhotoImage(Image.open('Victory.png').resize((600,500), Image.ANTIALIAS))
        victoire = Label(leaveTable,image=imageVar)
        victoire.pack()

    msgLeave.config(font=("Courier", 20))
    msgLeave.pack()
    leaveTable.wm_attributes("-topmost", 1)
    for i in listeBoutons:
        i:Boutton
        i:Boutton.destroy()
    buttonLeave.disableButtons()
    stockImg.append(imageVar)

#------------
#MAIN
#------------

global stockImg
global myDeck
global board
global jetonStart
global numStep

stockImg = []
myDeck = Deck()
board = Hand(myDeck)
root = Tk()
getParam()
root.geometry("500x300")
root.minsize(500,300)
root.maxsize(500,300)
root.configure(background='#3372AD')
root.mainloop()

fen = Tk()
fen.title("Poker")
fen.geometry('1100x700')
fen.minsize(1100,700)
fen.maxsize(1100,700)
fen.configure(background='#70B83B')
buttonStart = Boutton("start")
buttonFin = Boutton("Rejouer")
fen.wm_attributes("-topmost", 1)
fen.mainloop()
