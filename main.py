import time
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Function for opening the
# file explorer window
def browseFiles():
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    image=Image.open(filename)

    # creating a copy of original image
    watermark_image = image.copy()

    # Image is converted into editable form using
    # Draw function and assigned to draw
    draw = ImageDraw.Draw(watermark_image)



    # Decide the text location, color and font
    # (255,255,255)-White color text
    draw.text((0, 0), "Ujjwal Patel", (0, 0, 0))
    # to show image
    watermark_image.show()
    watermark_image.save("watermarkimage.png")


windows=Tk()
windows.minsize(500,500)

button=Button(text="choose image file",command=browseFiles)
button.pack()


windows.mainloop()
