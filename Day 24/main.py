PLACEHOLDER="[name]"

#for each name in invited_names.txt
with open("Day 24/input/Names/invited_names.txt") as names_file:
    each_names=names_file.readlines()

with open("Day 24/input/Letters/starting_letter.txt") as l:
    letter=l.read()
    for name in each_names:
        name=name.strip()
        new_letter=letter.replace(PLACEHOLDER,name)
        with open(f"Day 24\Output\ReadyToSend/letter_for_{name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)
