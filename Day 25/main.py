import pandas
df=pandas.read_csv("Day 25/nato_phonetic_alphabet.csv")


student_dict={row.letter:row.code for (index,row) in df.iterrows()}

def phonetic(): 
    user_input=input("Enter a word: ").upper()
    try:
        user_list=[student_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        phonetic()
    else:
        print(user_list)

phonetic()


