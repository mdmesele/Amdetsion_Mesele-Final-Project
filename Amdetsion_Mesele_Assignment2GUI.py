from tkinter import*

def bool():
    Q1 = str(entry1.get())
    Q2 = str(entry2.get())
    Q3 = str(entry3.get())
    Q4 = str(entry4.get())
    Q5 = str(entry5.get())

    if Q1 == "D" or Q1 == "d":
        output_label1.configure(text="You are correct",bg="green")
    elif Q1 != "D" or Q1 != "d":
        output_label1.configure(text="You are wrong! Try again",bg="red")
    if Q2 == "G" or Q2 == "g":
        output_label2.configure(text="You are correct",bg="green")
    elif Q2 != "G" or Q2 != "g":
        output_label2.configure(text="You are wrong! Try again",bg="red")
    if Q3 == "F" or Q3 == "f":
        output_label3.configure(text="You are correct",bg="green")
    elif Q3 != "F" or Q3 != "f":
        output_label3.configure(text="You are wrong! Try again",bg="red")
    if Q4 == "E" or Q4 == "e":
        output_label4.configure(text="You are correct",bg="green")
    elif Q4 != "E" or Q4 != "e":
        output_label4.configure(text="You are wrong! Try again",bg="red")
    if Q5 == "3":
        output_label5.configure(text="You are correct",bg="green")
    elif Q5 != "3":
        output_label5.configure(text="You are wrong! Try again",bg="red")

root = Tk()
root.geometry("900x200")
root.title("Neighbors")


label1 = Label(text="1. who lives in the first corner",font="verdana")
label1.grid(row=3, column=0)

entry1 = Entry()
entry1.grid(row=3,column=1)

label2 = Label(text="2. who lives in the middle",font="verdana")
label2.grid(row=4, column=0)

entry2 = Entry()
entry2.grid(row=4,column=1)

label3 = Label(text="3. enter the person who live between B and G",font="verdana")
label3.grid(row=5, column=0)

entry3 = Entry()
entry3.grid(row=5,column=1)

label4 = Label(text="4. who is the neighbour of A",font="verdana")
label4.grid(row=6, column=0)
entry4 = Entry()
entry4.grid(row=6,column=1)

label5 = Label(text="5. how many houses are between A and G",font="verdana")
label5.grid(row=7, column=0)
entry5 = Entry()
entry5.grid(row=7,column=1)

button = Button(text="Evaluate Answer",font="liberation 15 bold",bg="green",fg="white", command=bool)
button.grid(row=8,column=1,columnspan=2)

output_label1 = Label(font="liberation 15 ")
output_label2 = Label(font="liberation 15 ")
output_label3 = Label(font="liberation 15 ")
output_label4 = Label(font="liberation 15 ")
output_label5 = Label(font="liberation 15 ")


output_label1.grid(row=3,column=3)


output_label2.grid(row=4,column=3)
output_label3.grid(row=5,column=3)
output_label4.grid(row=6,column=3)
output_label5.grid(row=7,column=3)


root.mainloop()