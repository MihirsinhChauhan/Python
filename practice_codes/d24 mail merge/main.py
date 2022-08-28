# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(".\Input\Names\invited_names.txt") as invitedNames:
    names = invitedNames.readines()
    print(names)

with open(".\Input\Letters\starting_letter.txt") as startingLetter:
    letter = startingLetter.read()
    for people in names:
        people.strip()
        newLetter = letter.replace("[name]", people)

        with open(f".\Output\ReadyToSend\invite {people}.txt", mode="w") as createLetter:
            createLetter.write(newLetter)
