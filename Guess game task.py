import random
count=0


while True:
    level_request=input('There are 3 levels in number guessing game.Enter Hard, medium or easy:').upper()
    if level_request=='EASY':
        guess_limit=6
        secrete_number=random.randint(1,10)
        while count<guess_limit:
                try:
                    user_guess=int(input('Guess a number between 1 and 10: '))
                    count=count+1
                    guess_info=guess_limit-count
                    if user_guess==secrete_number:
                        print('You Won!')
                        break
                    if guess_info >= 2:
                        print('You have',guess_info,'guesses left')
                    elif guess_info<=1:
                        print('You have',guess_info,'guess left')

                except:
                    print('invalid value,enter a numeric value')

        else:
            print('sorry you failed')
        break
    elif level_request=='MEDIUM':
        guess_limit=4
        secrete_number=random.randint(1,20)
        while count<guess_limit:
                try:
                    user_guess=int(input('Guess a number between 1 and 20: '))
                    count=count+1
                    guess_info=guess_limit-count
                    if user_guess==secrete_number:
                        print('You Won!')
                        break
                    if guess_info >= 2:
                        print('You have',guess_info,'guesses left')
                    elif guess_info<=1:
                        print('You have',guess_info,'guess left')
                except:
                    print('invalid value,enter a numeric value')
        else:
            print('sorry you failed')
        break
    elif level_request=='HARD':
        guess_limit=3
        secrete_number=random.randint(1,50)
        while count<guess_limit:
                try:
                    user_guess=int(input('Guess a number between 1 and 50: '))
                    count=count+1
                    guess_info=guess_limit-count
                    if user_guess==secrete_number:
                        print('You Won!')
                        break
                    if guess_info >= 2:
                        print('You have',guess_info,'guesses left')
                    elif guess_info<=1:
                        print('You have',guess_info,'guess left')
                except:
                    print('invalid value,enter a numeric value')
        else:
            print('sorry you failed')
        break
    else:
        print('Invalid input')