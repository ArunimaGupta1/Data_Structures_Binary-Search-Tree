class Tree:
    def __init__(self,initval = None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
            
    def insert(self,v):
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        if self.value==v:
            return()
        elif v<self.value:
            self.left.insert(v)
            return
        else:
            self.right.insert(v)
            return
            
    
    def __str__(self):
        return(str(self.inorder()))
    
    def isempty(self):
            return(self.value==None)

   
    def inorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.inorder()+[self.value]+self.right.inorder())
    
        
 
    def maxval(self):
        if self.right.value==None:
            return(self.value)
        else:
            return(self.right.maxval())
        

t = Tree()      
for i in [1,65,8,6,7,3,4,55,66,78]:
    t.insert(i)

print(t)
print(t.maxval())
