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


Provide the TrayIcon and SubMenu classes using qt (qticon submodule),
gtk (gtkicon submodule) and tktray (tkicon submodule) GUI toolkits.

The classes possess the same methods in all three toolkits and can therefore
be used in the same way regardless of the toolkit. However, tktray does not
handle icon resizing so the icon rendering in the system tray is very toolkit
dependent.
"""

import os
from subprocess import check_output
from trayicon import tkicon, qticon, gtkicon


def get_available_gui_toolkits():
    """
    Check which gui toolkits are available to create a system tray icon.

    Requires tclsh (usually provided by the tcl package).
    """
    toolkits = {'gtk': True, 'qt': True, 'tk': True}
    b = False
    try:
        import gi
        b = True
    except ImportError:
        toolkits['gtk'] = False

    try:
        import PyQt5
        b = True
    except ImportError:
        try:
            import PyQt4
            b = True
        except ImportError:
            try:
                import PySide
                b = True
            except ImportError:
                toolkits['qt'] = False

    tcl_packages = check_output(["tclsh",
                                 os.path.join( os.path.dirname(__file__), "packages.tcl")]).decode().strip().split()
    toolkits['tk'] = "tktray" in tcl_packages
    b = b or toolkits['tk']
    if not b:
        raise ImportError("No GUI toolkits available to create the system tray icon.")
    return toolkits
