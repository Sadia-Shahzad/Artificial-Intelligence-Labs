# Question:1 
# Implement Stack using Python. 

class Stack:
   
    def __init__(self,size):
        self.size=size
        self.noe=0
        self.list=[]

    def total_elements(self):
        return self.noe
    
    def is_empty(self):
        return self.noe==0
    
    def peek(self):
        return self.list[self.noe-1]
    
    def push(self,ele):
        self.list+=[ele]    #python lists cannot add values on the indexes which do not exist instead we merge them with new lists
        self.noe+=1

    def pop(self):
        deleted=self.list[self.noe-1]
        self.noe-=1
        return deleted
    

s1=Stack(10)


s1.push(10)
s1.push(20)
s1.push(30)
try:
    print("Popped",s1.pop())
except empty_stack as es: 

print("Top item",s1.peek())
print("Is stack empty?",s1.is_empty())
print("Current size is ",s1.total_elements())
