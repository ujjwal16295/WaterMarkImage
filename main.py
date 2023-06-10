import time
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

watermark_value=""
def enter_button():
    global watermark_value
    watermark_value=input.get()
    print(watermark_value)
# Function for opening the
# file explorer window
def browseFiles():
    if watermark_value=="":
        messagebox.showerror(title="error",message="please write watermark")
    else:
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        image = Image.open(filename)

        # creating a copy of original image
        watermark_image = image.copy()

        # Image is converted into editable form using
        # Draw function and assigned to draw
        draw = ImageDraw.Draw(watermark_image)

        # Decide the text location, color and font
        # (255,255,255)-White color text
        draw.text((0, 0), watermark_value, (0, 0, 0))
        # to show image
        watermark_image.show()
        watermark_image.save("watermarkimage.png")





windows=Tk()
windows.minsize(500,500)
label_for_info=Label(text="watermark")
input=Entry(width=10)
entrybutton=Button(text="Enter",command=enter_button)
button=Button(text="choose image file",command=browseFiles)
label_for_info.grid(row=0,column=0)
input.grid(row=0,column=1)
entrybutton.grid(row=0,column=2)
button.grid(row=1,column=1)



windows.mainloop()
