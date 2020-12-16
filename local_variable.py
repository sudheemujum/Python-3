class Test():

    @staticmethod
    def average(list1):
        result=sum(list1)/len(list1)
        print('The average:',result)

    @staticmethod
    def wish(name):
        for i in range(10):
            print('Good evening:',i,name)

list1=[10,20,30,40]
Test.average(list1)
Test.wish('Sudhee')

        
