class sort():
    
    def __init__(self):                                 	            #To initialize array
        self.n=int(input("Enter the length of your array:"))
        self.a=[0]*self.n

        for i in range(self.n):                                             #Taking elements of array
            self.a[i]=int(input("Enter "+str(i)+" element:"))

        print("The array is:",end=" ")
        for i in range(self.n):                                             #Transversing the array
            print(self.a[i],end=" ")
        print()

    def trans(self):
        print("The array is:",end=" ")
        for i in range(self.n):
            print(self.a[i],end=" ")
        print()

                
    def bubble_sort(self):
        
        length=self.n
        for j in range(length-1):
            for z in range(length-j-1):
                if(self.a[z]>self.a[z+1]):
                    self.a[z],self.a[z+1]=self.a[z+1],self.a[z]

            

        

    def selection_sort(self):
        length=self.n
        for j in range(length-1):
            min=j
            for z in range(j,length):
                if(self.a[z]<self.a[min]):
                    min=z
                
            if(min!=j):
                self.a[j],self.a[min]=self.a[min],self.a[j]



        


    def insertion_sort(self):                                   
        length=self.n
        for j in range(1,length):
            z=j
            while(z>0):
                if(self.a[z]<self.a[z-1]):
                    self.a[z],self.a[z-1]=self.a[z-1],self.a[z]
                else:
                    break
                z-=1
                
            


        
       
while True:
    
    print("1.Bubble Sort")
    print("2.Selection Sort")
    print("3.Insertion Sort")
    print("Any key to exit")
    
    ch=int(input("Enter your choice:"))

    print("Enter the elements of array",end="\n\n")

    ob1=sort()
    if(ch==1):
        ob1.bubble_sort()
        ob1.trans()
            
    elif(ch==2):
        ob1.selection_sort()
        ob1.trans()
        
    elif(ch==3):
        ob1.insertion_sort()
        ob1.trans()        
    else:
        break
    
