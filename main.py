import sys
import tkinter as tk
from tkinter import *
import urllib.request
import webbrowser
from functools import partial
from tkinter import Tk, StringVar , ttk

      
window = Tk()
window.title('All In One Converter')
window.geometry("450x400+100+200")
labelfont = ('arial', 56, 'bold')
l=Label(window,text='ALL IN ONE CONVERTER',font = ("Arial", 16), justify = CENTER)
l.place(x=80,y=20)

widget = Button(None, text="QUIT", bg="red", fg="black",font = ("Arial", 14, "bold"), justify = CENTER, command=window.destroy).place(x=70,y=350)



def weight_conversion():
    factors = {'kg' : 1000, 'hg' : 100, 'dg' : 10, 'g' : 1,'deg' : 0.1, 'cg' : 0.01, 'mg' : 0.001}
    units = {"Kilogram" : 'kg', "Hectagram" : 'hg', "Decagram" : 'dg', "Decigram" : 'deg', "Kilogram" : 'kg', "gram" : 'g', "centigram" : 'cg', "milligram" : 'mg'}
  
    def convert(val, inp, to):
        if inp != 'g':
            val = val * factors[inp]
            return val / factors[to]
        else:
            return val / factors[to]

    def callback():
        try:
            val = float(in_field.get())
        except ValueError:
            out_val.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_val.set('Input or output unit not chosen')
            return None
        else:
            inp = units[in_unit.get()]
            to = units[out_unit.get()]
            out_val.set(convert(val, inp, to))

    window = Toplevel()
    window.title("Weight Converter")

   
    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Weight Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)

    in_val = StringVar()
    in_val.set('0')
    out_val = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_val)
    in_field.grid(row=1, column=2, sticky=(W, E))

    in_select = OptionMenu(mainframe, in_unit, "Kilogram","Hectagram","Decagram", "gram", "Decigram","Centigram", "Milligram") .grid(column=3, row=1, sticky=W)

    

    ttk.Entry(mainframe, textvariable=out_val, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Kilogram","Hectagram","Decagram", "gram", "Decigram","Centigram", "Milligram").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()


def area_conversion():
    wind = Toplevel()
    wind.minsize(width=400, height=150)
    wind.maxsize(width=400, height=150) 

    mf = {'square meter':1,'square km':1000000,'square rood':1011.7141056,'square cm':0.0001,'square foot':0.09290304 ,
                    'square inch':0.00064516, 'square mile':2589988.110336, 'milimeter':0.000001,'square rod':25.29285264,
                    'square yard':0.83612736, 'square township':93239571.9721, 'square acre':4046.8564224 ,'square are': 100,
                    'square barn':1e-28, 'square hectare':10000, 'square homestead':647497.027584 }

       

    def convert(x, fromUnit, toUnit):    
        if fromVar.get() in mf.keys() and toVar.get() in mf.keys():     
            resultxt.delete(0, END)
            result = (float(str(x))*mf[fromUnit])/(mf[toUnit])
            resultxt.insert(0, str(result))
       


    titleLabel = Label (wind, text = "Area Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)

    e = Entry(wind)
    e.grid(row = 1, column = 2)    
    values = list(mf.keys())    

    fromVar = StringVar(wind)
    toVar = StringVar(wind)
    fromVar.set("From Unit")
    toVar.set("To Unit")

  
    fromOption = OptionMenu(wind, fromVar, *values, command= lambda y: convert(e.get(), fromVar.get() ,toVar.get()))
    fromOption.grid(row=1, column = 3)

    toLabel = Label(wind, text="To : ", font="Arial").grid(row=2, column = 2)  
    toOption = OptionMenu(wind, toVar, *values, command= lambda x: convert(e.get(), fromVar.get() ,toVar.get()))
    toOption.grid(row=3, column = 3)

    resultxt = Entry(wind)
    resultxt.grid(row=3, column=2) 

    



def length_conversion():
        
    factors = {'nmi' : 1852, 'mi' : 1609.34, 'yd' : 0.9144, 'ft' : 0.3048, 'inch' : 0.0254, 'km' : 1000, 'm' : 1, 'cm' : 0.01, 'mm' : 0.001}
    units = {"Nautical Miles" : 'nmi', "Miles" : 'mi', "Yards" : 'yd', "Feet" : 'ft', "Inches" : 'inch', "Kilometers" : 'km', "meters" : 'm', "centimeters" : 'cm', "millileters" : 'mm'}


    def convert(val, inp, to):
        if inp != 'm':
            val = val * factors[inp]
            return val / factors[to]
        else:
            return val / factors[to]

    def callback():
        try:
            val = float(in_field.get())
        except ValueError:
            out_val.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_val.set('Input or output unit not chosen')
            return None
        else:
            inp = units[in_unit.get()]
            to = units[out_unit.get()]
            out_val.set(convert(val, inp, to))


    window = Toplevel()
    window.title("Length Converter")

    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label (mainframe, text = "Length Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)

    in_val = StringVar()
    in_val.set('0')
    out_val = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_val)
    in_field.grid(row=1, column=2, sticky=(W, E))

    in_select = OptionMenu(mainframe, in_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "meters", "centimeters", "millileters").grid(column=3, row=1, sticky=W)

    

    ttk.Entry(mainframe, textvariable=out_val, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "meters", "centimeters", "millileters").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()




def temp_conversion():
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()



        if celTempVar.get() != 0.0:
            celToFah = (celTemp *  9/5 + 32)
            fahTempVar.set(celToFah)

        elif fahTempVar.get() != 0.0:
            fahToCel = ((fahTemp - 32) * (5/9))
            celTempVar.set(fahToCel)

    def reset():
        top = Toplevel(padx=50, pady=50)
        top.grid()
        message = Label(top, text = "Reset Complete")
        button = Button(top, text="OK", command=top.destroy)

        message.grid(row = 0, padx = 5, pady = 5)
        button.grid(row = 1, ipadx = 10, ipady = 10, padx = 5, pady = 5)

        fahTempVar.set(int(0))
        celTempVar.set(int(0)) 
    top = Toplevel()
    top.title("Temperature Converter")
    
  
  
    celTempVar = IntVar()
    celTempVar.set(int(0))
    fahTempVar = IntVar()
    fahTempVar.set(int(0))
    titleLabel = Label (top, text = "Temperature Converter", font = ("Arial", 12, "bold"), justify = CENTER).grid(column=1,row=1)
   

    celLabel = Label (top, text = "Celsius: ", font = ("Arial", 16), fg = "light green")
    celLabel.grid(row = 2, column = 1, pady = 10, sticky = NW)

    fahLabel = Label (top, text = "Fahrenheit: ", font = ("Arial", 16), fg = "blue")
    fahLabel.grid(row = 3, column = 1, pady = 10, sticky = NW)

    celEntry = Entry (top, width = 10, bd = 5, textvariable = celTempVar)
    celEntry.grid(row = 2, column = 1, pady = 10, sticky = NW, padx = 125 )


    fahEntry = Entry (top, width = 10, bd = 5, textvariable = fahTempVar)
    fahEntry.grid(row = 3, column = 1, pady = 10, sticky = NW, padx = 125 )

    convertButton =Button (top, text = "Convert", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, command = convert)
    convertButton.grid(row = 4, column = 1, ipady = 8, ipadx = 12, pady = 5, sticky = NW, padx = 55)

    resetButton = Button (top, text = "Reset", font = ("Arial", 8, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "light green", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command = reset)
    resetButton.grid(row = 4, column = 2,ipady = 8, ipadx = 12, pady = 5, sticky = NW)
    



widget = Button(window, text="Temperature converter", bg="green" , fg="black",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, command=temp_conversion).place(x=70,y=120)
widget = Button(window, text="Length Converter", bg="green" , fg="black",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, command=length_conversion).place(x=70,y=180)
widget = Button(window, text="Area Converter", bg="green" , fg="black",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, command=area_conversion).place(x=70,y=240)
widget = Button(window, text="Weight Converter", bg="green" , fg="black",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, command=weight_conversion).place(x=70,y=300)


window.mainloop()
