import time



print(f"""Hello world!

    I'm about to make a task loop!
    
    In 5 seconds I'm about too spam every 5 seconds!
    
    This loop will make it so in 5 seconds it will say 'Task loop' and then in another 5 seconds it will keep repeating""")

time.sleep(5)

while True:
    print("\nTask loop")

    time.sleep(5)