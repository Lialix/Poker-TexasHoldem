from random import *
from tkinter import *
from time import *
from PIL import ImageTk, Image


class Deck:

    def __init__(self):
        self.deck = []
        colorR = "R"
        colorB = "B"
        signR = ["H","D"]
        signB = ["C","S"]
        number = ["2","3","4","5","6","7","8","9","10","11","12","13","14"]
        for color in colorR:
            for sign in signR :
                for num in number :
                    self.deck.append(Card(color,sign,num))
        for color in colorB:
            for sign in signB :
                for num in number :
                    self.deck.append(Card(color,sign,num))
        self.deck.append(Card("dos","",""))
    
    def shuffle(self):
        self.deck = sample(self.deck, len(self.deck))
    
    def draw(self):
        place = randint(0,(len(self.deck)-2))
        card = self.deck[place]
        self.deck.remove(card)
        return card

class Card():

    def __init__(self,color:str,sign:str,num:str):

        self.cardColor = color
        self.cardSign = sign
        self.cardNum = num
        self.cardID = self.cardColor+self.cardSign+self.cardNum

    def getColor(self):
        return self.cardColor

    def getSign(self):
        return self.cardSign
    
    def getNum(self):
        return self.cardNum

    def getCardID(self):
        return self.cardID
    
    def showCard(self,fen:Tk,x:int,y:int):

        imageVar = ImageTk.PhotoImage(Image.open(self.cardID+'.png').resize((90, 120), Image.ANTIALIAS))
        img1 = Label(fen,image=imageVar)
        img1.place(x = x, y = y)
        return imageVar

    def showFlip(self,fen:Tk,x:int,y:int):
        
        imageVar = ImageTk.PhotoImage(Image.open('dos.png').resize((90, 120), Image.ANTIALIAS))
        img1 = Label(fen,image=imageVar)
        img1.place(x = x, y = y)
        return imageVar

class Hand():
    
    def __init__(self,deck:Deck):
            
            self.hand = []
            self.myDeck = deck
    
    def drawCard(self):

        cardDrawn1:Card = self.myDeck.draw()
        self.hand.append(cardDrawn1)
        return self.myDeck

    def getCard(self,x)-> Card:
        
        return self.hand[x]

class Player():
    
    def __init__(self):
        self.jeton = 50
        self.mise = 0

    def addJeton(self,jeton):
        self.jeton += jeton

    def subJeton(self,jeton):
        self.jeton -= jeton

    def getJeton(self):
        return self.jeton
    
    def getMise(self):
        return self.mise
    
    def setMise(self,x):
        self.mise = x

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
            self.button.place(x=1005,y=600)

        if nom == "leave":
            self.button = Button(fen,text = "Leave table",command=leave,bd=5,
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

    def destroy(self):
        self.button.destroy()
    
    def disableButtons(self):
        self.button['state'] = DISABLED

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
                self.label = Label(fen,text="Jetons : " + str(joueur.getJeton()-joueur.mise))
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


def start():

    if not end :
        round.reset()
        myDeck = Deck()
        myDeck.shuffle()
        Board = Hand(myDeck)
        miseInitiale()
        checkEnd()

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

        if round.highBidPlayer :
            player2.setMise(player1.mise)

        allLabelUpdate()

def flop():
    ("faire ca !")
    
def bidRaise():

    print("hello")

def call():

    player1.mise = player2.mise
    

def fault():

    lose()
    start()

def leave():

    leaveTable = Toplevel(fen)
    if player1.jeton-player1.mise < 0 :
        msgLeave = Label(leaveTable, text = "Il ne vous reste plus de jetons... ",width=50)
    else :
        msgLeave = Label(leaveTable, text = "Vous avez réussi à partir avec " + str(player1.jeton-player1.mise)+" jetons!!!",width=50)
    msgLeave.config(font=(30))
    msgLeave.pack()
    for i in listeBoutons:
        i:Boutton
        i.disableButtons()
    buttonLeave.disableButtons()
    end = True
    
def checkState():

    print("hello")

def miseInitiale():

    if round.highBidPlayer :
        mise1 = 20
        mise2 = 10

    else :
        mise1 = 10
        mise2 = 20

    round.pot += (mise1+mise2)
    player1.setMise(mise1)
    player2.setMise(mise2)

def game():
    print("ahah")

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

def allLabelUpdate():

    myLabel.update(player1)
    ennemyLabel.update(player2)
    pot.updatePot()
    myMise.updateMise(player1)
    ennemyMise.updateMise(player2)
    swapJeton(img1)

def initialisation():

    global player1
    player1 = Player()
    global player2
    player2 = Player()
    entryRaise = Entry(fen)
    entryRaise.place(x=680,y=550)
    global round
    round = Round()

    global listeBoutons
    listeBoutons = []
    buttonRaise = Boutton("raise")
    listeBoutons.append(buttonRaise)
    buttonFault = Boutton("fault")
    listeBoutons.append(buttonFault)
    buttonCall = Boutton("call")
    listeBoutons.append(buttonCall)
    global buttonLeave
    buttonLeave = Boutton("leave")
    buttonStart.destroy()

    global tour
    tour = 0
    global myLabel
    myLabel = ourLabel("score",player1,150,550)
    global ennemyLabel
    ennemyLabel = ourLabel("score",player2,150,50)
    global pot
    pot = ourLabel("pot",player1,100,300)
    global myMise
    myMise = ourLabel("mise",player1,170,510)
    global ennemyMise
    ennemyMise = ourLabel("mise",player2,170,90)
    myLabel.update(player1)
    ennemyLabel.update(player2)
    
    imgJeton()
    start()

def lose():
    
    player1.jeton -= player1.mise
    player2.jeton += player1.mise
    
def win():
    
    player2.jeton -= player2.mise
    player1.jeton += player2.mise

def checkEnd():
    if round.highBidPlayer :
        x = 20
        y = 10
        if player1.jeton >= 100 or player2.jeton-y < 0 or player1.jeton <= 0 or player1.jeton-x < 0 :
            leave()
    else  :
        x = 10
        y = 20
        if player1.jeton >= 100 or player2.jeton-y < 0 or player1.jeton <= 0 or player1.jeton-x < 0 :
            leave()
    

stockImg = []
global end
end = False
fen = Tk()
fen.title("Poker")
fen.geometry('1100x700')
fen.configure(background='#70B83B')
buttonStart = Boutton("start")
fen.mainloop()
