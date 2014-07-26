from random import shuffle

cards = ["9", "J", "Q", "K", "10", "A"]
suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
trump = ""

def getDeck():
    deck = list()
    for card in cards:
        for suit in suits:
            deck.append(card + " of " + suit)
            deck.append(card + " of " + suit + "'")
    return deck

def game(playerNames, deck):
    shuffle(deck)
    deal = [deck[0:12], deck[12:24], deck[24:36], deck[36:]]
    hands = dict(zip(playerNames, deal))
    for player in hands:
        printHand(player, hands[player])
    

def printHand(playerName, hand):
    print "\n" +  playerName + "\n" + "----------------------------------------"
    for card in hand:
        printCard(card)
    print "---------"
    print "Meld:"
    print getMeld(hand)
    print "---------"

def printCard(card):
    print(card)
    
def getMeld(hand):
    meld = 0
    flags = list()

    if all (bothCards("A of " + suit, hand) for suit in suits):
        flags.append("A Thousand Aces")
        meld += 1000
    else:
        if all (anyCards("A of " + suit, hand) for suit in suits):
            flags.append("A Hundred Aces")
            meld += 100

    if all (bothCards("K of " + suit, hand) for suit in suits):
        flags.append("800 Kings")
        meld += 800
    else:
        if all (anyCards("K of " + suit, hand) for suit in suits):
            flags.append("80 Kings")
            meld += 80

    if all (bothCards("Q of " + suit, hand) for suit in suits):
        flags.append("600 Queens")
        meld += 600
    else:
        if all (anyCards("Q of " + suit, hand) for suit in suits):
            flags.append("60 Queens")
            meld += 60

    if all (bothCards("J of " + suit, hand) for suit in suits):
        flags.append("400 Jacks")
        meld += 400
    else:
        if all (anyCards("J of " + suit, hand) for suit in suits):
            flags.append("40 Jacks")
            meld += 40

    if any (bothCards("K of " + suit, hand) and bothCards("Q of" + suit, hand) for suit in suits):
        flags.append("Double marriage")
        meld += 300
    else:
        if anyCards("K of Spades", hand) and anyCards("Q of Spades", hand):
            flags.append("Marriage in Spades")
            meld += 20
        if anyCards("K of Diamonds", hand) and anyCards("Q of Diamonds", hand):
            flags.append("Marriage in Diamonds")
            meld += 20
        if anyCards("K of Hearts", hand) and anyCards("Q of Hearts", hand):
            meld += 20
            flags.append("Marriage in Hearts")
        if anyCards("K of Clubs", hand) and anyCards("Q of Clubs", hand):
            meld += 20
            flags.append("Marriage in Clubs")
    if straight(hand):
        meld += 150

    if (bothCards("Q of Spades", hand) and bothCards("J of Diamonds", hand)):
        flags.append("Double Pinochle")
        meld += 300
    else:
        if (anyCards("Q of Spades", hand) and anyCards("J of Diamonds", hand)):
            flags.append("Pinochle")
            meld += 40
    
    for flag in flags:
        print flag
    print ""
    return meld

def getNumCards(card, hand):
    count = 0
    if card in hand:
        count += 1
    if card + "'" in hand:
        count += 1
    return count

def isTrump(suit):
    return (suit == trump)

def straight(hand):
    retVal = [True, True, True, True]
    for i in range(len(suits)):
        for j in range(1,len(cards)):
            if (not ((cards[j] + " of " + suits[i]) in hand)):
                retVal[i] = False
    return any(retVal)

def bothCards(card, hand):
    return (getNumCards(card, hand) == 2)

def oneCard(card, hand):
    return (getNumCards(card, hand) == 1)

def anyCards(card, hand):
    return (getNumCards(card, hand))

def noneCards(card, hand):
    return (getNumCards(card, hand) == 0)

myGame = game(["R", "L", "H", "E"], getDeck())

#print getMeld(["A of Spades", "A of Diamonds", "A of Clubs", "A of Hearts\'"])


#print anyCards("K of Spades", ["K of Spades", "Q of Spades"]) and anyCards("Q of Spades", ["K of Spades", "Q of Spades"])

#print getMeld(["Q of Spades", "J of Diamonds"])
