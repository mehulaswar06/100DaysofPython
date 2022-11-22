from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
new_bidders={}
def max_bidder(bidding_amount):
  highest_bid=0
  for bidder in bidding_amount:
      if bidding_amount[bidder]>highest_bid:
      
          highest_bid=bidding_amount[bidder]
          winner=bidder
  print(f"The Winner is {winner} with a bid of {highest_bid}")

end_of_bid=True
while end_of_bid==True:
  name=input("What is your name:\t")
  bid=int(input("What is your bid:\t"))
  

  
  new_bidders[name]=bid
  
  is_bidder=input("Are there any other bidders, Type 'yes' or 'no'")
    


  if(is_bidder=="yes"):
    clear()
  else:
    end_of_bid=False
    max_bidder(new_bidders)


  

  