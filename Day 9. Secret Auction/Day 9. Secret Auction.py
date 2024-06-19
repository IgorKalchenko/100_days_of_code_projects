from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
auction_dict = {}
def auction():


    def auction_quiz():
        bidder_name = str(input("What is your name?\n"))
        bid = int(input("What is your bid?\n$"))
        auction_dict[bidder_name] = bid
    auction_quiz()
    auction_time = True
    while auction_time == True:
        bidders_left = input("Are there any other bidders? Type 'yes' or 'no'. \n")
        if bidders_left == "yes":
            clear()
            auction_quiz()
        else:
            auction_time = False
            bidder_name = 0
            count = 0
            for b in auction_dict:
                if count < auction_dict[b]:
                    count = auction_dict[b]
                    bidder_name = b
            print(f"The winner is {bidder_name} with a bid of ${count}")
auction()