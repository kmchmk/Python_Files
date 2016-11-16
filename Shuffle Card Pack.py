import random
num = [6,7,8,9,10,"J","Q","K","A"]
symbol = ["Hearts - haaratha", "Diamonds - ruvutha", "Clubs - kalaabara", "Spades - iskoppa"]

deck = [""] * len(num) * len(symbol)
for i in range(len(num)):
    for j in range(len(symbol)):
        deck[len(symbol)*i + j] = str(num[i]) + symbol[j]

newdeck = [""]* len(deck)
for i in range(len(deck)):
    index = random.randint(0,len(deck)-1)
    newdeck[i] = deck[index]
    deck = deck[:index]+deck[index+1:]

for i in newdeck:
    print i

for i in range(40):
    print ""

print "Scroll up to see the card pack.\nNow press enter..."
print "",

for i in newdeck:
    raw_input()
    print i

