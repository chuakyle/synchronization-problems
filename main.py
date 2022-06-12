import threading

# Initialize; both threads are not yet ready
flag = [False, False]
turn = 0
# Serves as the number of threads went in critical section, as well as thread ID
total_counter = 0 

def green(green_threads):
    global flag, turn, total_counter

    #
    while(True):
        flag[0] = True
        turn = 1
        
        while(flag[1] and turn == 1):
            continue

        # critical section
        print("producer critical")
        total_counter += 1
        green_threads -= 1

        print("Thread ID: ", total_counter)
        print("Color: Green")
        flag[0] = False

        # remainder section
        print("\nEmpty Fitting Room\n")

        if(green_threads <= 0):
            break 

def blue(blue_threads):
    global flag, turn, total_counter

    while(True):
        flag[1] = True
        turn = 0

        while(flag[0] and turn == 0):
            continue

        # critical section
        total_counter += 1
        blue_threads -= 1

        print("consumer critical")
        print("Thread ID: ", total_counter)
        print("Color: Blue")

        flag[1] = False  

        # remainder section
        print("\nEmpty Fitting Room\n")

        if(blue_threads <= 0):
            break  

def test(blue_threads):
    print("Before: ", blue_threads)
    blue_threads -= 1
    print("After: ", blue_threads)
    
# Asks and accepts 3 inputs from the user

room_size = input("Enter number of slots inside the fitting room: ")
blue_threads = input("Enter number of blue threads: ")
green_threads = input("Enter number of green threads: ")

room_size = int(room_size)
blue_threads = int(blue_threads)
green_threads = int(green_threads)

green = threading.Thread(target = green, args=[green_threads])
blue = threading.Thread(target = blue, args=[blue_threads])
green.start()
blue.start()

#   test = threading.Thread(target = test)
#   test.start()

