
def main():

    line, wager = get_input()
    odds = get_odds(line)
    payout = get_payout(odds, wager)
    display(odds, payout)
    


def get_input():
    
    line = float(input("Enter Line: "))
    wager = float(input("Your Wager: "))
    return line, wager

def get_odds(line):
    
    if line > 0:
        odds = (line/100) + 1
    else:
        odds = (100/-line) + 1
    return odds

def get_payout(odds, wager):
    payout = odds * wager
    return payout
    
def display(odds, payout):

    print(f"Odds: {odds:,.2f}")
    print(f"Payout: ${payout:,.2f}")

main()
