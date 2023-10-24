class deque :
    def __init__(self) :
        self.qeue = []
        
    def addfront(self,item) :
        self.qeue.insert(0,item)
        
    def addrear(self,item) :
        self.qeue.append(item)
        
    def removefront(self) :
        self.qeue.pop()
        
    def removerear(self) :
        self.qeue.pop(0)
     
    def isempty(self) :
        if self.qeue == [] :
            return True
        else :
            return False
    
    def size(self) :
        return len(self.qeue)


def main() : 
    data = deque()
    print("IMPLEMENTASI QEUE")
    print(
    """
    1.insert data
    2.remove data
    3.size data
    4.output 
    0.end
    """
    )
    while True :
        inputuser = str(input("silahkan dipilih : "))
        if inputuser == "1" :
            item = input("Masukan data : ")
            data.addrear(item)
            print("SUCCESS\n")
        
        elif inputuser == "2" :
            data.removefront()
            print("SUCCESS\n")
            
        elif inputuser == "3" :
            print(
                "banyaknya data =",data.size()
                ) 
            print("SUCCESS\n")
            
        elif inputuser == "4" :    
            print(*data.qeue)
            print("SUCCESS\n")
            
        elif inputuser == "0" :
            break
        
main()