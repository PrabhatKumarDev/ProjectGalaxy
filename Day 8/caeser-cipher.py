from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(message,shift,direction):
    shift=shift%26
    if(direction=="encode"):
        message=message.lower()
        cipher_text=""
        for char in message:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position+shift
                cipher_text+=alphabet[new_position]
            else:
                cipher_text+=char
        print(f"Here's the {direction}d result: {cipher_text}")

    elif(direction=="decode"):
        message=message.lower()
        plain_text=""
        for char in message:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position-shift
                plain_text+=alphabet[new_position]
            else:
                plain_text+=char
        print(f"Here's the {direction}d result: {plain_text}")

    else:
        print("Wrong input!")
    

print(logo)
choice=True
while(choice):
    direction=str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"))
    message=str(input("Type your message:\n"))
    shift=int(input("Type your shift number:\n"))
    caeser(message,shift,direction)
    option=str(input("Type 'yes' if you want to go again. Otherwise type 'no'.\n"))
    if(option=='yes'):
        choice=True
    elif(option=="no"):
        choice=False
    else:
        print("Wrong input")
