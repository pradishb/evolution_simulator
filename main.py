''' Main script of the program '''
import tkinter as tk
import threading
import os

from PIL import Image, ImageTk

from gui import Gui, ContextMenu, ScrollFrame
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
        self.builder.get_object('find_fitness')['state'] = 'disabled'
        self.builder.get_object('sort')['state'] = 'disabled'
        self.builder.get_object('do_selection')['state'] = 'disabled'
        self.builder.get_object('reproduce')['state'] = 'disabled'
        self.builder.get_object('save')['state'] = 'disabled'
        self.creatures = []

        self.scroll_frame = ScrollFrame(self.builder.get_object('creatures_frame'))
        self.scroll_frame.grid(sticky='nsew')

    def create(self):
        ''' Create button callback '''
        threading.Thread(target=self.threaded_create, daemon=True).start()

    def threaded_create(self):
        ''' Creates an initial population of creatures '''
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('create')['state'] = 'disabled'
        for i in range(POPULATION_SIZE):
            creature = Creature(5)
            self.creatures.append(creature)
            image = creature.get_image(5)
            pillow_image = Image.fromarray(image)
            imgtk = ImageTk.PhotoImage(image=pillow_image)

            frame = tk.Frame(self.scroll_frame.view_port)
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

            progress = i * 100 // POPULATION_SIZE
            self.builder.get_object('progress')['value'] = progress
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('find_fitness')['state'] = 'active'

    def test_fitness(self, creature: Creature):
        fitness = framework(Environment, True, creature)
        print(fitness)


def main():
    ''' Main function of the script '''
    root = tk.Tk()
    Application(root)
    root.mainloop()


if __name__ == '__main__':
    create_directories()
    main()
