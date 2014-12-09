''' Box Locker '''
from Tkinter import *
from time import *
import sys
''' Global Valueable. '''
listCustomer = ['---EMPTY---'] * 61
listCountDayInBox = [(-1, 0)] * 61 # First:Count Day, Second: Begin Day
listColorInBox = ['WHITE'] * 61
#--------------------------------------------------------------------------------------------------------------------------------------
class Frame(object):
    def __init__(self):
        ''' Initial Main Frame. '''
        root = Tk()
        root.geometry("800x630+100+20")
        root.resizable(width=FALSE, height=FALSE)
        root.title("Box Locker")
        root.config(bg = "#222222")
        #------------------------------------------------------------------------------------------------------------------------------
        ''' LOGO Picture. '''
        self.photo = PhotoImage(file = "logo.gif")
        self.label = Label(image = self.photo)
        self.label.image = self.photo # keep a reference!
        self.label.place(x = 350, y = 25)
        #------------------------------------------------------------------------------------------------------------------------------
        ''' SET DATE. [Ref.Calendar in your PC]'''
        skipDay = IntVar()
        skip = IntVar()
        timelocal = localtime()
        dayInWeek = strftime('%A ')
        Day = strftime('%d ')
        Day = int(Day)
        Month = strftime(' %B ')
        Year = strftime('%Y')
        self.Today = dayInWeek + str(Day) + Month + Year
        self.YesterDay = 0
        Label(root, text="SKIP DAY", fg="white", bg="#222222", font = 13).place(x = 500, y = 95)
        Spinbox(root, from_= Day, to=32, textvariable = skipDay, command = lambda: self.showDay(skipDay.get(), root, self.Today), font = 13).place(x = 580, y = 95, width = 40)
        Label(root, text= 'Today : ' + self.Today, fg="white", bg="#222222", font=13).place(x = 100, y = 95)
        #------------------------------------------------------------------------------------------------------------------------------
        ''' Create 60 Boxs. '''
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
            down += 80
            right = 0
            for j in xrange(10):
                self.button_value[block] = Button(root, text = block+1, command = lambda block=block : self.clickBox(block+1, self.Today), font=15, bg = self.colour.get())
                self.button_value[block].place(x = right, y = down, width = 80, height = 80)
                right += 80
                block += 1
                
        #######MAIN#######
        root.mainloop()###
        ##################
        
    def clickBox(self, number, Today):
        ''' Input: (Index of box, Date) -> Output:Send Index of box and Date to Class BOX.'''
        
        listColorInBox[number-1] = 'GREY'
        dayInWeek, Day, Month, Year = Today.split()
        if listCountDayInBox[number-1][0] == -1:
                listCountDayInBox[number-1] = 0, int(Day)
        Box(number, self.Today)

    def showDay(self, day, root, today):
        ''' Input: (day, root, date) -> Output: Show Date and Color of Box after click skipDay.'''
        #------------------------------------------------------------------------------------------------------------------------------
        ''' DATE : Skip Day [Next/Previous]. '''
        week = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tueday']
        month = ['December', 'January']
        year = ['2014', '2015']
        dayInWeek, Day, Month, Year = today.split()
        skip = day - int(Day)
        self.Today = week[(week.index(dayInWeek) + skip)%7] +' '+ str([day%32, 1][day%32==0]) +' '+ str(month[[0, 1][day>31]]) +' '+ str(year[[0, 1][day>31]])
        Label(root, text = ('%50s' % (' '*120)), fg="white", bg="#222222").place(x = 100, y = 95) #clear old date.
        Label(root, text= 'Today : ' + self.Today, fg="white", bg="#222222", font=13).place(x = 100, y = 95)
        #------------------------------------------------------------------------------------------------------------------------------
        ''' CountDay : Skip Day [Next/Previous]. '''
        DAY = int(Day)
        skipBOX = 0 #chk skipbox not Up/Down
        for number in xrange(len(listCountDayInBox)):
            if self.YesterDay <= day:
                skipBOX = 1
                if listCountDayInBox[number][0] >= 0:
                    listCountDayInBox[number] = (DAY - listCountDayInBox[number][1], listCountDayInBox[number][1])
            else:
                skipBOX = 2
                if listCountDayInBox[number][0] >= 0:
                    listCountDayInBox[number] = ([listCountDayInBox[number][0] - 1, 0][listCountDayInBox[number][0] - 1 <= 0], listCountDayInBox[number][1])
        if skipBOX == 1:
            self.YesterDay = DAY + 1
        elif skipBOX == 2:
            self.YesterDay = DAY - 1
        #------------------------------------------------------------------------------------------------------------------------------
        ''' Set Condition Color in Box.'''
        for number in xrange(len(listColorInBox)):
            if 1 <= listCountDayInBox[number][0] < 2:
                listColorInBox[number] = 'GREY'
            elif listCountDayInBox[number][0] == 2:
                listColorInBox[number] = 'YELLOW'
            elif listCountDayInBox[number][0] == 3:
                listColorInBox[number] = 'ORANGE'
            elif listCountDayInBox[number][0] >= 4:
                listColorInBox[number] = 'RED'
        #------------------------------------------------------------------------------------------------------------------------------
        ''' Update Color in Box '''
        block = 0
        right = 0
        down = 65
        for i in xrange(6):
            down += 80
            right = 0
            for j in xrange(10):
                self.button_value[block] = Button(root, text = block+1, command = lambda block=block : self.clickBox(block+1, self.Today), font=15, bg = listColorInBox[block])
                self.button_value[block].place(x = right, y = down, width = 80, height = 80)
                right += 80
                block += 1

#--------------------------------------------------------------------------------------------------------------------------------------
class Box(object):
    def __init__(self, value, date):
        ''' Initial Box Frame. [Pop up] '''
        box = Tk()
        box.geometry("400x230+950+50")
        box.resizable(width=FALSE, height=FALSE)
        box.title("Box Locker : " + str(value))
        box.config(bg = "#f7fac1")
        Label(box, text = "Box : " + str(value), fg="BLACK", bg="#f7fac1", font=13).place(x = 200, y = 30, anchor = CENTER)
        #------------------------------------------------------------------------------------------------------------------------------
        ''' Input: Name. '''
        Label(box, text = "Name ", fg="BLACK", bg="#f7fac1", font=13).place(x = 125, y = 55, anchor = CENTER)
        self.name = StringVar(box)
        Entry(box, textvariable = self.name).place(x = 210, y = 55, anchor = CENTER)
        
        Label(box, text = listCustomer[value], fg="BLACK", bg="#f7fac1", font=13).place(x = 200, y = 125, anchor = CENTER)
        if listCustomer[value] == '---EMPTY---':
            Button(box, text = "Save", command = lambda: self.getData(self.name.get(), value, box, date), bg = "#f1f4b2").place(x = 200 ,y = 195, anchor = CENTER)
        else:
            Button(box, text = "Close", command = lambda: self.closeButton(box), bg = "#f1f4b2").place(x = 200 ,y = 195, anchor = CENTER)
        box.mainloop()

    def closeButton(self, box):
        ''' Close Button. '''
        box.destroy()

    def getData(self, name, number, box, today):
        ''' Detail customer. '''
        week = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tueday']
        month = ['December', 'January']
        year = ['2014', '2015']
        listCustomer[number] = ''
        expire_inweek, expire_day, expire_month, expire_year = today.split()
        expireDay = ''
        expireDay += week[(week.index(expire_inweek) + 5) % 7] +' '+ str(int(expire_day)+5) +' '+ str(expire_month) +' '+str(expire_year)
        listCustomer[number] += 'Name : ' + name + '\n\nCheck In : ' + today + '\n\nExpire : ' + expireDay
        box.destroy()

#--------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    Frame()
