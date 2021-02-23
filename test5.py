import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test5.py"))) 

print(os.path.join(os.getcwd(), os.pardir))
print(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))