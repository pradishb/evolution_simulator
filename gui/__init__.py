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


class ScrollFrame(tk.Frame):
    ''' Wrapper around frame and adds scrollbar '''

    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, borderwidth=0)
        self.view_port = tk.Frame(self.canvas)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas_window = self.canvas.create_window(
            (4, 4), window=self.view_port, anchor="nw", tags="self.view_port")

        self.view_port.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.on_frame_configure(None)

    def on_frame_configure(self, *_):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width=canvas_width)


class Gui:
    ''' Main gui class '''

    def __init__(self, master, title):
        self.master = master
        self.master.title(title)
        self.builder = builder = pygubu.Builder()
        self.builder.add_from_file('main_frame.ui')
        self.mainwindow = builder.get_object('main_frame', master)
        self.builder.connect_callbacks(self)
