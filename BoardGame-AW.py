#Arhaan Wazid Board Game, Dying To Restart


import pygame
import random


# main function
def main():

    pygame.font.init()

    font = pygame.font.SysFont('times new roman', 16)


    # size of the board meaning 8 squares in width and 7 in height, 8x7=56
    width = 8
    height = 7
    print("Note: When a player rolls a three it permits a double move, so the player will move 6 places.")
    print("A player cannot move past end of the board, if it rolls over the board, it will go back to the start.")
    print("When you roll a 4, the game will skip the player's turn.")

    counter = 0


    # size of the squares so 50x50 pixels
    square_dim = 50
    # setting up pygame window
    win = pygame.display.set_mode((width * square_dim, height * (square_dim+10)))
    # making a board with the same pygame dimensions
    board = pygame.Surface((width * square_dim, height * (square_dim+10)))
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
    pygame.display.update()
    # making a while loop for the computers to play against each other until one of them wins

    while True:


        # player 1 turn
        print("Player 1 turn (Red)")
        # Player 1 turn
        display_text_on_board(board, font, "Player 1 turn (Red)", (20, 350))
        pygame.display.update()
        # Rolling the dice
        die_1 = roll()
        die_2 = roll()
        space = die_1 + die_2
        display_text_on_board(board, font, f"Player 1 rolls {space}", (20, 400))
        pygame.display.update()

        # if player 1 rolls a three they get a double move, so they actually move 6 places
        # this qualifies as features from table "Double Moves"
        if space == 3:
            space += space
            print("Congrats Player 1, you get a double move for rolling a 3")
            print("Now you can move ", space, "places")
        # if the player rolls a sum of 4, the game automatically skips their turn
        # this qualifies as "Missed Turns" from the table 1 features
        if space == 4:
            space = 0
            print("OH NO. You rolled a 4. This means we skip your turn")
            print("You move", space, "spaces")

        # loop for many spaces player 1 moves
        for i in range(space):
            # drawing the board after every loop and displaying player 1 and player 2 and player 1's new position
            win.blit(board, (0, 0))
            player1(win, pos_x1, pos_y1)
            player2(win, pos_x2, pos_y2)
            # if player is in the end of the board then they move down a row and start from the left of the row
            # they then move from left to right again until one of them wins the game
            if pos_x1 > 310 and pos_y1 < 310:
                pos_y1 += 50
                pos_x1 = 10
            # if player is not at the end of the board they just go again from left to right, each move is worth
            # 50 pixels to the right
            else:
                pos_x1 += 50
            # if they go past the board in the bottom right corner then they have to restart from the beginning
            # this qualifies as features from table 1 "Exact Requirements"
            if pos_x1 > 360:
                print("Player 1: Rolled over the end of the board. Go back to the start!")
                pos_x1 = 10
                pos_y1 = 10
                break
            # delaying and updating screen after each loop
            pygame.display.update()
            pygame.time.delay(300)

        # displays the player in the last box, if they reached there or else it will just end the game
        win.blit(board, (0, 0))
        player1(win, pos_x1, pos_y1)
        player2(win, pos_x2, pos_y2)
        pygame.display.update()
        pygame.time.delay(300)
        # checks to see if player 1 is at the exact coordinates of the last box and if they are then they won the game
        if pos_y1 == 310 and pos_x1 == 360:
            print("Player 1 wins")
            # breaking the loop and ending the game
            break

            #Player 1 turn
        display_text_on_board(board, font, "Player 2 turn (Blue)", (20, 350))
        pygame.display.update()
        # Rolling the dice
        die_1 = roll()
        die_2 = roll()
        spaces_2 = die_1 + die_2

        display_text_on_board(board, font, f"Player 2 rolls {spaces_2}", (20, 400))
        pygame.display.update()
        # if player 2 rolls a three they get a double move, so they are actually moving 6 places instead of 3
        # this qualifies as features from table "Double Moves"
        if spaces_2 == 3:
            space += space
            print("Congrats Player 2, you get a double move for rolling a 3")
            print("Now you can move ", space, "places")

        # if the player rolls a sum of 4, the game automatically skips their turn
        # this qualifies as "Missed Turns" from the table 1 features
        if spaces_2 == 4:
            print("OH NO. You rolled a 4. This means we skip your turn")
            spaces_2 = 0
            print("You move", spaces_2, "spaces")
        # starting for loop for player 2 and how many times they move in the board
        for j in range(spaces_2):
            # drawing the board after every loop and displaying player 1 and player 2
            win.blit(board, (0, 0))
            player1(win, pos_x1, pos_y1)
            player2(win, pos_x2, pos_y2)
            # if player is in the end of the board then they move down a row and start from the left of the row
            # they then move from left to right again until one of them wins the game
            if pos_x2 > 310 and pos_y2 < 330:
                pos_y2 += 50
                pos_x2 = 10
            # if player is not at the end of the board they just go again from left to right, each move is worth
            # 50 pixels to the right
            else:
                pos_x2 += 50
            # if they go past the board in the bottom right corner then they have to restart from the beginning
            # this qualifies as features from table 1 "Exact Requirements"
            if pos_x2 > 360:
                print("Player 2: Rolled over the end of the board. Go back to the start!")
                pos_x2 = 10
                pos_y2 = 30
                break
            # updating the screen and delaying it after the move of the player
            pygame.display.update()
            pygame.time.delay(300)

        # this displays the player going on the last block to win the game, without it you would not see
        # the player go on the last box
        win.blit(board, (0, 0))
        player1(win, pos_x1, pos_y1)
        player2(win, pos_x2, pos_y2)
        pygame.display.update()
        pygame.time.delay(300)

        # checks to see if player two is at the exact coordinates of the last box, if they are then the game ends
        # and this player won
        if pos_y2 == 330 and pos_x2 == 360:
            print("Player 2 wins")
            break


def player1(win, pos_x1, pos_y1):
    pygame.draw.circle(win, (255, 0, 0), (pos_x1, pos_y1), 8)


def player2(win, pos_x2, pos_y2):
    pygame.draw.circle(win, (0, 0, 255), (pos_x2, pos_y2), 8)


def roll():
    return random.randint(1, 6)


#function used to draw the text on to the screen
def display_text_on_board(board, font, text, position):
    # Clear the previous text on the screen
    pygame.draw.rect(board, (255, 255, 255), (*position, 300, 50))

    # Display the text on the board
    text_surface = font.render(text, True, (0, 0, 0))
    board.blit(text_surface, position)


# calling main function
main()
