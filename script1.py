from tkinter import *

#creating an empty window
window = Tk()

# function to clear input
def clearText(textBox):
    textBox.delete("1.0", "end")

# function to convert integers and insert into correct fields
def convert():

    # get user input and multiply by 1000 for kg -> grams
    converted_grams = float(kg_value.get()) * 1000

    # get user input and multiply by 2.20462 for kg -> pounds
    converted_pounds = float(kg_value.get()) * 2.20462

    # get user input and multiply by 35.274 for kg -> ounces
    converted_ounces = float(kg_value.get()) * 35.274

    # clearing text and adding new converted value into appropriate box
    clearText(grams)    #clearing text if there was old input
    grams.insert("end", converted_grams)   # adding new input

    clearText(pounds)
    pounds.insert("end", converted_pounds)

    clearText(ounces)
    ounces.insert("end", converted_ounces)

##label
label = Label(text="Kg")
label.grid(row = 0,column = 0)  ##first

# Kg input
# Entry() = single line entry from user
kg_value = StringVar()
kg = Entry(window, textvariable = kg_value)  ##textvariable will get value from user, which is converted to string
kg.grid(row = 0, column = 1)

##convert button
b1 = Button(window, text="Convert", command = convert) ##passing function name as parameter with NO paranthesis
# b1.pack() ##pack method is a widget method
b1.grid(row=0,column=2)

# Create three empty text boxes for converted output integers
grams = Text(window, height = 1, width = 30)
grams.grid(row = 1, column = 0)

pounds = Text(window, height = 1, width = 30)
pounds.grid(row = 1, column = 1)

ounces = Text(window, height = 1, width = 30)
ounces.grid(row = 1, column = 2)

#needed to close the program - always at end of code
window.mainloop()
