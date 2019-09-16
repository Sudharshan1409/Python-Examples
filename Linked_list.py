class node:

    def __init__(self,data):
        self.data = data
        self.link = None
    
    def insert_first(self,data):
        newnode = node(data)
        newnode.link = self
        return newnode

    def insert_last(self,data):
        newnode = node(data)
        self.link = newnode
        return newnode
    
    def delete_first(self):
        temp = self
        temp1 = self.link
        del(temp)
        return temp1

    def delete_last(self,last):
        temp = self
        while temp.link != last:
            temp = temp.link
        temp.link = None
        del(last)
        last = temp
    
    def display(self):
        temp = self
        while temp:
            print(temp.data,end = ' ')
            if temp.link:
                print('-->',end = ' ')
            temp = temp.link
        print()

if __name__ == "__main__":
    run = True
    front,last = None,None
    while run:

        print('1 --> Insert First')
        print('2 --> Insert Last')
        print('3 --> Delete First')
        print('4 --> Delete Last')
        print('5 --> Display')
        print('6 --> Exit')
        choice = int(input('Enter the choice : '))

        if choice == 1:
            if front:
                front = front.insert_first(input('Enter the Element : '))
            else:
                front = node(input('Enter the Element : '))
                last = front
        
        elif choice == 2:
            if front:
                last = last.insert_last(input('Enter the Element : '))
            else:
                front = node(input('Enter the Element : '))
                last = front

        elif choice == 3:
            if front:
                front = front.delete_first()
        
        elif choice == 4:
            if front:
                front.delete_last(last)

        elif choice == 5:
            if front:
                front.display()

        elif choice == 6:
            run = False
        
        else:
            print('Enter the valid choice ')

        

