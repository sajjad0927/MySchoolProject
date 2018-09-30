
class School:
    'Class To store and get the school information'
    __Name='';__Id=0;__Address='';__State='';__City='';__Pin=0

    def __init__(self,name,id,address,state,city,pin):
        self.__Name=name
        self.__Address=address
        self.__Id=id
        self.__City=city
        self.__State=state
        self.__Pin=pin
        
    def setSchoolAttributs(self,name,id,address,state,city,pin):
        __Name=name
        __Address=address
        __Id=id
        __City=city
        __State=state
        __Pin=pin
    
    def getSchoolDetails(self):
        print("Printing")
        print ("Name=",self.__Name)
        print ("Address=",self.__Address)
        print ("ID=",self.__Id)
        print ("State=",self.__State)
        print ("City=",self.__City)
        print ("Pin=",self.__Pin)
    
        
#def main():
    #School.setSchoolAttributs("School1",1,"Address1","State1","City1",55)
    #School.getSchoolDetails()


#if __name__=='__main__':
    #main()




