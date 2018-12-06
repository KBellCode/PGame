import random
cardPlacement = 0
placementPoint = 0
transitCount = 0
deckCount = 0

def play(numPlayers):
    #shuffle
    #deal 2 each
    #shuffle player order

    for x in range(numPlayers):
        playerStack[x] = x

    random.shuffle(playerStack)

    #you will always be player 0

    deck = shuffle() # cards
    transitDeck = []
  
    for y in range(0,2,1):
        for x in playerStack:
            playerStack[y,x] = deck[cardPlacement]
            transitDeck[transitCount] = deck[cardPlacement]
            cardPlacement+=1
    
    tableCards = []
    tableCards[0] = deck

def shuffle():
    #0-12 hearts
    #13-25 spades
    #26-38 diamonds
    #29-51 clubs
    for i in range(0,52,1):
        deckArr[i] = i
    random.shuffle(deckArr)
    return deckArr

 