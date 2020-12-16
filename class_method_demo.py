class Test:
    count=0
    
    def __init__(self):
        Test.count=Test.count+1

    @classmethod
    def getNoOfObjects(cls):
        print('Number of objects:',Test.count)

Test.getNoOfObjects()
t1=Test()
t2=Test()
Test.getNoOfObjects()
