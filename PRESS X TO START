import pygame
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.output(3,GPIO.LOW)

TRIG_Center = 36
ECHO_Center = 40
TRIG_Left = 35
ECHO_Left = 38
TRIG_Right = 33
ECHO_Right = 37
GPIO.setup(TRIG_Center,GPIO.OUT)
GPIO.setup(ECHO_Center,GPIO.IN)
GPIO.setup(TRIG_Left,GPIO.OUT)
GPIO.setup(ECHO_Left,GPIO.IN)
GPIO.setup(TRIG_Right,GPIO.OUT)
GPIO.setup(ECHO_Right,GPIO.IN)

p = GPIO.PWM(18,50)
b= GPIO.PWM(13,50)
p.start(3.5) #correct
b.start(5) #correct

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

# This is a simple class that will help us print to the screen
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def print(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
        
    def unindent(self):
        self.x -= 10
    

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
        
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
            
 
    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    textPrint.print(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.indent()
    #Center UltraSonic
    GPIO.output(TRIG_Center,False)
    time.sleep(0.5)
    GPIO.output(TRIG_Center,True)
    time.sleep(0.00001)
    GPIO.output(TRIG_Center,False)
    while GPIO.input(ECHO_Center) ==0:
        pulse_start_center = time.time()
    while GPIO.input(ECHO_Center) == 1:
        pulse_end_center = time.time()

    pulse_duration_center = pulse_end_center - pulse_start_center
    distance_center = pulse_duration_center * 17150
    distance_center = round(distance_center,2)
    print ('distance of center',distance_center)
    if distance_center < 30:
        GPIO.output(3,False)
    #Left UltraSoinc
    GPIO.output(TRIG_Left,False)
    time.sleep(0.5)
    GPIO.output(TRIG_Left,True)
    time.sleep(0.00001)
    GPIO.output(TRIG_Left,False)
    while GPIO.input(ECHO_Left) ==0:
        pulse_start_Left = time.time()
    while GPIO.input(ECHO_Left) == 1:
        pulse_end_Left = time.time()
            
    pulse_duration_Left = pulse_end_Left - pulse_start_Left
    distance_Left = pulse_duration_Left * 17150
    distance_Left = round(distance_Left,2)
    print ('distance of left',distance_Left)
    if distance_Left < 30:
        p.ChangeDutyCycle(7) 
        b.ChangeDutyCycle(5.5)
    #Right UltraSonic
    GPIO.output(TRIG_Right,False)
    time.sleep(0.5)
    GPIO.output(TRIG_Right,True)
    time.sleep(0.00001)
    GPIO.output(TRIG_Right,False)
    while GPIO.input(ECHO_Right) ==0:
        pulse_start_right = time.time()
    while GPIO.input(ECHO_Right) == 1:
        pulse_end_right = time.time()

    pulse_duration_right = pulse_end_right - pulse_start_right
    distance_right = pulse_duration_right * 17150
    distance_right = round(distance_right,2)
    print ('distance of right',distance_right)
    if distance_right < 30:
        p.ChangeDutyCycle(2.5) #left for left tire 60*
        b.ChangeDutyCycle(1.5)   
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        textPrint.print(screen, "Joystick {}".format(i) )
        textPrint.indent()
    
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        textPrint.print(screen, "Joystick name: {}".format(name) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.print(screen, "Number of axes: {}".format(axes) )
        textPrint.indent()
        
        for i in range( axes ): #mapping the axes
            axis = joystick.get_axis( i )
            if joystick.get_axis( 0 ) < 0 and joystick.get_axis( 1 ) < 0:
                print("Left Top.")
                p.ChangeDutyCycle(2.5) #left for left tire 60*
                b.ChangeDutyCycle(1.5)
                break
            if joystick.get_axis( 0 ) > 0 and joystick.get_axis( 1 ) < 0:
                print("Right Top.")
                p.ChangeDutyCycle(7) 
                b.ChangeDutyCycle(5.5)
                break
            if joystick.get_axis( 1 ) == -1:
                print("Top.")
                p.ChangeDutyCycle(3.5) #left for left tire 60*
                b.ChangeDutyCycle(5)
                break
        buttons = joystick.get_numbuttons()
        textPrint.print(screen, "Number of buttons: {}".format(buttons) )
        textPrint.indent()

        for i in range( buttons ): #mapping the buttons
            button = joystick.get_button( i )
            
            if joystick.get_button( 0 ) == 1:             
                print("Joystick button pressed Square is pressed.")
                break
            if joystick.get_button( 1 ) == 1:
                print("Joystick button pressed X is pressed.")
                GPIO.output(3,GPIO.HIGH)   
                break
            if joystick.get_button( 2 ) == 1:
                print("Joystick button pressed O is pressed.")
                GPIO.output(3,GPIO.LOW)
                break
            if joystick.get_button( 3 ) == 1:
                print("Joystick button pressed Triangle is pressed.")
                break
            if joystick.get_button( 10 ) == 1:
                print("Joystick button pressed click is pressed.")
                p.ChangeDutyCycle(3.5) #left for left tire 60*
                b.ChangeDutyCycle(5)
                break

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
