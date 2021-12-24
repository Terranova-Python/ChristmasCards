from tkinter import *
import random

# Card generator Text
greeting = ['Happy Holiday\'s', 'Merry Chrysler', 'Happy Chrimus', 'Merry Christmas']
filler = ['You Filthy', 'You Dirty Little', 'You Scrumtious', 'My Precious', 'My Angel', 'You', 'My', 'To You']
final = ['Animal!', 'Monster!', 'Python Programmer ;)', 'TechToker', 'Beast!', 'Nerd!', 'Beautiful Human!']

# Tkinter fames and GUI
root = Tk()
root.title('TerranovaTech\'s Cards!')
root.geometry('310x400+550+150') # width, height, start_x, start_y

# Image Rendering in Tkinter
img1 = PhotoImage(file='pics/img1.png')
img2 = PhotoImage(file='pics/img2.png')
img3 = PhotoImage(file='pics/img3.png')
img4 = PhotoImage(file='pics/img4.png')
imgs = [img1, img2, img3, img4]

def card_generator():
    full_build = random.choice(greeting), random.choice(filler), random.choice(final)
    # Access full build indexes example: fullbuild[0] = the first part

    cts = f'{full_build[0]}\n{full_build[1]}\n{full_build[2]}' # cts = Compile the spaces, makes it look pretty on the card!
    final_label = Label(text=cts, bg='#ffffff', font=('Calibri', 16))
    final_label.pack(pady=150)

# Card background - random choice from list of imgs
background = Label(root, image=random.choice(imgs))
background.place(x=0, y=0, relwidth=1, relheight=1) # these attributs ensure it takes up the entire screen

card_generator() # call our generator function after gui has rendered, not before!
root.mainloop() # loop loop loop loop!