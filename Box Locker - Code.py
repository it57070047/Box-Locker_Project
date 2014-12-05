''' Box Locker '''
from Tkinter import *
from time import *
import sys

listCustomer = ['---EMPTY---'] * 61
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
        dayInWeek = strftime('%A ')
        Day = strftime('%d ')
        Month = strftime('%B ')
        Year = strftime('%Y')
        self.Today = dayInWeek + Day + Month + Year
        Label(root, text="SKIP DAY").place(x = 475, y = 55)
        Spinbox(root, from_= Day, to=32, textvariable = skipDay,  command = lambda: self.showDay(skipDay.get(), root, self.Today)).place(x = 535, y = 55, width = 35)
        Label(root, text= 'Today : ' + self.Today).place(x = 100, y = 55)
        
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
                self.button_value[block] = Button(root, text = block+1, command = lambda block=block : self.clickBox(block+1, self.Today), bg = self.colour.get())
                self.button_value[block].place(x = right, y = down, width = 80, height = 80)
                right += 80
                block += 1
                
        ##################
        root.mainloop()###
        ##################
        
    def clickBox(self, number, Today):
        self.colour.set('White' if self.colour.get() != 'White' else 'Grey')
        self.button_value[number-1].configure(bg='Grey')
        print number, self.Today
        Box(number, self.Today)

    def showDay(self, day, root, today):
        week = ['Wednessday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tueday']
        month = ['December', 'January']
        year = ['2014', '2015']
        dayInWeek, Day, Month, Year = today.split()
        skip = day - int(Day)
        self.Today = week[(week.index(dayInWeek) + skip)%7] +' '+ str([day%32, 1][day%32==0]) +' '+ str(month[[0, 1][day>31]]) +' '+ str(year[[0, 1][day>31]])
        print self.Today
        Label(root, text = ('%50s' % (' '*120))).place(x = 100, y = 55) #clear screen
        Label(root, text= 'Today : ' + self.Today).place(x = 100, y = 55)        
    
class Box(object):
    def __init__(self, value, date):
        box = Tk()
        box.geometry("400x230")
        box.resizable(width=FALSE, height=FALSE)
        box.title("Box Locker : " + str(value))
        Label(box, text = "Box : " + str(value)).place(x = 200, y = 35, anchor = CENTER)

        Label(box, text = "Name ", ).place(x = 125, y = 55, anchor = CENTER)
        self.name = StringVar(box)
        Entry(box, textvariable = self.name).place(x = 210, y = 55, anchor = CENTER)

        Label(box, text = listCustomer[value]).place(x = 200, y = 105, anchor = CENTER)

        if listCustomer[value] == '---EMPTY---':
            Button(box, text = "Save", command = lambda: self.getData(self.name.get(), value, box, date)).place(x = 200 ,y = 175, anchor = CENTER)
        else:
            Button(box, text = "Close", command = lambda: self.closeButton(box)).place(x = 200 ,y = 175, anchor = CENTER)
        box.mainloop()

    def closeButton(self, box):
        box.destroy()

    def getData(self, name, number, box, today):
        week = ['Wednessday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tueday']
        month = ['December', 'January']
        year = ['2014', '2015']
        listCustomer[number] = ''
        expire_inweek, expire_day, expire_month, expire_year = today.split()
        #print week[(week.index(expire_inweek) + 5) % 7]
        expireDay = ''
        expireDay += week[(week.index(expire_inweek) + 5) % 7] +' '+ str(int(expire_day)+5) +' '+ str(expire_month) +' '+str(expire_year)
        
        listCustomer[number] += 'Name : ' + name + '\n\nCheck In : ' + today + '\n\nExpire : ' + expireDay
        box.destroy()

#--------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    Frame()
