from PIL import Image, ImageTk
import pyscreenshot as ImageGrab
import tkinter
import json
import time
import os
import sys

x, y, w, h = 500, 300, 0, 0
label_var = None
last_person = 'default'

with open('names.json') as json_file:
    names = json.load(json_file)
    g_names = (n for n in names)

def take_pic(current_person):
    # local active window
    str_g = current_person.replace(' ', '_')
    savename = '{0}_certificate.png'.format(str_g)
    path_s = 'certificates/'

    img_s = ImageGrab.grab(bbox=(x, y+35, x+w, y+h+35))
    img_s.save(path_s+savename)

def key(event):
    global last_person, label_var

    if event.keysym == 'F7':
        try:
            current_person = next(g_names)
        except StopIteration:
            current_person = 'DONE'
            print('Finish..!')
        if current_person != 'DONE':
            label_var.set(current_person)
            take_pic(last_person)
            last_person = current_person
        else:
            print('GET OUT!')

def start(filename):
    global w, h, label_var

    p = os.getcwd() + '/image/{0}'.format(filename)
    im = Image.open(p)
    w, h = im.size

    root = tkinter.Tk()
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    tkimage = ImageTk.PhotoImage(im)

    label_var = tkinter.StringVar()
    label_var.set(last_person)

    back_image = tkinter.Label(root, image=tkimage)
    text_name = tkinter.Label(root, textvariable=label_var,
                                font=("Helvetica", 16),
                                compound=tkinter.CENTER)
    text_name.config(bg="white")
    back_image.grid(row=3, column=3)
    text_name.grid(row=3, column=3, pady=(10, 45))

    root.bind_all('<Key>', key)
    root.mainloop()

if __name__ == "__main__":
    if len (sys.argv) > 1:
        start(sys.argv[1])
    else:
        print('ERROR: Insert certificate\'s filename.')
