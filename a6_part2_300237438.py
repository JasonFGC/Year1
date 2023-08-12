class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'




class Rectangle:
    def __init__(self,bottomleft,topright,color):
        '''Rectangle,Point,Point,Str -> none
        initializes a rectangle with the 2 points as the bottom left and top right of the rectangle with the color given.
        Preconditions: first point must be smaller than the second point.
        '''
        self.bl=bottomleft
        self.tr=topright
        self.c=color
    def __repr__(self):
        '''Recttangle->str
        Returns a string representation of the rectangle
        '''
        return 'Rectangle('+str(self.bl)+','+str(self.tr)+','+'"'+str(self.c)+'"'+")"
    def __eq__(self,other):
        '''Rectangle,rectangle
        Checks if the rectangles are the same.
        '''
        if self.bl==other.bl and self.tr==other.tr and self.c==other.c:
            return True
        else:
            return False
        
    def __str__(self):
        '''Rectangle->str
        Returns a nice representation of the rectangle.
        '''
        return "I am a "+str(self.c)+" rectangle with a bottom left corner at "+str(self.bl.get())+" and top right corner at "+str(self.tr.get())+"."
    def get_bottom_left(self):
        '''Rectangle->point
        returns the bottom left point of the rectangle
        '''
        return self.bl
    def get_top_right(self):
        '''rectangle->point
        returns the top right point of the rectangle
        '''
        return self.tr
    def get_color(self):
        '''rectangle->str
        returns the color of the rectangle
        '''
        return self.c
    def reset_color(self,color):
        '''Rectangle,str->none
        Sets the color of the given rectangle to the given color.
        '''
        self.c=color
    def get_perimeter(self):
        '''Rectangle->num
        finds perimeter of the rectangle
        '''
        xbl=self.bl.get()[0]
        ybl=self.bl.get()[1]
        xtr=self.tr.get()[0]
        ytr=self.tr.get()[1]
        perim=((xtr-xbl)*2)+((ytr-ybl)*2)
        return perim
    def get_area(self):
        '''Rectangle->num
        finds area of the rectangle
        '''
        xbl=self.bl.get()[0]
        ybl=self.bl.get()[1]
        xtr=self.tr.get()[0]
        ytr=self.tr.get()[1]
        area=(xtr-xbl)*(ytr-ybl)
        return area
    def move(self,dx,dy):
        '''Rectangle,num,num->none
        moves the rectangle horizontally by dx and vertically by dy
        '''
        self.bl.move(dx,dy)
        self.tr.move(dx,dy)
    def intersects(self,other):
        '''Rectangle,Rectangle->bool
        finds if the two rectangles intersect. 
        '''
        xbl=self.bl.get()[0]
        ybl=self.bl.get()[1]
        xtr=self.tr.get()[0]
        ytr=self.tr.get()[1]
        
        xbl2=other.bl.get()[0]
        ybl2=other.bl.get()[1]
        xtr2=other.tr.get()[0]
        ytr2=other.tr.get()[1]
        if xbl > xtr2 or xbl2 > xtr or ybl > ytr2 or ybl2 > ytr: 
            return False
        else:
            return True
    def contains(self,x,y):
        '''Rectangle,num,num->bool
        finds if the point made with x and y is contained inside of the rectangle
        '''
        if x<=self.tr.get()[0] and y<=self.tr.get()[1] and x>=self.bl.get()[0] and y>=self.bl.get()[1]:
            return True
        else:
            return False


class Canvas:
    def __init__ (self):
        '''Canvas->none
        initializes the canvas and makes an empty list for rectangles
        '''
        self.rects=[]
    def __len__(self):
        '''Canvas -> int
        returns the amount of rectangles in the canvas
        '''
        return len(self.rects)
    def __repr__ (self):
        '''Canvas->str
        returns a string representation of the canvas
        '''
        string=[]
        for i in range(len(self.rects)):
            string.append(repr(self.rects[i]))
        return "Canvas("+str(string)+")"
    def add_one_rectangle(self,rectangle):
        '''Canvas,Rectangle->none
        appends a rectangle into the canvas
        '''
        self.rects.append(rectangle)
    def count_same_color(self,color):
        '''canvas,str->int
        finds the amount of rectangles that are the given color
        '''
        count=0
        for i in range(len(self.rects)):
            if self.rects[i].c==color:
                count+=1
        return count
    def total_perimeter(self):
        '''canvas->number
        finds the total perimeter of all the rectangles
        '''
        totalp=0
        for i in range(len(self.rects)):
            totalp+=self.rects[i].get_perimeter()
        return totalp

    def min_enclosing_rectangle(self):
        '''canvas->rectangle
        finds the minimum sized rectangle needed to contain all the rectangles in the current canvas
        '''
        minY=0
        minX=0
        maxY=0
        maxX=0
        for i in range(len(self.rects)):
            if i ==0:
                minY=self.rects[i].get_bottom_left().get()[1]
                minX=self.rects[i].get_bottom_left().get()[0]
                maxY=self.rects[i].get_top_right().get()[1]
                maxX=self.rects[i].get_top_right().get()[0]
            else:
                if minY>self.rects[i].get_bottom_left().get()[1]:
                    minY=self.rects[i].get_bottom_left().get()[1]
                if minX>self.rects[i].get_bottom_left().get()[0]:
                    minX=self.rects[i].get_bottom_left().get()[0]
                if maxY<self.rects[i].get_top_right().get()[1]:
                    maxY=self.rects[i].get_top_right().get()[1]
                if maxX<self.rects[i].get_top_right().get()[0]:
                    maxX=self.rects[i].get_top_right().get()[0]
        return Rectangle(Point(minX,minY),Point(maxX,maxY),'red')
    
    def common_point(self):
        '''canvas->bool
        finds if there is a common point that is contained by all the rectangles
        '''
        x=True
        for i in range(len(self.rects)):
            for j in range(i+1,len(self.rects)):
                if self.rects[i].intersects(self.rects[j]) == False:
                    x=False

        return x














    
