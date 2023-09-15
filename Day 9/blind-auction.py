from art import logo
import os
def clear():
    os.system('cls')

print(logo)
print("Welcome to the secret auction program.\n")


bid_directory={}
option=True
while(option):
    name=str(input("What is your name?: "))
    bid=int(input("What's your bid?: $"))
    choice=str(input("Are there any other bidders? Type 'yes' or 'no'.\n"))

    # Adding Valuse in bid_directory dictionary
    bid_directory[name]=bid
    if(choice=='no'):
        option=False
        clear()
        bid_list=list(bid_directory.values())
        max=bid_list[0]
        for i in bid_list:
            if(max<i):
                max=i
        
        for i in bid_directory:
            if(bid_directory[i]==max):
                print(f"The winner is {i} with a bid of ${max}.")
    elif(choice=='yes'):
        option=True
        clear()
    else:
        print("Wrong option")
