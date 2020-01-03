class BinaryTree():

    def __init__(self,value):
        self.value = value
        self.right = None  
        self.left = None
    
    def AddNode(self,value):
        node = BinaryTree(value)
        self.InsertNode(node,self)
    
    def InsertNode(self,node,root):
        if node.value < root.value:
            if root.left:
                self.InsertNode(node,root.left)
            else:
                root.left = node
        else:
            if root.right:
                self.InsertNode(node,root.right)
            else:
                root.right = node
    
    def Display(self,state):
        if state == 1:
            print('The Pre-Order display of the Tree is as follows : ')
            self.Preorder(self)
        elif state == 2:
            print('The In-Order display of the Tree is as follows : ')
            self.Inorder(self)
        else:
            print('The Post-Order display of the Tree is as follows : ')
            self.Postorder(self)
    
    def Preorder(self,root):
        if root == None:
            return
        print(root.value)
        self.Preorder(root.left)
        self.Preorder(root.right)
    
    def Inorder(self,root):
        if root == None:
            return 
        self.Inorder(root.left)
        print(root.value)
        self.Inorder(root.right)
    
    def Postorder(self,root):
        if root == None:
            return
        self.Postorder(root.left)
        self.Postorder(root.right)
        print(root.value)
    
if __name__ == '__main__':
    root = None
    while True:
        print('Binary Tree : ')
        print('1 --> Add Node')
        print('2 --> Display Tree in Pre-Order')
        print('3 --> Display Tree in In-Order')
        print('4 --> Display Tree in Post-Order')
        print('5 --> Exit the Menu')
        choice = int(input('Enter the choice : '))

        if choice == 1:
            if root:
                root.AddNode(int(input('Enter the Value for the Node : ')))
            else:
                root = BinaryTree(int(input('Enter the value for the Node : ')))
        
        elif choice == 2:
            if root:
                root.Display(1)
            else:
                print('Tree is Empty')
        
        elif choice == 3:
            if root:
                root.Display(2)
            else:
                print('Tree is Empty')
        
        elif choice == 4:
            if root:
                root.Display(3)
            else:
                print('Tree is Empty')
        
        elif choice == 5:
            print('Thank You')
            exit()
        
        else:
            print('Invalid Choice')
