print("Welcome to the game!")

secret_word =  "knowledge"
length = len(secret_word)
letters_input = []
won = False

print("The length of the secret word is: ", length)

while True:
    attempts = 7
    for letter in secret_word:
        if letter.lower() in letters_input:
                print(letter, end=" ")
        else :
                ("_")
        print(" ")
       

    choose = input("What is the letter? ")
    letters_input.append(choose.lower())
    
    if choose.lower() not in secret_word.lower():
        attempts = attempts - 1
            
        
    won = True
    #verifica se tem alguma letra que ainda não ganhou
    for letter in secret_word:
        if letter.lower() not in letters_input:
            won = False
        
    if attempts == 0 or won:
        print("finished")

    if won:
        print(f"Congrats, you won! The word is: {secret_word}")
    else:
        print(f"You lost! The word is: {secret_word}")