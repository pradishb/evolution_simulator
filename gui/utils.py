''' Module that contains the the utility functions of gui '''
import tkinter as tk


def set_entry(builder, name, value):
    ''' Sets value of entry component '''
    builder.get_object(name).delete(0, tk.END)
    builder.get_object(name).insert(0, str(value))


def insert_row(builder, name, value):
    ''' Sets value of a single row of treeview component '''
    builder.get_object(name).insert('', 'end', values=value)


def set_cell(builder, name, row, column, value):
    ''' Sets the value of a specific cell of the tree view '''
    item_id = builder.get_object(name).get_children()[row]
    builder.get_object(name).set(item_id, '#{}'.format(column), value)


def set_treeview(builder, name, values):
    ''' Sets value of whole treeview component '''
    for value in values:
        insert_row(builder, name, value)


def clear_treeview(builder, name):
    ''' Clears the values of treeview component '''
    tree = builder.get_object(name)
    tree.delete(*tree.get_children())


def init_checkbox(builder, name, value):
    ''' Initializes a checkbox component using boolean value '''
    builder.get_object(name).state(['!alternate'])
    if value:
        builder.get_object(name).state(['selected'])
    else:
        builder.get_object(name).state(['!selected'])


def set_button_list_state(builder, buttons, state):
    ''' Sets the state of a list of button components '''
    for button in buttons:
        builder.get_object(button)['state'] = state
