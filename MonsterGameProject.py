
from random import randint

game_choice = True


def calculate_monster_attack(m_attack_min, m_attack_max):
    return randint(m_attack_min, m_attack_max)


def calculate_player_attack(p_attack_min, p_attack_max):
    return randint(p_attack_min, p_attack_max)


while game_choice:

    player_name = input('Please enter your name: ')
    player = {'name': player_name, 'p_attack_min': 8, 'p_attack_max': 12, 'heal': 16, 'health': 100}
    monster = {'name': 'Monster', 'm_attack_min': 10, 'm_attack_max': 15, 'health': 100}

    loop_choice = True
    while loop_choice:

        player_choice = input("Please select action \n 1.Attack \n 2.Heal \n 3.Show scores \n 4.Exit \n")

        if player_choice == '1':
            print('{} is attacking'.format(player['name']))
        elif player_choice == '2':
            print('{} is healing'.format(player['name']))
        elif player_choice == '3':
            print(monster['name'], "'s point: ", monster['health'])
            print(player['name'], "'s point: ", player['health'])
        elif player_choice == '4':
            print("You're leaving the game!")
            loop_choice = False
            game_choice = False
        else:
            print('Invalid input \n')

        if player_choice == '1':
            monster['health'] = monster['health'] - calculate_player_attack(player['p_attack_min'], player['p_attack_max'])
            # print(monster['name'], "'s point: ", monster['health'])
            # print(player['name'], "'s point: ", player['health'])
            if monster['health'] <= 0:
                print(monster['name'], "'s point: ", monster['health'])
                print(player['name'], "'s point: ", player['health'])
                print('Player won!')

                keep_play = True
                while keep_play:
                    cont_play_p = input('Do you want to keep playing?(y/n): ').lower()
                    if cont_play_p == 'y':
                        print('\n -----New Game----- \n')
                        keep_play = False
                        loop_choice = False
                    elif cont_play_p == 'n':
                        print("You're leaving the game!")
                        keep_play = False
                        loop_choice = False
                        game_choice = False
                    else:
                        print('Invalid input')
                        keep_play = True
            else:
                print('Now, monster attacks')
                player['health'] = player['health'] - calculate_monster_attack(monster['m_attack_min'], monster['m_attack_min'])
                print(monster['name'], "'s point: ", monster['health'])
                print(player['name'], "'s point: ", player['health'])
                if player['health'] <= 0:
                    print('Monster won!')

                    keep_play = True
                    while keep_play:
                        cont_play_p = input('Do you want to keep playing?(y/n): ').lower()
                        if cont_play_p == 'y':
                            print('\n -----New Game----- \n')
                            keep_play = False
                            loop_choice = False
                        elif cont_play_p == 'n':
                            print("You're leaving the game!")
                            keep_play = False
                            loop_choice = False
                            game_choice = False
                        else:
                            print('Invalid input')
                            keep_play = True

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']
            player['health'] = player['health'] - calculate_monster_attack(monster['m_attack_min'], monster['m_attack_min'])
            print(monster['name'], "'s point: ", monster['health'])
            print(player['name'], "'s point: ", player['health'])
