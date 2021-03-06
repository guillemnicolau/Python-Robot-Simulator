'''
/***********************************************
*    Title: Moving Robot Application           *
*    Author: Guillem Nicolau Alomar Sitjes     * 
*    Date: July 15th, 2017                     *
*    Code version: 0.1                         *
*    Availability: Public                      *
***********************************************/
'''
from ToyRobot.ToyRobot import Robot


# Method to check if the user wants to finish the application
def check_input(input_var):
    if input_var == 'exit':
        print "The application will now end."
        clean_screen()
        raise SystemExit
    return 0


# Method called to do a 'clear', just for application visualization purposes
def clean_screen():
    print(chr(27) + "[2J")


# Print method for the first message
def message_output1():
    print "This is an application to place a robot on a default table of 5x5.\n" \
          "After placing it, you will be able to move it all over the table.\n" \
          "First place value is on the West/East axis, second is on the North/South axis.\n" \
          "To quit the application, insert \"exit\""


# Print method for the second message
def message_output2():
    print "Now that the robot has been initialized, you can either:\n" \
          "    a) 'PLACE x, y, orientation(NORTH,SOUTH,EAST or WEST' to define a new position\n" \
          "    b) 'MOVE' the robot forward to a new position\n" \
          "    c) Turn the robot 'LEFT' or 'RIGHT'\n" \
          "    d) 'REPORT' current robot state"

# Main method
if __name__ == "__main__":
    clean_screen()
    message_output1()
    my_robot = Robot()

    while not my_robot.ready():
        var = raw_input("Insert 'PLACE x, y, orientation(NORTH,SOUTH,EAST or WEST)' to define a new position:")
        check_input(var)
        robot_input = my_robot.parse_first_input(var)
    message_output2()
    while True:
        var = raw_input("Please, enter a new command: ")
        check_input(var)
        robot_input = my_robot.parse_second_input(var)
