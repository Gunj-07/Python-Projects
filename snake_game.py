from tkinter import *
import random

# Game settings
GAME_WIDTH = 700
GAME_HEIGHT = 600
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

game_loop_id = None  # For canceling .after loop


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for _ in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        self.square = canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):
    global direction, score, game_loop_id

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        game_loop_id = window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    opposites = {"left": "right", "right": "left", "up": "down", "down": "up"}
    if direction != opposites.get(new_direction):
        direction = new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    global game_loop_id
    if game_loop_id:
        window.after_cancel(game_loop_id)

    canvas.delete(ALL)
    canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2 - 50,
                       font=('consolas', 40), text="GAME OVER", fill="red", tag="gameover")

    # Show buttons using place
    restart_button.place(x=250, y=350)
    exit_button.place(x=370, y=350)


def restart_game():
    global score, direction, snake, food, game_loop_id

    score = 0
    direction = 'down'
    label.config(text="Score:{}".format(score))
    canvas.delete(ALL)

    restart_button.place_forget()
    exit_button.place_forget()

    snake = Snake()
    food = Food()
    game_loop_id = window.after(SPEED, next_turn, snake, food)


# Setup window
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 30))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()
window.geometry(f"{window.winfo_width()}x{window.winfo_height()}+"
                f"{(window.winfo_screenwidth() // 2) - (window.winfo_width() // 2)}+"
                f"{(window.winfo_screenheight() // 2) - (window.winfo_height() // 2)}")

# Key bindings
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Buttons (initialized but not visible yet)
restart_button = Button(window, text="Restart", font=('consolas', 16), command=restart_game)
exit_button = Button(window, text="Exit", font=('consolas', 16), command=window.destroy)

# Start game
snake = Snake()
food = Food()
game_loop_id = window.after(SPEED, next_turn, snake, food)

window.mainloop()
