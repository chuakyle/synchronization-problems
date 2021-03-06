import threading
from time import sleep

# Initialize; both threads are not yet ready
flag = [False, False]
turn = 0
# Serves as the number of threads went in critical section, as well as thread ID
total_counter = 0 


def green(green_threads, room_size):
    global flag, turn, total_counter
    
    while(True):
        sleep(2)

        flag[0] = True
        turn = 1
        room_counter = 0
        
        while(flag[1] and turn == 1):
            continue

        print("<><> Green Only <><>\n")

        while(room_counter < room_size):
            if(green_threads > 0):
                green_threads -= 1
                total_counter += 1
                room_counter += 1

                print("Thread ID: ", total_counter)
                print("Color: Green\n")
            else: break
            if(room_counter == room_size or green_threads == 0):
                print("*** Empty Fitting Room ***\n")

        flag[0] = False

        if(green_threads <= 0):
            break 

def blue(blue_threads, room_size):
    global flag, turn, total_counter
    
    while(True):
        sleep(2)

        flag[1] = True
        turn = 0
        room_counter = 0

        while(flag[0] and turn == 0):
            continue

        print("<><> Blue Only <><>\n")

        while(room_counter < room_size):
            if(blue_threads > 0):
                total_counter += 1
                blue_threads -= 1
                room_counter += 1
        
                print("Thread ID: ", total_counter)
                print("Color: Blue\n")
            else: break
            if(room_counter == room_size or blue_threads == 0):
                print("*** Empty Fitting Room ***\n")

        flag[1] = False  

        if(blue_threads <= 0):
            break  
    
# Asks and accepts 3 inputs from the user

room_size = input("Enter number of slots inside the fitting room: ")
blue_threads = input("Enter number of blue threads: ")
green_threads = input("Enter number of green threads: ")

room_size = int(room_size)
blue_threads = int(blue_threads)
green_threads = int(green_threads)

green = threading.Thread(target = green, args=[green_threads, room_size]).start()
blue = threading.Thread(target = blue, args=[blue_threads, room_size]).start()