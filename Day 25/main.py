import pandas
df=pandas.read_csv("Day 25/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
student_dict={row.letter:row.code for (index,row) in df.iterrows()}
user_input=input("Enter a word: ")
user_input=user_input.upper()
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_list=[student_dict[i] for i in user_input if i in student_dict]
print(user_list)

