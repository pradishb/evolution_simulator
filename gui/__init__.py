''' Main script of the program '''
import logging
import sys
import threading
import tkinter as tk
import pygubu


class Gui:
    ''' Main gui class '''

    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.builder = builder = pygubu.Builder()
        self.builder.add_from_file('main_frame.ui')
        self.mainwindow = builder.get_object('main_frame', master)
        self.builder.connect_callbacks(self)
