# Exception Handling

# try - except - else - finally

#f = open('file1.txt', 'r')
#
#print(f.read())

try:
    f = open('file1.txt', 'r')
    
except FileNotFoundError:
    print('File does not exist')

except Exception:
    print('Something went wrong')

else:
    print(f.read())
    f.close()

finally:
    print('Executes not matter what')

