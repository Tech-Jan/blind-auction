# HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

more_bidders = True
bidders_dict = {}


def highesbidda():
    highest_bid = 0
    highest_bidder = ""
    for bidders in bidders_dict:
        money = bidders_dict[bidders]
        if int(money) > int(highest_bid):
            highest_bid = money
            highest_bidder = str(bidders)
    return highest_bidder + " with highest bid: " + highest_bid


while more_bidders == True:
    name = input("what name? ")
    amount = input("money much? ")
    more_bidders_string = input("more bidders? [yes]? ")
    if more_bidders_string != "yes":
        more_bidders = False
    bidders_dict[name] = amount
    print(logo)

highersbit = highesbidda()
print(highersbit)
print(bidders_dict)

