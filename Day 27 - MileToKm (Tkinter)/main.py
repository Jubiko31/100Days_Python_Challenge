from tkinter import * 

UNIT = 1.60934

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=70)

def calculate():
    miles = float(input.get())
    km = "{:.3f}".format(miles * UNIT)
    result["text"] = km

input = Entry(width=20)
input.grid(column=2, row=1, pady=10, padx=2)

is_equal = Label(text="Is equal to")
is_equal.grid(column=1, row=2)
miles_label = Label(text="Miles")
km_label = Label(text="Km")
miles_label.grid(column=3, row=1)
km_label.grid(column=3, row=2)

result = Label(text="", fg="#3CB043", font='Helvetica 16 bold')
result.grid(column=2, row=2, pady=10, padx=2)

btn = Button(text="Calculate", command=calculate)
btn.grid(column=2, row=3)

window.mainloop()