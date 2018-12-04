import random
cardPlacement = 0

def play(numPlayers):
    #shuffle
    #deal 2 each
    #shuffle player order

    for x in range(numPlayers):
        playerStack[x] = x

    random.shuffle(playerStack)

    deck = shuffle() # cards

  
    for y in range(0,2,1):
        for x in playerStack:
            playerStack[y,x] = deck[count]
            cardPlacement+=1
    
    tableCards

def shuffle():
    #0-12 hearts
    #13-25 spades
    #26-38 diamonds
    #29-51 clubs
    for i in range(0,52,1):
        deckArr[i] = i
    random.shuffle(deckArr)
    return deckArr

 