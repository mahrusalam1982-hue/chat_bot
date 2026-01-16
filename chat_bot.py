print('Hi! I am a chatbot. I can:')
print('- Tell you a joke')
print('- Tell you the best football player in your preferred team')
print('- Suggest a game based on your favorite type')
print('- Suggest a musician based on your preference')
print('- Ask you a puzzle')

action = input('\nWhat do you want me to do for you? (Type "off" to exit): ').lower()

while action != 'off':

    if action == 'joke':
        print('Why do sharks live in salt water?\nBecause pepper water makes them sneeze.')

    elif action == 'music':
        music_type = input('What is your music preference? (e.g., rap, rock): ').lower()
        if music_type == 'rap':
            print('You might like: Muslim')
        elif music_type == 'rock':
            print('You might like: Rock Together')
        else:
            print('Sorry, I don\'t have a suggestion for that genre yet.')

    elif action == 'player of football':
        team = input('What is your preferred team? (e.g., Barcelona, Madrid, Liverpool): ').lower()
        if team == 'barcelona':
            print('Lionel Messi is a legendary player from Barcelona.')
        elif team == 'madrid':
            print('Cristiano Ronaldo is a famous player from Madrid.')
        elif team == 'liverpool':
            print('Mohamed Salah is a top player from Liverpool.')
        elif team == 'man city' :
            print ('Kevin De Bruyne is one of the best midfield in football history in all time  ' )
        elif team == 'Bayern Munich':
             print('Robert Lewandowski is the best player number 9 in bayern history')
        elif team == 'Borussia Dortmund' : 
             print('Marco Reus is the best Player for the fans.  ')   
        else:
            print('I don\'t know a player from that team.')

    elif action == 'game':
        game_type = input('What is your preferred type of game? (e.g., survival, battle royale): ').lower()
        if game_type == 'survival':
            print('You might enjoy playing Minecraft.')
        elif game_type == 'battle royale':
            print('You might enjoy playing Fortnite.')
        else:
            print('I don\'t have a suggestion for that type yet.')

    elif action == 'puzzle':
        level = input('What is the level of the puzzle? (easy/hard): ').lower()
        score = 0

        if level == 'easy':
            answer1 = input('What has keys but can’t open locks? ').lower()
            if answer1 == 'piano':
                print('Correct!')
                score += 1
            else:
                print('Incorrect. The correct answer was: piano')

            answer2 = input('What has a neck but no head? ').lower()
            if answer2 == 'bottle':
                print('Correct!')
                score += 1
            else:
                print('Incorrect. The correct answer was: bottle')

            print(f'Your total score: {score}/2')

        else:
            print('Hard puzzles not available yet.')

    else:
        print('Sorry, I don\'t understand that action.')

    # Ask again
    action = input('\nWhat do you want me to do for you? (Type "off" to exit): ').lower()

print('Goodbye!')
