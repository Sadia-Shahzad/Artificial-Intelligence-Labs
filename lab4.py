# Question:1 
# Implement Stack using Python. 

class Stack:
   
    def __init__(self):
        self.noe=0
        self.list=[]

    def total_elements(self):
        return self.noe
    
    def is_empty(self):
        return self.noe==0
    
    def peek(self):
        if (self.noe-1 >=0):
            return self.list[self.noe-1]
        else:
            raise ValueError
    
    def push(self,ele):
        self.list+=[ele]    #python lists cannot add values on the indexes which do not exist instead we merge them with new lists
        self.noe+=1

    def pop(self):
        if (self.noe-1 < 0):
            raise ValueError
        else:
            deleted=self.list[self.noe-1]
            self.noe-=1
            return deleted
    

s1=Stack()


s1.push(10)
s1.push(20)
s1.push(30)


try:
    popped=s1.pop()
   
except ValueError :
    print("stack is already empty") 
else:
    print("Popped value is",popped)



try:
    print("Top item",s1.peek())
except ValueError:
    print("Empty stack cannot be peeked")




try:
    popped=s1.pop()
   
except ValueError :
    print("stack is already empty") 
else:
    print("Popped value is",popped)




try:
    popped=s1.pop()
   
except ValueError :
    print("stack is already empty") 
else:
    print("Popped value is",popped)




try:
    popped=s1.pop()
   
except ValueError :
    print("stack is already empty") 
else:
    print("Popped value is",popped)




try:
    print("Top item",s1.peek())
except ValueError:
    print("Empty stack cannot be peeked")



print("Is stack empty?",s1.is_empty())
print("Current size is ",s1.total_elements())
