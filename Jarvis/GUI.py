from tkinter import* 
from PIL import Image, ImageTk                                                      
import speech_to_text 
import action     
root = Tk()  
root.title("JARVIS")  
root.geometry("550x675")   
root.resizable(False, False)  
root.config(bg="black") 

# ask function

def ask():
    user_val = speech_to_text.speech_to_text() 
    bot_val = action.Action(user_val) 
    text.insert(END, 'Mr.Aditya--->' + user_val + "\n") 
    if bot_val != None:
        text.insert(END, "JARVIS <---" + str(bot_val) + "\n") 
    if bot_val == "ok mr.aditya":  
        root.destroy()      

def send():
    send = entry.get() 
    bot = action.Action(send) 
    text.insert(END, 'Mr.Aditya--->' + send + "\n")  
    if bot != None:
        text.insert(END, "JARVIS <---" + str(bot) + "\n") 
    if bot == "ok mr.aditya":  
        root.destroy() 
    
    
    
def del_text():
    text.delete('1.0', "end")  


# Frame

frame = LabelFrame(root, padx = 100, pady = 7, borderwidth = 3, relief = "raised")  
frame.config(bg="black")
frame.grid(row = 70, column = 90, padx = 55, pady = 10) 

# Text Label

text_label = Label(frame, text = "JARVIS", font = ("comic Sans ms", 14, "bold"))  
text_label.grid(row = 70, column = 0, padx = 40, pady = 30)  


# image                                                                         
image = ImageTk.PhotoImage(Image.open("image/jarvis1.png"))                              
image_label = Label(frame, image = image) 
image_label.grid(row = 1, column = 0, pady = 20,)


# Adding a Text Widget

text = Text(root, font =('courier 10 bold')) 
text.grid(row = 2, column =0) 
text.place(x = 100, y = 375, width = 375, height = 100) 

# Entry widget

entry = Entry(root, justify = CENTER)
entry.place(x = 100, y = 500, width = 375, height = 30) 


# Button 1

Button1 = Button(root, text = "ASK", bg = 'white', pady = 16, padx = 40, borderwidth = 3, relief = SOLID, command = ask)
Button1.place(x = 70, y = 575) 

# Button 2 

Button2 = Button(root, text = "SEND", bg = 'white', pady = 16, padx = 40, borderwidth = 3, relief = SOLID, command = send) 
Button2.place(x = 400, y = 575)

# Button 3 

Button3 = Button(root, text = "DELETE", bg = 'white', pady = 16, padx = 40, borderwidth = 3, relief = SOLID, command = del_text) 
Button3.place(x = 225, y = 575)


root.mainloop()  

