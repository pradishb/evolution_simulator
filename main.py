''' Main script of the program '''
import tkinter as tk
import os

from PIL import Image, ImageTk

from gui import Gui
from creature import Creature
from settings import POPULATION_SIZE


def create_directories():
    "Creates necesesary directories"
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("data/vertices"):
        os.makedirs("data/vertices")
    if not os.path.exists("data/edges"):
        os.makedirs("data/edges")


COL_COUNT = 10


class Application(Gui):
    ''' Main gui class '''

    def __init__(self, master):
        Gui.__init__(self, master, 'Evolution Simulator')
        create_directories()

        creatures = []

        for i in range(POPULATION_SIZE):
            creatures.append(Creature(5))

        for i, creature in enumerate(creatures):
            image = creature.get_image(5)
            pillow_image = Image.fromarray(image)
            imgtk = ImageTk.PhotoImage(image=pillow_image)

            # Put it in the display window
            panel = tk.Label(self.builder.get_object('creatures'))  # initialize image panel
            panel.grid(row=i//COL_COUNT, column=i % COL_COUNT)
            panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            panel.config(image=imgtk)  # show the image
            # Put it in the display window
            # tk.Label(self.builder.get_object('creatures'), image=imgtk).pack()
            # label1 = tk.Label(self.builder.get_object('creatures'), text=str(creature.edges))


def main():
    ''' Main function of the script '''
    root = tk.Tk()
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
