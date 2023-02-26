import curses
import time


def main(screen):
    curses.curs_set(0)
    screen.nodelay(1)
    screen.keypad(1)
    height, width = screen.getmaxyx()

    player_x = width // 2
    player_y = height // 2
    player_char = 'O'

    gravity = 0.25
    jump_speed = 1
    jump = False
    max_jump_height = 20

    while True:
        screen.clear()
        screen.addstr(player_y, player_x, player_char)
        screen.refresh()

        key = screen.getch()
        if key == curses.KEY_UP and not jump and player_y > max_jump_height:
            jump = True

        if jump:
            jump_speed -= gravity
            player_y -= int(jump_speed)
            if player_y <= max_jump_height:
                jump = False
                jump_speed = 1

        time.sleep(0.01)


if __name__ == "__main__":
    curses.wrapper(main)
