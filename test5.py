import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("test5.py"))) 