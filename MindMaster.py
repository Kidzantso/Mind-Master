import tkinter as tk
from tkinter import *
import tkinter.messagebox
import random
LARGEFONT =("Arial", 10)
def resretandshow(e1,controller,page):
	e1.delete(0, 'end')
	controller.show_frame(page)
def Gamelogic(e1,code,counter,correctyes,correctno,controller):
	Page3.counter=counter+1
	text=e1.get()
	if text==code:
		tkinter.messagebox.showinfo("Message",f"You got it in {counter} tries!")
		e1.delete(0, 'end')
		Page3.counter=1
		controller.show_frame(StartPage)
	else:
		for i in range(4):
			if code[i] == text[i]:
							correctyes += 1
			elif code[i] in text:         
							correctno += 1
		tkinter.messagebox.showinfo("Message",f"You got {correctyes+correctno}  numbers correct and {correctyes} in correct position")
		e1.delete(0, 'end')

def checklength(e1,controller):
        text=e1.get()
        if len(text) == 4 and text.isdigit():resretandshow(e1,controller,Page3);tkinter.messagebox.showinfo("Message","Ok now we will go to player 2's turn,get ready!");Page3.code=text
        else:
            tkinter.messagebox.showwarning("Warning", "Only 4 numbers are allowed!");e1.delete(0, 'end')
def Oneplayer(controller):
	controller.show_frame(Page3);Page3.code= str(random.randrange(1000, 10000))

def checkanswer(e1,code,counter,correctyes,correctno,controller):
        text=e1.get()
        if len(text) == 4 and text.isdigit():Gamelogic(e1,code,counter,correctyes,correctno,controller)
        else:
            tkinter.messagebox.showwarning("Warning", "Only 4 numbers are allowed!");e1.delete(0, 'end')

class tkinterApp(tk.Tk):	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		
		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True) 
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {} 

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage,Page2,Page3):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, page1, page2 respectively with 
			# for loop
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew")
			frame.configure(bg="#5A47A5")

		self.show_frame(StartPage)
	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()    
        
# first window frame startpage

class StartPage(tk.Frame):
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent)
		
		# label of frame Layout 2
		label = Label(self, text ="Welcome to the Code Guess Game\nChoose an Option", font = LARGEFONT, bg="#5A47A5")
		
		# putting the label in its place by using grid
		label.grid(row = 1, column = 1) 

		buttononeplayer = Button(self, text ="One PLayer",
		command = lambda : Oneplayer(controller),
		width=17,bg="#3401FF", activebackground="#3401FF")
	
		# putting the button in its place by using grid
		buttononeplayer.grid(row = 3, column = 0, padx = 5)

		buttontwoplayers = Button(self, text ="Two Players",
		command = lambda : controller.show_frame(Page2),
		width=17,bg="#FF0101", activebackground="#FF0101")
	
		# putting the button in its place by
		# using grid
		buttontwoplayers.grid(row = 3, column = 2, padx = 10)


# third window frame page2
class Page2(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = Label(self, text ="It is Player 1's turn\nEnter your 4 digit code", font = LARGEFONT, bg="#5A47A5")
		label.grid(row = 1, column = 1, padx = 10, pady = 10)
		e1 = Entry(self)
		e1.configure({"background": "#6F6F6F"})
		e1.grid(row=1,column=2)
		# button to show frame 2 with text
		# layout2
		button1 = Button(self, text ="Done",bg="#CCA62C",command = lambda :checklength(e1,controller), activebackground="#CCA62C")
		button2 = Button(self, text ="Back",bg="#6D2061",command = lambda : resretandshow(e1,controller,StartPage), activebackground="#6D2061")
		# putting the button in its place by 
		# using grid
		button1.grid(row = 3, column = 3, padx = 10, pady = 10)
		button2.grid(row = 6, column = 3, padx = 10, pady = 10)	

class Page3(tk.Frame):
	code=0
	counter=1
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = Label(self, text ="It is Player 2's turn\nEnter your 4 digit Guess", font = LARGEFONT, bg="#5A47A5")
		label.grid(row = 1, column = 1, padx = 10, pady = 10)
		e1 = Entry(self)
		e1.configure({"background": "#6F6F6F"})
		e1.grid(row=1,column=2)
		# button to show frame 2 with text
		# layout2
		correctyes=0
		correctno=0
		button1 = Button(self,text ="Done",bg="#CCA62C",command=lambda :checkanswer(e1,self.code,self.counter,correctyes,correctno,controller), activebackground="#CCA62C")
		button2 = Button(self, text ="Back",bg="#6D2061",command = lambda : resretandshow(e1,controller,StartPage), activebackground="#6D2061")
		# putting the button in its place by 
		# using grid
		button1.grid(row = 4, column = 3, padx = 10, pady = 10)
		button2.grid(row = 6, column = 3, padx = 10, pady = 10)
			

# Driver Code
app = tkinterApp()
app.title('Code Guess')
app.geometry('500x500')
app.resizable(width=False, height=False)
app.mainloop()

# import os
# game=True
# turn=True
# while game:
#     print("Player 1's turn")
#     code = input("Enter your four digit code\n")
#     if len(code)!=4:
#         print("Invalid output,Only 4 numbers are allowed")
#     else:
#         clear = lambda: os.system('cls')
#         clear()
#         print("Now Player2's turn\n")
#         counter=0
#         Guess = input("Enter your guess\n")
#         while Guess!=code:            
#             if len(Guess)!=4:
#                 print("Invalid output,Only 4 numbers are allowed\n")
#             else:
#                 counter=counter+1
#                 correctyes=0
#                 correctno=0
#                 for i in range(4):
#                     if code[i] == Guess[i]:
#                         correctyes += 1
#                     elif code[i] in Guess:         
#                         correctno += 1
#                 print("You got ",correctyes+correctno," numbers correct and ", correctyes ," in correct position\n")
#             Guess = input("Enter your guess\n")
#         print("You Won!\nYou got in ",counter+1," tries\n")
