#import
import math

#user inputs
initial_height= float(input("Enter initial height: "))
initial_velocity = float(input("Enter initial velocity: "))
angle = float(input("Enter angle: "))
time = float(input("The time you would like to know the projectile (must be an integer): "))

#find max height
angle_radians = math.radians(angle) #degrees --> radians
max_height = initial_height + ( ( (initial_velocity ** 2) * (math.sin(angle_radians) ** 2) ) / (2 * 9.8) )

#loops
t = 1
current_height = 0

if time <= 0:
    print("0")
else:
    while t <= time:
        #equation - height = initial_height + (v(sin(x))) * t -1/2g^2 --> quadratic
        current_height = initial_height + initial_velocity * math.sin(angle_radians) * t - (0.5 * 9.8 * t ** 2)
        t +=1

#Solution
print(f"The height of the projectile after {time} seconds  is {current_height} meters.")