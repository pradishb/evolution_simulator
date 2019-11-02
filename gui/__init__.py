''' Main script of the program '''
import logging
import sys
import threading
import tkinter as tk
import pygubu


class ContextMenu:
    ''' Wrapper around dropdown context menu '''

    def __init__(self, master, commands):
        self.menu = tk.Menu(master, tearoff=0)

        for command in commands:
            self.menu.add_command(**command)

    def popup(self, event):
        ''' Called when menu popup '''
        self.menu.post(event.x_root, event.y_root)


class Gui:
    ''' Main gui class '''

    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.builder = builder = pygubu.Builder()
        self.builder.add_from_file('main_frame.ui')
        self.mainwindow = builder.get_object('main_frame', master)
        self.builder.connect_callbacks(self)
