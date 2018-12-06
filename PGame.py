import random
cardPlacement = 0
placementPoint = 0
transitCount = 0
deckCount = 0
outDeckCount = 0

class CircularQueue():
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 52
    
    def enqueue(self, data):
        if (self.size() == self.maxSize-1):
            return ("queue full")
        self.queue.append(data)
        self.tail = (self.tail +1) % self.maxSize
        return True
    
    def dequeue(self):
       if self.size()==0:
            return ("Queue Empty!") 
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data 

    def seeHead():
        return self.queue[self.head]

    def size(self):
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.maxSize - (self.head-self.tail))

    
def play(numPlayers):
    #shuffle
    #deal 2 each
    #shuffle player order
    #you will always be player 0    

    for x in range(numPlayers):
        playerStack[x] = x

    random.shuffle(playerStack)

    deckQ = shuffle() # cards
    dealOut(playerStack)
    #intial bet
    #


def dealOut(playerStack):
    outDeck = []

    for y in range(0,2,1):
        for x in playerStack:
            playerStack[y,x] = deckQ.seeHead()
            outDeck[outDeckCount] = deckQ.dequeue()
            outDeckCount+=1
 
    
    tableCards = []
    for i in range(0,3,1):
        tableCards[i] = deckQ.seeHead()
        outDeck[outDeckCount] = deckQ.dequeue()
        outDeckCount+=1



def shuffle():
    deckQ = CircularQueue()
    #0-12 hearts
    #13-25 spades
    #26-38 diamonds
    #29-51 clubs
    for i in range(0,52,1):
        deckArr[i] = i
    random.shuffle(deckArr)
    for i in deckArr:
        deckQ.enqueue(deckArr[i])
    return deckQ

top = " ____ "
upper = "/    \""
midUPLow = "|    |"
content = str("| " + i +  " |")
lower = "\____/"

cardImg = [top, upper, midUPLow, midUPLow, lower]
def drawcards(tableCards):
    for i in range(0,6,1):
        if (i==3):
            for k in tableCards:
                content = str("| " + i +  " |")
                #concat content
        for j in tableCards:
            cardImg[]

def cardnumrules(num):
    result = []
    if (num > -1 and num < 13):
        result[1] = 'H'
    elif (num > 12 and num < 26):
        result[1] = 'S'
        num = num-13
    elif (num > 25 and num < 39):
        result[1] = 'D'
        num = num-26
    else:
        result[1] = 'C'
        num = num-39
    
    #------------------------
    if(num > -1 and num < 9):
        result[0] = num+2
    elif (num == 12):
        result[0] = 'A'
    elif (num == 11):
        result[0] = 'K'
    elif (num == 10):
        result[0] = 'Q'
    else:
        result[0] = 'J'
    return result
def evaluate(tableCards, playerStack):
    