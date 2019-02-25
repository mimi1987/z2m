#INFOS

'''Title: Z2M-Calculator
Description: Zoll too meter converter
Author: MiMi
Copyright: 2017'''

from tkinter import *
import pyperclip as clip


#FUNCTIONS

def z2m(event): #Parameter needed for the bind function.
  ergebnis_meter = zoll_value.get() * 2.54 / 100
  ergebnis_label.config(text=ergebnis_meter)
  ergebnis_meter_2_kommastellen = "{:.2f}".format(ergebnis_meter) #Comma formating.
  clip.copy(ergebnis_meter_2_kommastellen) #Copys result too clipboard.
  

def whd_calc():
  width_v = width_value.get() * 2.54
  height_v = height_value.get() * 2.54
  depth_v = depth_value.get() * 2.54
  result_whd = "{:.1f}x{:.1f}x{:.1f}mm".format(width_v,height_v,depth_v)
  result_label_whd.config(text=result_whd)
  clip.copy(result_whd)
      
   
#GUI APP

window = Tk()
window.bind('<Return>', z2m) #Process is triggerd by the enter key.
window.title("Inches2Meter")
window.attributes("-topmost", True) #Window stays in front.

titel_label = Label(window, text="Inches2Meter", font=("bold",15))
titel_label.grid(row=0, column=1)

zoll_label = Label(window, text="Zoll:", font=("bold",15), fg="blue")
zoll_label.grid(row=1, column=0, sticky=W)

zoll_value = DoubleVar()

zoll_entry = Entry(window, textvariable=zoll_value)
zoll_entry.grid(row=1, column=1)


ergebnis_label = Label(window, font=("bold", 25), fg="red")
ergebnis_label.grid(row=3, column=0, sticky=W)

berechnungs_button = Button(window, text="Berechnen", command=z2m)
berechnungs_button.grid(row=2, column=0, sticky=W)


#GUI INTERFACE SECOND FUNCTION

width_value = IntVar()
height_value = IntVar()
depth_value = IntVar()


#LABELS

width_label = Label(window, text="Width:", font=("bold",15))
width_label.grid(row=5, column=0, sticky=W)

height_label = Label(window, text="Height:", font=("bold",15))
height_label.grid(row=5, column=1, sticky=W)

depth_label = Label(window, text="Depth:", font=("bold",15))
depth_label.grid(row=5, column=2, sticky=W)

result_label_whd = Label(window, font=("bold", 25), fg="red")
result_label_whd.grid(row=8, column=0, sticky=W)


#TEXTBOXES

width_textbox = Entry(window, textvariable=width_value)
width_textbox.grid(row=6, column=0)

height_textbox = Entry(window, textvariable=height_value)
height_textbox.grid(row=6, column=1)

depth_textbox = Entry(window, textvariable=depth_value)
depth_textbox.grid(row=6, column=2)


#BUTTONS

whd_button = Button(window, text="Berechnen BxHxT", command=whd_calc)
whd_button.grid(row=7, column=0, sticky=W)


#MAINLOOP
window.mainloop()

