# TurtleCommand
IMPORT NECESSARY HEADER FILES FOR DEVELOPMENT-
We are using Tkinter and turtle libraries which provide the gui support to make the project more user friendly.

DEFINE MAIN CLASS-
We define the main class of the program over here.

INSTANTIATE THE MAIN WINDOW TO START PROGRAM-
The main window is called over here for building the gui of the game.

CREATE A PLOT GRAPH TO SHOW THE OBSTACLES IN PATH FOR THE TURTLE-
The obstacle plot or map is made to show the player that he should not move the turtle over these obstacles.

SET THE POSTIONS FOR THE PREDEFINED OBSTACLES HERE-
Certain sample positions of the obstacles of the turtle are predefined in the game.

        
CREATE THE FIGURE OF THE GRAPH PLOT-
The graph window of the obstacle is instantiated.


START MAIN COMMAND TO RUN THE TURTLE ON THE FIELD-
This is the main function in which the turtle is given command and runs in the main field.

        

OPTIMIZE THE TURTLE WINDOW-
Turtle playground is depicted in this small window to create a nice user experience.
        

SET INITIAL COORDINATES FOR THE TURTLE-
Initial coordinates for the turtle are set at the start of every game.
        

GETTING AND PARSING THE USER INPUT COMMAND-
User input is read and parsed over here.
        

EXECUTING EACH COMMAND AS PER THE RULES OF THE GAME-
Each command of the user input is read and processed into the following action to be undertaken as per that particular command.
        

CHECKING THE PREVAILING OBSTACLE CONDITIONS AND BACKTRACKING IF THERE IS OBSTACLE IN THE PATH-
By checking if there is an obstacle in the turtles way , the turtle cannot move and that it has to backtrack that particular command.
        

EXECUTING WARNING FOR INVALID COMMAND INPUT-
Error handlers and necessary warning are given to the player so that he can refine his particular input command.
       
        
PRINTING THE OUTPUT AS BOTH COMMAND LINE AS WELL AS IN THE GUI OUTPUT BOX-
Appropriate output is given to the player as per his input commands and the output consists of the final position and the direction in which the turtle is headed. 
