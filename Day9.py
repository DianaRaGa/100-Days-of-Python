from Modules.Day9_Blind_auction import logo

# Initiating variables
biding_auction = {}
other_biters = True

#While loop to create as many entries in the dictionary as posible
while other_biters:
    print(logo)
    print("\nWelcome to the Blind Biding Auction.")
    name = input("Please enter your name: ")
    try:#Have to see how to make this part a while loop also to only get numbers and then keep going, maybe with an if function?
        amount = float(input("Please enter your bid amount (only numbers allowed): "))
    except ValueError:
        print("Please enter a correct bid as a number")

    #Appending the data to the dictionary
    biding_auction[name] = amount

    # Handling other biders
    question = input("Is there any other biders? Please answer 'yes' or 'no' only: ").lower()
    if question == "no":
        print("\n"*100)
        other_biters = False
    else:
        print("\n"*100)
        continue

#Cheking for the highest bid
max_key = max(biding_auction, key=biding_auction.get)#the get function does not need the () or it will get an error
max_value = biding_auction[max_key]
print(f"The winner is {max_key} with a bid of {max_value}")
