''' Main script of the program '''
import tkinter as tk
import threading
import os
from copy import copy
from random import choices

from PIL import Image, ImageTk

from gui import Gui, ContextMenu, ScrollFrame
from environment import Environment
from framework.framework import main as framework
from reproduction import reproduce
from creature import Creature
from settings import POPULATION_SIZE, SELECTION_SIZE, OFFSPRINGS_PER_SELECTION_SIZE, K_COUNT


def create_directories():
    "Creates necesesary directories"
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("data/vertices"):
        os.makedirs("data/vertices")
    if not os.path.exists("data/edges"):
        os.makedirs("data/edges")


COL_COUNT = 8


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
        for col in range(COL_COUNT):
            self.scroll_frame.view_port.columnconfigure(col, minsize=66)
        for row in range(POPULATION_SIZE//COL_COUNT + 1):
            self.scroll_frame.view_port.rowconfigure(row, minsize=106)

    def create_creature(self, creature, i):
        ''' Creates a single creature '''
        self.creatures.append(creature)
        image = creature.get_image(5)
        pillow_image = Image.fromarray(image)
        imgtk = ImageTk.PhotoImage(image=pillow_image)
        creature.frame.grid(row=i//COL_COUNT, column=i % COL_COUNT)
        creature.set_description()
        right_click = ContextMenu(self.master, [
            {'label': 'Test fitness', 'command': lambda c=creature: self.test_fitness(c)},
            {'label': 'Test reproduce', 'command': self.test_fitness}])
        creature.description.grid(sticky='w')
        panel = tk.Label(creature.frame)
        panel.bind('<Button-3>', right_click.popup)
        panel.grid()
        panel.imgtk = imgtk
        panel.config(image=imgtk)

    def create(self):
        ''' Create button callback '''
        threading.Thread(target=self.threaded_create, daemon=True).start()

    def find_fitness(self):
        ''' Find fitness button callback '''
        threading.Thread(target=self.threaded_find_fitness, daemon=True).start()

    def sort(self):
        ''' Sort button callback '''
        threading.Thread(target=self.threaded_sort, daemon=True).start()

    def do_selection(self):
        ''' Do selection button callback '''
        threading.Thread(target=self.threaded_selection, daemon=True).start()

    def reproduce(self):
        ''' Reproduce button callback '''
        threading.Thread(target=self.threaded_reproduce, daemon=True).start()

    def threaded_create(self):
        ''' Creates an initial population of creatures '''
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('create')['state'] = 'disabled'
        for i in range(POPULATION_SIZE):
            creature = Creature(5, self.scroll_frame.view_port)
            self.create_creature(creature, i)
            progress = i * 100 // POPULATION_SIZE
            self.builder.get_object('progress')['value'] = progress
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('find_fitness')['state'] = 'active'

    def threaded_find_fitness(self):
        ''' Finds the fitness of all the creatures with render off '''
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('find_fitness')['state'] = 'disabled'
        for i, creature in enumerate(self.creatures):
            creature.fitness = framework(Environment, False, creature)
            creature.set_description()
            creature.description.grid(sticky='w')
            progress = i * 100 // POPULATION_SIZE
            self.builder.get_object('progress')['value'] = progress
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('sort')['state'] = 'active'

    def threaded_sort(self):
        ''' Sorts the creatures based on the fitness values '''
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('sort')['state'] = 'disabled'

        # Empty the view port
        for widget in self.scroll_frame.view_port.winfo_children():
            widget.grid_forget()

        self.creatures.sort(key=lambda c: c.fitness, reverse=True)
        for i, creature in enumerate(self.creatures):
            creature.frame.grid(row=i//COL_COUNT, column=i % COL_COUNT)
            progress = i * 100 // POPULATION_SIZE
            self.builder.get_object('progress')['value'] = progress
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('do_selection')['state'] = 'active'

    def threaded_selection(self):
        ''' Selects the creatures based on the fitness values '''
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('do_selection')['state'] = 'disabled'

        selected_population = []
        creatures = copy(self.creatures)
        for _ in range(SELECTION_SIZE):
            selected = max(choices(creatures, k=K_COUNT), key=lambda c: c.fitness)
            selected_population.append(selected)
            creatures.remove(selected)

        for i, creature in enumerate(self.creatures):
            if creature not in selected_population:
                creature.frame.grid_forget()
                self.creatures.remove(creature)
            progress = i * 100 // POPULATION_SIZE
            self.builder.get_object('progress')['value'] = progress
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('reproduce')['state'] = 'active'

    def threaded_reproduce(self):
        ''' Reproduces the creatures '''
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('reproduce')['state'] = 'disabled'

        # Empty the view port
        for widget in self.scroll_frame.view_port.winfo_children():
            widget.grid_forget()

        creatures = copy(self.creatures)
        total_creatures = len(creatures)
        print(total_creatures)
        self.creatures = []
        k = 0
        for i, creature in enumerate(creatures):
            for _ in range(OFFSPRINGS_PER_SELECTION_SIZE):
                offspring = reproduce(creature)
                self.create_creature(offspring, k)
                k += 1
            progress = i * 100 // total_creatures
            self.builder.get_object('progress')['value'] = progress
        self.builder.get_object('progress')['value'] = 0
        self.builder.get_object('find_fitness')['state'] = 'active'

    def test_fitness(self, creature: Creature):
        ''' Tests the fitness of a single creature with render on '''
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
