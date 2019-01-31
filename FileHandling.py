# opening a file

# modes

# r --> read (default)
# w --> write
# r+ --> read and write
# a --> append
# rb --> read-binary
# wb --> write-binary
#
#f = open('file.txt')
#
##print(type(f))
#
##print(f.read())
#
#f.seek(3)
#
##print(f.read())
#
#print(f.tell())
#
#f.close()


#f = open('file2.txt', 'r+')
#
#print(f.readline())
#f.writelines('This is second line')
#
#f.close()


#f = open('file.txt')
#
##for line in f.readlines():
##    print(line)
#
#print(f.readline())
#print(f.tell())
#print(f.readline())
#    
#f.close()

with open('file.txt', 'rb') as f:
    var = f.read()
    
print(f.closed)






