def count(word,ltf):
    # ltf = letter to find
    counter = 0

    for letter in word:
        if letter == aletter :
            counter = counter + 1
    print(counter)

word = input('what is your word?: ')
aletter = input('what letter are you counting?: ')
count(word, aletter)
