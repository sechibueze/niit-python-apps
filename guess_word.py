
choice = 'wisdom'

size = len(choice)

choice_hash = "*" * size
is_game_over = False
trial = 0
while trial <= 3:
    display_hash = choice_hash
    print(display_hash)
    guess = input('Guess : ')
    if guess in choice:
        for ii in range(len(choice)):
            display_hash = choice_hash[:ii] + guess + choice_hash[ii+1:]
            print(display_hash)
    trial += 1
print(choice_hash)