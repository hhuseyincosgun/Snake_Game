## Snake Game
This code is a Python implementation of the classic Snake game using the Turtle graphics library. Here's an overview of the code:

![snake_gıf](https://user-images.githubusercontent.com/21257660/215592633-66e77876-1409-416f-98f6-a4ebac2a212a.gif)

1. **Imports:**
   - `turtle`: Used for creating graphics and handling user input.
   - `time`: Used for introducing delays in the game loop.
   - `random`: Used for generating random positions and properties.
   - `winsound`: Used for playing a sound when certain events occur.

2. **Setting up the screen:**
   - The code creates a Turtle graphics screen with a specified size and background color.
   - The Snake game window has a title, background image ("background.png"), and a size of 600x600 pixels.

3. **Snake Initialization:**
   - A turtle named `snake` is created to represent the snake in the game.
   - The snake starts as a red square at coordinates (0, 100).
   - The snake's properties such as color, speed, and shape are set.

4. **Score Display:**
   - The code initializes a turtle named `score_table` to display the current score and high score.
   - The initial score and high score are set to 0.

5. **Food Initialization:**
   - A turtle named `food` is created to represent the food in the game.
   - The food has random colors and shapes (square, triangle, or circle).
   - The initial position of the food is set to (0, 0).

6. **Snake Body:**
   - A list named `body` is used to keep track of the snake's body parts.
   - The `add_body` function creates a new turtle and appends it to the body list.

7. **Functions for Movement:**
   - Functions (`go_up`, `go_down`, `go_left`, `go_right`) change the direction of the snake.
   - The `move` function updates the snake's position based on its direction.

8. **Speed Control:**
   - The snake's speed can be increased or decreased using the `speed_up` and `speed_down` functions.
   - The spacebar (`'space'`) is used to activate the speed boost.

9. **Input Handling:**
   - Arrow keys and spacebar are used for controlling the snake and adjusting its speed.

10. **Game Loop:**
    - The main game loop (`while True`) continually updates the game state.
    - It checks for collisions with the screen boundaries and handles the game over scenario.
    - If the snake eats the food, it updates the score, creates a new food, and adjusts the snake's speed.

11. **Sound Effects:**
    - The `winsound` library is used to play a sound when the snake collides with the screen boundaries or eats the food.

12. **Body Movement:**
    - The code handles the movement of the snake's body when it grows longer.

13. **Time Delay:**
    - The `time.sleep(speed)` statement controls the speed of the game loop, introducing a delay based on the snake's speed.

Note: The code uses the Windows-specific `winsound` library for sound effects, so it might not work on non-Windows systems without modification. Additionally, the code has a perpetual game loop (`while True`) which typically should be part of a more controlled game loop, especially in graphical user interface (GUI) applications.
