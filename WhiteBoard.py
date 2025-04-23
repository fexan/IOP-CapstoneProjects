'''
Author: Ifeoluwa Oyelowo-Paul
Date: April 11, 2025

White Board:
Created an application which allows you to draw pictures, write notes and use various colors to flesh out ideas for projects. 

- host online
- require auth 
- Add feature to invite friends to collaborate on a white board online.



Credits:
- https://tkdocs.com/tutorial/canvas.html
- https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06 
'''


from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor

class WhiteBoard():

    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        #title
        #label = ttk.Label(root,text="Welcome to IOP's Whiteboard",relief='ridge')
        #label.grid(row=0,column=1)
        self.root.title("Welcome to IOP's Whiteboard")


        #canvas
        self.canvas = Canvas(self.root, width=600, height=600, background='gray75')
        self.canvas.grid(row=1,column=1)

        #eraser button
        #self.eraser = ttk.Button(self.root,text="Eraser",command=self.use_eraser,style="TButton")
        #self.eraser.grid(row=1,column=2)

        #color button
        self.color_but = ttk.Button(self.root,text="Color",command=self.select_color,style="TButton")
        self.color_but.grid(row=1,column=3)


        #x,y coords and color
        self.lastx = None
        self.lasty = None
        self.color = self.DEFAULT_COLOR

    
        self.canvas.bind("<Button-1>", self.setxy)
        self.canvas.bind("<B1-Motion>", self.drawLine)
        self.canvas.bind('<ButtonRelease-1>', self.doneStroke)



        self.root.mainloop()

    def setxy(self,event):
        self.lastx , self.lasty = event.x , event.y 

    def drawLine(self,event):

        if self.lastx and self.lasty:
            self.canvas.create_line((self.lastx,self.lasty,event.x,event.y), fill = self.color, width = 5,tags='currentline')
            self.lastx, self.lasty = event.x,event.y
    
    def select_color(self):
        self.color = askcolor(color = self.color)[1]
    
    def doneStroke(self, event):
        self.canvas.itemconfigure('currentline', width=1)        

WhiteBoard()

'''

from nicegui import ui

ui.markdown("")

class WhiteBoardApp():

    def __init__(self):
        # Create a canvas element using NiceGUI
        self.mycanvas = ui.element('canvas').props('id=myCanvas width=800 height=800')
        self.mycanvas.style('border: 1px solid black;')

        self.drawing = False  # Flag to track if a stroke is in progress

        self.line_thickness = 2
        self.line_color = "black"





wb = WhiteBoardApp()
wb_slider = ui.slider(min=1, max=10).bind_value(wb, 'line_thickness')

ui.color_input(label='Color', value='#000000', on_change=lambda e: wb_slider.style(f'color:{e.value}'))

ui.run()

'''

'''



def on_mousedown(event):
    global drawing
    drawing = True
    drawing_canvas.set_position(event.x, event.y)

def on_mouseup(event):
    global drawing
    drawing = False

def on_mousemove(event):
    if drawing:
        drawing_canvas.draw_line(
            drawing_canvas.get_position()[0],  # Previous position
            drawing_canvas.get_position()[1],  # Previous position
            event.x,  # Current position
            event.y,  # Current position
            current_color,
            line_thickness,
        )
        drawing_canvas.set_position(event.x, event.y)

drawing_canvas.on_mousedown(on_mousedown)
drawing_canvas.on_mouseup(on_mouseup)
drawing_canvas.on_mousemove(on_mousemove)

 
ui.run()

''' 
