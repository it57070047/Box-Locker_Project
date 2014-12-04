''' Box Locker '''
from Tkinter import *
from time import *
import sys

class Frame(object):
    def __init__(self):               
        root = Tk()
        root.geometry("800x630")
        root.resizable(width=FALSE, height=FALSE)
        root.title("Box Locker")
        self.photo = PhotoImage(file = "logo.gif")
        self.label = Label(image = self.photo)
        self.label.image = self.photo # keep a reference!
        self.label.place(x = 350, y = 5)

        skipDay = IntVar()
        skip = IntVar()
        timelocal = localtime()
        self.day_in_week = timelocal[3]
        self.day = timelocal[2]
        self.month = timelocal[1]
        self.year = timelocal[0]
        Label(root, text="SKIP DAY").place(x = 475, y = 55)
        Spinbox(root, from_=self.day, to=32, textvariable = skipDay,  command = lambda: self.showDay(skipDay.get())).place(x = 535, y = 55, width = 35)
        month_year = 'December 2014'
        Label(root, text=strftime('Today :  %A %d ') + ('%s' % month_year)).place(x = 100, y = 55)

        number = []
        for i in xrange(1, 61):
            number.append(str(i))
        self.button_value = [0]*61
        self.colour = StringVar()
        self.colour.set('White')
        time = localtime()    
        block = 0
        right = 0
        down = 65
        for i in xrange(6):
            box = number[block]
            down += 80
            right = 0
            for j in xrange(10):
                self.button_value[block] = Button(root, text = block+1, command = lambda block=block : self.clickBox(block+1), bg = self.colour.get())
                self.button_value[block].place(x = right, y = down, width = 80, height = 80)
                right += 80
                block += 1
                
        ##################
        root.mainloop()###
        ##################
        
    def clickBox(self, number):
        self.colour.set('White' if self.colour.get() != 'White' else 'Grey')
        self.button_value[number-1].configure(bg='Grey')
        print number
        Box(number)

    def showDay(self, v):
        week = ['Wednessday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tueday']
        month = ['December', 'January']
        year = ['2014', '2015']
        Label(root, text = ('%50s' % (' '*120))).place(x = 100, y = 55)
        Label(root, text = ('Today : %s %s %s %s' % (week[(v - self.day)% 7], [v%32, 1][v%32==0], month[[0, 1][v>31]], year[[0, 1][v>31]]))).place(x = 100, y = 55)
    
class Box(object):
    def __init__(self, value):
        box = Tk()
        box.geometry("400x230")
        box.resizable(width=FALSE, height=FALSE)
        box.title("Box Locker : " + str(value))
        Label(box, text = "Box : " + str(value)).place(x = 200, y = 35, anchor = CENTER)
        Label(box, text = "Name ", ).place(x = 115, y = 55, anchor = CENTER)
        self.name = StringVar(box)
        Entry(box, textvariable = self.name).place(x = 200, y = 55, anchor = CENTER)
        Submit = Button(box, text = "Save", command = lambda: self.getData(self.name.get())).place(x = 150, y = 175, anchor = CENTER)
        Button(box, text = "Close", command = lambda: self.closeButton(box)).place(x = 200 ,y = 175, anchor = CENTER)
        box.mainloop()

    def closeButton(self, box):
        box.destroy()

    def getData(self, name):
        print name

#--------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    Frame()
