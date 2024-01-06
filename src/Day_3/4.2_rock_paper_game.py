import random

rock = '''
"!!!ROCK IT, MAN!!!
 !!!GO, MAN, GO!!!"                       _____
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
           /---._.---._.---\        /       /
           \||   '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/
jro'''

scissor = '''⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣶⣶⣦⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢻⣿⣿⡟⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡿⠛⢉⣉⡉⠛⠻⠿⣧⣤⣉⠋⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⠁⢸⣿⣿⣿⣷⣦⡀⠀⠈⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣧⡈⠻⢿⣿⣿⡿⠇⢠⣶⣦⣄⠀⠀⠀⠈⠉⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣶⣤⣤⣤⣤⣶⣿⣿⡇⠙⠻⢶⣤⣀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠹⣿⣿⣦⣄⡀⠀⠀⠀⠀⠈⠻⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠙⣿⣿⣿⣿⣷⣦⣄⡀⠀⠀⠈⢿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠈⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿'''

paper = '''        /')    ./')             ('\.    ('\
      /' /.--''./'')           (''\.''--.\ '\
 :--''  ;    ''./'')           (''\.''    ;  ''--:
 :     '     ''./')             ('\.''     '     :
 :           ''./'               '\.''           :
 :--''-..--''''                     ''''--..-''--:
 dp'''

game_iamge = [rock,paper,scissor]
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))
print(game_iamge[user_choice])
computer_choice = random.randint(0,2)
print("computer_chose:")
print(game_iamge[computer_choice])
if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice >=3 or user_choice < 0:
    print("you typed an invalid number, you lose!")
elif computer_choice == 2 and user_choice == 2:
    print("you lose")
elif computer_choice>user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it's a draw")
