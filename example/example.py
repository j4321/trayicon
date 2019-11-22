#! /usr/bin/python3
# -*- coding:Utf-8 -*-
"""
trayicon - Multi-GUI-toolkit trayicon package for use with Tkinter
Copyright 2017 Juliette Monsel <j_4321@protonmail.com>
based on code by Michael Lange <klappnase@web.de> copyright 2010

trayicon is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

trayicon is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Example
"""

import trayicon
import os
import tkinter as tk

icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')


def make_icon(gui):

    def cmd1():
        print('Item 1')

    def cmd2():
        print('Item 2: %s' % icon.menu.get_item_value('Item 2'))

    def cmd3():
        print('Q1: %s' % icon.menu.get_group_value('Q1'))

    def cmd4():
        print('Q2: %s' % icon.menu.get_group_value('Q2'))

    if gui == 'qt':
        module = trayicon.qticon
    elif gui == 'gtk':
        module = trayicon.gtkicon
    else:
        module = trayicon.tkicon

    icon = module.TrayIcon('icon.png', fallback_icon_path=icon_path)

    # command
    icon.menu.add_command(label='Item 1', command=cmd1, image=icon_path)
    # checkbutton
    icon.menu.add_checkbutton(label='Item 2', command=cmd2)
    # submenu
    submenu = module.SubMenu(parent=icon.menu)
    submenu.add_command('Subitem 1')
    submenu.add_command('Subitem 2')
    icon.menu.add_cascade(label='Submenu', menu=submenu)
    # separator
    icon.menu.add_separator()
    # radiobuttons
    icon.menu.add_radiobutton(label="Q1: a", command=cmd3, value="a", group="Q1")
    icon.menu.add_radiobutton(label="Q1: b", command=cmd3, value="b", group="Q1")
    icon.menu.add_radiobutton(label="Q2: a", command=cmd4, value="a", group="Q2")
    icon.menu.add_radiobutton(label="Q2: b", command=cmd4, value="b", group="Q2")

    # separator
    icon.menu.add_separator()
    icon.menu.add_command(label='Quit', command=root.destroy)

    # start icon event loop
    icon.loop(root)


toolkits = trayicon.get_available_gui_toolkits()

root = tk.Tk()

for gui in toolkits:
    if toolkits[gui]:
        tk.Button(root, text=gui, command=lambda g=gui: make_icon(g)).pack()

root.mainloop()
