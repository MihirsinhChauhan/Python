from tkinter import *

def convert():
    global km,miles
    km = 1.6093 * float(miles)
    label4.config(text=f"{round(km, 2)}")

window = Tk()
window.title("Miles to kilometer converter")
window.minsize(width=500,height=200)
window.config(padx=50,pady= 50)

#input
input = Entry(width=20)
miles = input.get()
input.grid(row=1,column=2)

#label
label1 = Label(text="                           ")
label1.grid(row=1,column=1)

label2 = Label(text="Miles")
label2.grid(row=1,column=3)

label3 = Label(text= "is equal to ")
label3.grid(row=2,column=1)

km = 0

label4 = Label(text= f"{km}")
label4.grid(row=2,column=2)

label5 = Label(text="km")
label5.grid(row=2,column=3)



cal = Button(text = "calculate", command=convert)
cal.grid(row=3,column=2)
window.mainloop()