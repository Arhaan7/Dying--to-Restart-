# Arhaan Wazid Board Game, Dying To Restart

# importing the libraries needed
import pygame
import random


# main function
def main():
    # initializing pygame window
    pygame.font.init()

    # type of font used in the pygame window
    font = pygame.font.SysFont('times new roman', 16)

    # size of the board meaning 8 squares in width and 7 in height, 8x7=56
    width = 8
    height = 7
    # Outputting certain rules to the user watching the game
    print("Note: When a player rolls a three it permits a double move, so the player will move 6 places.")
    print("A player cannot move past end of the board, if it rolls over the board, it will go back to the start.")
    print("When you roll a 4, the game will skip the player's turn.")

    # making a counter so that each player only has 30 turns, game could go on forever as it stops when there is a winner
    counter = 0

    # size of the squares so 50x50 pixels
    square_dim = 50
    # setting up pygame window
    win = pygame.display.set_mode((width * square_dim, height * (square_dim + 10)))
    # making a board with the same pygame dimensions
    board = pygame.Surface((width * square_dim, height * (square_dim + 10)))
    # filling board with a white background
    board.fill((255, 255, 255))
    # setting up colours for the checkerboard
    colour_1 = (0, 0, 0)
    colour_2 = (255, 255, 255)
    curr_colour = colour_1

    # setting up the checkerboard using a nested loop
    for y in range(0, height):
        # draw the row at index i
        for x in range(0, width):
            # drawing a square for the checkerboard everytime
            pygame.draw.rect(board, curr_colour, (x * square_dim, y * square_dim, square_dim, square_dim))
            # updating the screen after every square is drawn
            pygame.display.update()
            # changing the colour of the square after each one is drawn
            if curr_colour == colour_1:
                curr_colour = colour_2
            else:
                curr_colour = colour_1
        # changing the colour of the square after each loop
        if curr_colour == colour_1:
            curr_colour = colour_2
        else:
            curr_colour = colour_1
    # setting up pixel positions for computer players
    pos_x1 = 10
    pos_y1 = 10
    pos_x2 = 10
    pos_y2 = 30
    # displaying a new board and drawing the computer players on to them and updating the display
    win.blit(board, (0, 0))
    # player 1 is red
    player1(win, pos_x1, pos_y1)
    # player 2 is blue
    player2(win, pos_x2, pos_y2)
    # updating the screen and delaying it for the user to see the characters move
    pygame.display.update()
    pygame.time.delay(300)

    while True:
        # adds 1 every time a turn takes place
        counter += 1

        # Player 1's turn
        pos_x1, pos_y1 = handle_player_turn(win, board, font, "Red", pos_x1, pos_y1, player1, pos_x2, pos_y2)
        win.blit(board, (0, 0))
        # displaying the players on the board
        player1(win, pos_x1, pos_y1)
        player2(win, pos_x2, pos_y2)
        # updating the board
        pygame.display.update()
        pygame.time.delay(300)

        # if player 1 is landed on these coordinates then player 1 wins the game
        if pos_y1 == 310 and pos_x1 == 360:
            print("Player 1 wins")
            break

        # Player 2's turn
        pos_x2, pos_y2 = handle_player_turn(win, board, font, "Blue", pos_x2, pos_y2, player2, pos_x1, pos_y1)
        win.blit(board, (0, 0))
        player1(win, pos_x1, pos_y1)
        player2(win, pos_x2, pos_y2)
        pygame.display.update()
        pygame.time.delay(300)

        # if player 2 lands on these coordinates and stays there, then they win the game
        if pos_y2 == 330 and pos_x2 == 360:
            print("Player 2 wins")
            break

        # tie game if they go over 30 turns
        if counter > 30:
            print("Tie game")
            break


#
def handle_player_turn(win, board, font, player_color, pos_x, pos_y, draw_player_function, pos_x2, pos_y2):
    # printing which player's turn
    print("Player's ", player_color, " turn")
    # displaying it on the pygame window
    display_text_on_board(board, font, f"Player {player_color} turn", (20, 350))
    pygame.display.update()

    # rolling the die
    die_1 = roll()
    die_2 = roll()
    spaces = die_1 + die_2
    # showing user what the player rolled
    display_text_on_board(board, font, f"Player {player_color} rolls {spaces}", (20, 400))
    pygame.display.update()

    # special rule if they roll a 3, they get to move double the amount of spaces
    if spaces == 3:
        spaces += spaces
        print(f"Congrats Player {player_color}, you get a double move for rolling a 3")
        print(f"Now you can move {spaces} places")

    # turn is skipped if they roll a 4
    if spaces == 4:
        print(f"OH NO. You rolled a 4. This means we skip your turn")
        spaces = 0
        print(f"You move {spaces} spaces")

    # for loop that makes the players move spaces and updates the board constantly while they are moving
    for i in range(spaces):
        # displaying board
        win.blit(board, (0, 0))
        # drawing the current player whose turn it is to move
        draw_player_function(win, pos_x, pos_y)  # Draw the current player

        # these two if statements draws the other player in the game
        if player_color == "Blue":
            player1(win, pos_x2, pos_y2)
        elif player_color == "Red":
            player2(win, pos_x2, pos_y2)

        # updating the screen
        pygame.display.update()
        pygame.time.delay(500)

        # this if statement moves the player's position forwards and downwards
        # if they roll enough to move down the board
        if pos_x > 310 and pos_y < 310:
            pos_y += 50
            pos_x = 10
        # moves the player horizontally
        else:
            pos_x += 50
        # this is if the red player crosses the end of the board, they have to restart
        if pos_x > 360 and player_color == "Red":
            print(f"Player {player_color}: Rolled over the end of the board. Go back to the start!")
            pos_x = 10
            pos_y = 10
            break

        # if the blue player crosses the board, they have to restart at their original location from the beginning
        elif pos_x > 360 and player_color == "Blue":
            print(f"Player {player_color}: Rolled over the end of the board. Go back to the start!")
            pos_x = 10
            pos_y = 30
            break
        # showing the board with the new locations of the players
        win.blit(board, (0, 0))

        # Save the updated player positions
    return pos_x, pos_y


# function to draw player 1
def player1(win, pos_x1, pos_y1):
    pygame.draw.circle(win, (255, 0, 0), (pos_x1, pos_y1), 8)


# function to draw player 2
def player2(win, pos_x2, pos_y2):
    pygame.draw.circle(win, (0, 0, 255), (pos_x2, pos_y2), 8)


# function that rolls the dice
def roll():
    return random.randint(1, 6)


# function used to draw the text on to the screen
def display_text_on_board(board, font, text, position):
    # Clear the previous text on the screen
    pygame.draw.rect(board, (255, 255, 255), (*position, 300, 50))

    # Display the text on the board
    text_surface = font.render(text, True, (0, 0, 0))
    board.blit(text_surface, position)


# calling main to start the program
main()