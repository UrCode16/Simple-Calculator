#You must have installed keyboard module (pip install keyboard)
import time
import keyboard

#Made by Ur Manager (@UrCode16 on GitHub)
#Thanks for using this code!

ver = 3.1 #Version

print(f"Welcome to my calculator! Version: {ver}")
print("GitHub: @UrCode16")
print("\nUse only These operations: +, -, *, /")
print("Syntax must be NUM. OPERATION NUM. (Example: 1+1)")
A = input("\nEnter: ")

print("The answer is:", eval(A))

time.sleep(1)

print("\nIf u want calculate something else press Enter", end="")

run = True
while run:
    if keyboard.is_pressed("Enter"):
        input("")
        A = input("Enter: ")
            
        print("The answer is:", eval(A))
            
        time.sleep(1)
            
        print("\nIf u want calculate something else press Enter")
        time.sleep(0.5)
        print("If not press Esc")
    if keyboard.is_pressed("Esc"):
        run = False
print("Bye!")
time.sleep(1)
