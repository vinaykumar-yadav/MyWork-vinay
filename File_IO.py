
# write dictionary to file and print file data after reading
colorDic = {1: 'Red', 2: 'Blue', 3: 'Green'} 
filename= 'abc.txt'

try: 
    fileHandler = open(filename, 'wt') 
    fileHandler.write(str(colorDic)) 
    fileHandler.close() 
  
except: 
    print("Unable to write to file")

content = open(filename)
print(content.read())
