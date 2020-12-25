## Test driving the LookingGLass context managers class

from mirror import LookingGlass
with LookingGlass() as what:
    print('AKshat','ROnaldo','Batman')
    print(what)

    
## Exercising LookingGlass without a with block

from mirror import LookingGlass
manager=LookingGlass()
manager

monster=manager.__enter__()
monster=='JABBEREOCKY'
