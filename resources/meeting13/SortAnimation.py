"""
Source: Lee & Hubbard (2015). "Data Structures and Algorithms with Python"
http://knuth.luther.edu/~leekent/CS2Plus/chap4/chap4.html

"""

import tkinter
import turtle
import random
import time
import math

class Point(turtle.RawTurtle):
    def __init__(self, canvas, x, y):
        super().__init__(canvas)
        canvas.register_shape("dot",((3,0),(2,2),(0,3),(-2,2),(-3,0),(-2,-2),(0,-3),(2,-2)))
        self.shape("dot")
        self.speed(0)
        self.penup()
        self.goto(x,y)

    def __str__(self):
        return "("+str(self.xcor())+","+str(self.ycor())+")"

    def __lt__(self, other):
        return self.ycor() < other.ycor()     

# This class defines the animation application. The following line says that
# the SortAnimation class inherits from the Frame class. 
class SortAnimation(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()    
        self.paused = False
        self.stop = False
        self.running = False


    def buildWindow(self):

        def partition(seq, start, stop):
            pivotIndex = start
            pivot = seq[pivotIndex]

            theTurtle.color("red")
            theTurtle.penup()
            theTurtle.goto(start,pivot.ycor())
            theTurtle.pendown()
            theTurtle.goto(stop,pivot.ycor())
            screen.update()

            # Why twice? Because once doesn't seem to display
            # the line the first time through for some reason            
            theTurtle.color("red")
            theTurtle.penup()
            theTurtle.goto(start,pivot.ycor())
            theTurtle.pendown()
            theTurtle.goto(stop,pivot.ycor())
            screen.update()

            i = start+1
            j = stop-1

            while i <= j:
                while i <= j and not pivot < seq[i]:
                    i+=1
                while i <= j and pivot < seq[j]:
                    j-=1

                if i < j:
                    tmp = seq[i]
                    seq[i] = seq[j]
                    seq[i].goto(i,seq[i].ycor())
                    seq[j] = tmp
                    seq[j].goto(j,seq[j].ycor())
                    screen.update()
                    i+=1
                    j-=1

            seq[pivotIndex] = seq[j]
            seq[pivotIndex].goto(pivotIndex,seq[pivotIndex].ycor())
            seq[j] = pivot
            seq[j].goto(j,seq[j].ycor())
            seq[j].color("green")
            screen.update()

            theTurtle.color("white")
            theTurtle.penup()
            theTurtle.goto(0,pivot.ycor())
            theTurtle.pendown()
            theTurtle.goto(len(seq),pivot.ycor())
            screen.update()   

            return j


        def quicksortRecursively(seq, start, stop):
            if start >= stop:
                return 

            if stopping():
                return

            pivotIndex = partition(seq, start, stop)

            if stopping():
                return

            quicksortRecursively(seq, start, pivotIndex)

            if stopping():
                return

            quicksortRecursively(seq, pivotIndex+1, stop)

        def quicksort(seq):
            quicksortRecursively(seq, 0, len(seq))   

        def merge(seq, start, mid, stop):
            length = stop - start
            log = math.log(length,2)

            theTurtle.color("blue")
            theTurtle.penup()
            theTurtle.goto(start,-3*log)
            theTurtle.pendown()
            theTurtle.forward(length)
            screen.update()

            lst = []
            i = start
            j = mid

            # Merge the two lists while each has more elements
            while i < mid and j < stop:
                if seq[i] < seq[j]:
                    lst.append(seq[i])
                    seq[i].goto(i,seq[i].ycor())
                    i+=1
                else:
                    lst.append(seq[j])
                    seq[j].goto(j,seq[j].ycor())
                    j+=1
                #screen.update()

            # Copy in the rest of the start to mid sequence    
            while i < mid:
                lst.append(seq[i])
                seq[i].goto(i,seq[i].ycor())
                i+=1
                #screen.update()

            # Copy in the rest of the mid to stop sequence
            while j < mid:
                lst.append(seq[j])
                seq[j].goto(j,seq[j].ycor())
                j+=1
                #screen.update()

            # Copy the elements back to the original sequence   
            for i in range(len(lst)):
                seq[start+i]=lst[i]
                lst[i].goto(start+i,lst[i].ycor())
                lst[i].color("green")
                screen.update()

        def mergeSortRecursively(seq, start, stop):
            # We must use >= here only when the sequence we are sorting
            # is empty. Otherwise start == stop-1 in the base case.
            if start >= stop-1:
                return 

            mid = (start + stop) // 2

            if stopping():
                return

            length = stop-start
            log = math.log(length,2)

            theTurtle.color("red")
            theTurtle.penup()
            theTurtle.goto(start,-3*log)
            theTurtle.pendown()
            theTurtle.forward(length)
            screen.update()

            # Why twice? Because once doesn't seem to display
            # the line the first time through for some reason
            theTurtle.color("red")
            theTurtle.penup()
            theTurtle.goto(start,-3*log)
            theTurtle.pendown()
            theTurtle.forward(length)
            screen.update()  

            mergeSortRecursively(seq, start, mid)

            if stopping():
                return            

            mergeSortRecursively(seq, mid, stop)

            if stopping():
                return

            theTurtle.color("blue")
            theTurtle.penup()
            theTurtle.goto(start,-3*log)
            theTurtle.pendown()
            theTurtle.forward(length)
            screen.update()

            merge(seq, start, mid, stop)

            screen.update()
            theTurtle.color("white")
            theTurtle.goto(start-1,-3*log)
            theTurtle.pendown()
            theTurtle.forward(length+2)
            screen.update()           

        def mergeSort(seq):
            mergeSortRecursively(seq, 0, len(seq))                     

        def select(seq, start):
            minIndex = start
            seq[minIndex].color("green")

            for i in range(start+1, len(seq)):
                if seq[minIndex] > seq[i]:
                    seq[minIndex].color("black")
                    minIndex = i
                    seq[minIndex].color("green")

            return minIndex

        def selectionSort(seq):
            for i in range(len(seq)-1):
                minIndex = select(seq, i)
                if stopping():
                    return
                tmp = seq[i]
                seq[i] = seq[minIndex]
                seq[minIndex] = tmp
                seq[i].goto(i,seq[i].ycor())
                seq[minIndex].goto(minIndex,seq[minIndex].ycor())
                seq[i].color("green")        

        def pause():
            while self.paused:
                time.sleep(1)
                screen.update()
                screen.listen()                

        def stopping():
            if self.paused:
                pause()

            if self.stop:
                self.pause = False
                self.running = False
                screen.update()
                screen.listen()                 
                return True

            return False

        self.master.title("Sort Animations")

        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)

        def clear():
            screen.clear() 
            screen.update()
            screen.listen()

        def newWindow():
            clear()
            if self.running:
                self.stop = True

        fileMenu.add_command(label="Clear",command=newWindow)
        fileMenu.add_command(label="Exit",command=self.master.quit)   
        bar.add_cascade(label="File",menu=fileMenu)
        self.master.config(menu=bar)    

        canvas = tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=tkinter.LEFT)

        theTurtle = turtle.RawTurtle(canvas)
        theTurtle.ht()
        theTurtle.speed(0)
        screen = theTurtle.getscreen()
        screen.tracer(0)

        sideBar = tkinter.Frame(self,padx=5,pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        speedLabel = tkinter.Label(sideBar,text="Animation Speed")
        speedLabel.pack()
        speed = tkinter.StringVar()
        speedEntry = tkinter.Entry(sideBar,textvariable=speed)
        speedEntry.pack()
        speed.set("10")            

        def selSortHandler():
            self.running = True
            clear()
            screen.setworldcoordinates(0,0,200,200)
            screen.tracer(0)
            self.master.title("Selection Sort Animation")
            seq = []
            for i in range(200):
                if stopping():
                    return

                p = Point(screen,i,i)
                p.color("green")
                seq.append(p)

            screen.update()
            screen.tracer(1)

            for i in range(200):
                if stopping():
                    return 

                j = random.randint(0,199)

                p = seq[i]
                seq[i] = seq[j]
                seq[j] = p
                seq[i].goto(i,seq[i].ycor())
                seq[j].goto(j,seq[j].ycor())
                seq[i].color("black")
                seq[j].color("black")

            selectionSort(seq)
            self.running = False 
            self.stop = False

        button = tkinter.Button(sideBar, text = "Selection Sort", command=selSortHandler)
        button.pack(fill=tkinter.BOTH) 

        def mergeSortHandler():
            self.running = True
            clear()
            screen.setworldcoordinates(0,-25,200,200)
            theTurtle.width(5)
            screen.tracer(0)
            self.master.title("Merge Sort Animation")
            seq = []
            for i in range(200):
                if stopping():
                    return

                p = Point(screen,i,i)
                p.color("green")
                seq.append(p)

            screen.update()
            screen.tracer(1)
            for i in range(200):
                if stopping():
                    return 

                j = random.randint(0,199)

                p = seq[i]
                seq[i] = seq[j]
                seq[j] = p
                seq[i].goto(i,seq[i].ycor())
                seq[j].goto(j,seq[j].ycor())
                seq[i].color("black")
                seq[j].color("black")

            screen.tracer(0) 
            mergeSort(seq)
            self.running = False 
            self.stop = False

        button = tkinter.Button(sideBar, text = "Merge Sort", command=mergeSortHandler)
        button.pack(fill=tkinter.BOTH)         

        def quickSortHandler():
            self.running = True
            clear()
            screen.setworldcoordinates(0,0,200,200)
            theTurtle.width(5)
            screen.tracer(0)
            self.master.title("Quicksort Animation")
            seq = []
            for i in range(200):
                if stopping():
                    return

                p = Point(screen,i,i)
                p.color("green")
                seq.append(p)

            screen.update()
            screen.tracer(1)
            for i in range(200):
                if stopping():
                    return 

                j = random.randint(0,199)

                p = seq[i]
                seq[i] = seq[j]
                seq[j] = p
                seq[i].goto(i,seq[i].ycor())
                seq[j].goto(j,seq[j].ycor())
                seq[i].color("black")
                seq[j].color("black")

            screen.tracer(1) 
            quicksort(seq)
            self.running = False 
            self.stop = False


        button = tkinter.Button(sideBar, text = "Quicksort", command=quickSortHandler)
        button.pack(fill=tkinter.BOTH)  

        def pauseHandler():
            self.paused = not self.paused

        button = tkinter.Button(sideBar, text = "Pause", command=pauseHandler)
        button.pack(fill=tkinter.BOTH)  

        def stopHandler():
            if not self.paused and self.running:
                self.stop = True

        button = tkinter.Button(sideBar, text = "Stop", command=stopHandler)
        button.pack(fill=tkinter.BOTH)  

        screen.listen()

# The main function in our GUI program is very simple. It creates the 
# root window. Then it creates the SortAnimation frame which creates 
# all the widgets and has the logic for the event handlers. Calling mainloop
# on the frames makes it start listening for events. The mainloop function will 
# return when the application is exited. 
def main():
    root = tkinter.Tk()  
    anim = SortAnimation(root)  

    anim.mainloop()

if __name__ == "__main__":
    main()