# Variable Scope

# LEGB --> Local, Enclosing, Global, Builtins

#x = 'global x'

#def func():
##    x = 'local x'
#    print(x)
#
#func()
#print(x)


#x = 'global x'
#
#def func():
#    global x
#    x = 'local x'
#    print(x)
#    
#func()
#print(x)


#def min():
#    print('min function overriden')
#
#print(min())


x = 'global x'

def outer():
    x = 'outer x'
    
    def inner():
#        nonlocal x
        x = 'inner x'
        print(x)
    
    inner()
    print(x)


outer()
print(x)


