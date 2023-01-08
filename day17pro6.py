from tkinter import*
master=Tk()
demo_text="This is a sample demo of message widget."
msg=Message(master, text=demo_text)
msg.config(bg='yellow', font=('times',24,'italic'))
msg.pack()
