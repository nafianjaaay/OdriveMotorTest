# OdriveMotorTest
Python program for testing motor on ODRIVE Driver with closed loop parameter settings

# Features
1.  Closed loop settings (KP, KI, Ramp Rate, etc.)
2.  Change direction of motor using keybind
3.  Auto reset motor error when running
4.  Incremental velocity with delay

# Requirements
1.  Python 3.x
2.  keyboard library (pip install keyboard)
3.  odrivetool library (pip install odrive)
4.  time library (pip install time)

# How to use
1.  Clone this repository or download the OdriveTEST.py file to your computer.
2.  Open a terminal or command prompt and navigate to the directory where the OdriveTEST.py file is located.
3.  Install all of the library by running:
    pip install keyboard
    pip install odrive
    pip install time
4.  Be super user by running command: sudo su
5.  Run the program by running the command python OdriveTEST.py.
6.  The program window will appear, wait the motor calibrate itself.
7.  run the your prefered speed by clicking the keybind (p, o, l, k)
8.  if you want to turn off the motor, simply click h in your keyboard
9.  To exit the program, simply click the "Exit" button or close the window.

# Author
This program was created by Nafianjaaay. If you have any questions or suggestions, please feel free to contact me at nafianfalahakbar@gmail.com.
