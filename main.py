import threading

# Initialize; both threads are not yet ready
flag = [False, False]
turn = 0

def producer():
    global flag, turn

    #
    while(True):
        flag[0] = True
        turn = 1
        
        while(flag[1] and turn == 1):
            pass

        # critical section
        print("producer critical")
        flag[0] = False

        # remainder section
        #break

def consumer():
    global flag, turn

    while(True):
        flag[1] = True
        turn = 0

        while(flag[0] and turn == 0):
            pass

        # critical section
        print("consumer critical")
        flag[1] = False  

        # remainder section
        #break  
    
# Asks and accepts 3 inputs from the user

# room_size = input("Enter number of slots inside the fitting room: ")
# blue_threads = input("Enter number of blue threads: ")
# green_threads = input("Enter number of green threads: ")

green = threading.Thread(target = producer)
blue = threading.Thread(target = consumer)
green.start()
blue.start()

