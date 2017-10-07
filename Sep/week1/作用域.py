#!/usr/bin/env python
#!/usr/bin/python

def add():

    count=10
    def inner():
        nonlocal count
        count+=1
        print('2 is %s'%count)
    inner()
    print('1 is %s'%count)
add()

