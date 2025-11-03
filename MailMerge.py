PLACEHOLDER = "[Name]"


with open("./Input/Names/Names_List.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letter/Starting_Letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./Output/Ready_To_Send_Files/Letter_For_{stripped_name}.docx", mode = "w") as completed_letter:
            completed_letter.write(new_letter)
