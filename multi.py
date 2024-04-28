import multiprocessing

# Define a multiprocessing lock
lock = multiprocessing.Lock()

def drun(f_shared):
    for i in range(9):
        print(i)
        with lock:
            f_shared.value = f"dahyun {i}"

def p(f_shared):
    for i in range(9):
        with lock:
            print(f_shared.value.decode())  # Decode bytes to string and print

if __name__ == "__main__":
    # Create a shared array for holding characters
    f_shared = multiprocessing.Array('c', b" " * 50)  # Create an array with fixed size

    # Create processes
    process1 = multiprocessing.Process(target=drun, args=(f_shared,))
    process2 = multiprocessing.Process(target=p, args=(f_shared,))

    # Start processes
    process1.start()
    process2.start()

    # Join processes to wait for them to finish
    process1.join()
    process2.join()
