## Test driving the looking_glass context manager functions

from mirror_gen import LookingGlass
with LookingGlass() as what:
    print('ALice','Micky','Donald')
    print(what)
    
    
## Generator based context manager implementing exception handling 

import contextlib
import sys
def looking_glass():
    original_write-sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])
        
    sys.stdout.write=reverse_write
    msg=''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg='Please DO NOT divide by zero!!'

    finally:
        sys.stdout.write=original_write
        if msg:
            print(msg)
