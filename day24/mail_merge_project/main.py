#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

LETTER_FILE = 'Input/Letters/starting_letter.txt'
NAMES_FILE = 'Input/Names/invited_names.txt'
OUTPUT_PATH = 'Output/ReadyToSend/'

with open(LETTER_FILE, mode="r") as letter_file:
    letter = letter_file.read()

with open(NAMES_FILE, mode="r") as names_file:
    names = names_file.readlines()


for name in names:
    name = name.rstrip()
    new_letter = letter.replace("[name]", name)
    new_letter = new_letter.replace("Angela", "Justin")
    out_file_path = OUTPUT_PATH + f"{name}.txt"
    with open(out_file_path, mode='w') as out_file:
        out_file.write(new_letter)
