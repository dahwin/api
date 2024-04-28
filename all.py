import torch.multiprocessing as mp
import time
import subprocess
import torch
print('starting.....')
def run_script(script):
    """Function to run a script."""
    subprocess.run(["python", script])

if __name__ == "__main__":
    start_time = time.time()
    
    # List of scripts to run
    scripts = ["client.py",'client1.py']
    
    # Number of processes to use
    num_processes = len(scripts)
    
    # Create a list to hold process objects
    processes = []
    
    # Start processes
    for script in scripts:
        p = mp.Process(target=run_script, args=(script,))
        p.start()
        processes.append(p)
    
    # Join processes
    for p in processes:
        p.join()
    
    # Record end time
    end_time = time.time()
    
    # Calculate and print total processing time
    total_time = end_time - start_time
    print(f"Total processing time: {total_time} seconds")
