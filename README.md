# Pygame Class Study

This repository offers a beginner-friendly, step-by-step introduction to object-oriented programming in Python using Pygame. Each script builds upon the previous one, gradually introducing key OOP concepts such as encapsulation, class design, and object interaction through simple game mechanics.

## Prerequisites

- Python 3.7 or higher
- Pygame

To install Pygame, run:


```bash
pip install pygame
```


## File Overview

### 1. `101_blue_ball.py` — *Drawing a Static Object*

This script initializes a Pygame window and displays a static blue ball at the center. It introduces the basics of setting up a Pygame application, including window creation, event handling, and drawing shapes.

**Key Concepts:**
- Pygame initialization
- Creating a display window
- Drawing shapes on the screen
- Basic event loop

### 2. `102_blueball_move_key.py` — *Interactive Movement*

Building upon the previous script, this version allows the user to move the blue ball using keyboard inputs. It introduces user interaction and dynamic object positioning.

**Key Concepts:**
- Handling keyboard events
- Updating object positions based on input
- Refreshing the display to reflect changes

### 3. `103_redball_enemy.py` — *Introducing an Enemy Object*

This script adds a red ball that acts as an enemy, moving autonomously across the screen. It demonstrates how to manage multiple objects and introduces simple enemy behavior.

**Key Concepts:**
- Managing multiple objects
- Implementing autonomous movement
- Understanding object interactions

### 4. `104_redball_4_enemy.py` — *Multiple Enemies*

Expanding on the previous example, this script introduces four red enemy balls, each with its own movement pattern. It showcases how to handle multiple instances of similar objects and manage their behaviors.

**Key Concepts:**
- Creating multiple object instances
- Managing object lists
- Implementing varied behaviors for similar objects

### 5. `105_enemy_class.py` — *Object-Oriented Design*

The final script refactors the enemy logic into a dedicated `Enemy` class, encapsulating properties and behaviors. This approach simplifies code management and sets the foundation for scalable game development.

**Key Concepts:**
- Defining and using classes
- Encapsulation of object properties and methods
- Creating and managing multiple class instances

## How to Run

To execute any of the scripts, navigate to the repository directory in your terminal and run:


```bash
python <script_name>.py
```


Replace `<script_name>` with the desired file name, such as `101_blue_ball`.

## Learning Objectives

By progressing through these scripts, you will:

- Understand the basics of Pygame and game loop structures.
- Learn how to handle user input for interactive applications.
- Gain experience in managing multiple objects and their interactions.
- Develop skills in structuring code using classes and OOP principles.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Feel free to customize this `README.md` further to suit your specific needs or to add more detailed explanations and visuals. 
