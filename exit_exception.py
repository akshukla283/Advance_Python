import os
try:
    print("try block")
    os._exit(0)
except:
    print("Exception")
finally: 
    print("finally block")
