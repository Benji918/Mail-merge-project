# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open('Input/Names/invited_names.txt') as invited_names:
    names = invited_names.readlines()
    formated_names = []
    for name in names:
        stripped_name = name.strip('\n')
        # Append stripped names to empty list
        formated_names.append(stripped_name)
# Replace the [name] placeholder with the actual name.
with open(file='Input/Letters/starting_letter.txt') as letter_template:
    letter = str(letter_template.read())
    for name in formated_names:
        letter_replace = letter.replace('[name]', name)
        # Save the letters in the folder "ReadyToSend".
        with open(file=f'Output/ReadyToSend/letter_for_{name}.txt', mode='w') as named_invitation:
            named_invitation.write(letter_replace)
