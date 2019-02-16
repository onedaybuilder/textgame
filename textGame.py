while True:
    print('Welcome to the maze mirror game. We are trying to find the mystical casino by choosing doors. You have just entered the maze door, there is no goiung back')
    print('You have two options at each step. Left or right. Go the correct way to keep playing for the the mystical casino. Go the wrong way and all the mirrors will cruch on you. Time starts now!!')
    print('Stage one, There are two doors, one glass and the other wood. Which way would you go?')
    
    one = input()
    
    if one == 'right':
        print('Good, you have gone the right way')
        print('Welcome to stage two. This room has two doors, both are glass. Which one do you choose?')
        two = input()
        
        if two == 'left':
            print('Yeah boy! Feeling you')
            print('Welcome to stage three. This room has no doors. Just walk through any wall to find the mystical casino')
            
            three = input()
            if three == 'right':
                print('Genius! You are now at the casino')
            elif three == 'left':
                print('final stage and you failed')

            
                
        elif two == 'right':
            print('Bum head! Get out')
        
    elif one == 'left':
        print('You suck! Go home')
    break

