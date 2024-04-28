ss = False
while ss!=True:
    try:
        # Open the file in read mode
        with open('dahyun0.txt', 'r') as file:
            # Read the contents of the file
            content0 = file.read()

        # Open the file in read mode
        with open('dahyun1.txt', 'r') as file:
            # Read the contents of the file
            content1 = file.read()
    except:
        pass

    try:
        if "true" == content0 and 'true' == content1:
            print(True)
            ss=True
    except:
        pass



# Both yes0 and yes1 are True
print("Both yes0 and yes1 are True. Now you can sleep!")

