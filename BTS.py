class Node: #تعریف کلاس درخت
    
    def __init__(self,key): #تعریف سازنده که داده و زیر درخت های چپ و راست را در بر میگیرد
        
        self.data=key
        
        self.left=None
        
        self.right=None

def insert(root,node): #تابع درج در درخت
    
    if root is None:
        
        root=node
        
    else :
        
        if root.data<node.data:
            
            if root.right is None:
                
                root.right=node
                
            else:
                
                insert(root.right,node)
                
        else:
            
            if root.left is None:
                
                root.left=node
                
            else:
                
                insert(root.left,node)

def inorder(root): #تابع پیمایش میان ترتیب
    
    if root:
        
        inorder(root.left)

        print(root.data)

        inorder(root.right)

x=int(input("Root=")) #دریافت ریشه

lst1=[]

lst1.append(x) #قرار دادن در لیست

r=Node(x)

for n in range(0,10): #دریافت برگ ها
    
    lst2=[]
    
    n=int(input("Node="))
    
    insert(r,Node(n))  #فراخوانی تابع درج
    
    for i in range(0,10):
        
        lst2.append(n)
        
    lst1.extend(lst2)
    
inorder(r) #فراخوانی تابع میان ترتیب

search=int(input("Search:")) #جستجو در لیست ها 

if search in lst1:
    
    print("Found")
    
elif search in lst2:
    
    print("Found")
    
else :
    
    print("Not Found")

