''' Main script of the program '''
import tkinter as tk
import os

from PIL import Image, ImageTk

from gui import Gui, ContextMenu
from environment import Environment
from framework.framework import main as framework
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

            frame = tk.Frame(self.builder.get_object('creatures'))
            frame.grid(row=i//COL_COUNT, column=i % COL_COUNT)
            panel = tk.Label(frame)
            description = tk.Label(
                frame,
                text=f'Creature #{creature.identity} \n'
                f'Fitness: {creature.fitness}\n'
                f'Species: V{len(creature.vertices)}',
                font=(None, 7))
            right_click = ContextMenu(self.master, [
                {'label': 'Test fitness', 'command': lambda c=creature: self.test_fitness(c)},
                {'label': 'Test reproduce', 'command': self.test_fitness}])
            panel.bind('<Button-3>', right_click.popup)
            description.grid(sticky='w')
            panel.grid()
            panel.imgtk = imgtk
            panel.config(image=imgtk)

    def test_fitness(self, creature: Creature):
        fitness = framework(Environment, creature)
        print(fitness)


def main():
    ''' Main function of the script '''
    root = tk.Tk()
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
