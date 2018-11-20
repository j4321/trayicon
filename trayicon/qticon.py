#! /usr/bin/python3
# -*- coding:Utf-8 -*-
"""
trayicon - Multi-GUI-toolkit trayicon package for use with Tkinter
Copyright 2016-2018 Juliette Monsel <j_4321@protonmail.com>

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


System tray icon using Qt.
"""

try:
    from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QActionGroup
    from PyQt5.QtGui import QIcon
except ImportError:
    try:
        from PyQt4.QtGui import QApplication, QSystemTrayIcon, QMenu, QAction, QIcon, QActionGroup

    except ImportError:
        from PySide.QtGui import QApplication, QSystemTrayIcon, QMenu, QAction, QIcon, QActionGroup

import sys


class QRadioAction(QAction):
    def __init__(self, *args, value=None, group=None, command=None, **kwargs):
        kwargs.setdefault('checkable', True)
        QAction.__init__(self, *args, **kwargs)
        self.value = value
        self.group = group
        self.groupname = None if group is None else group.name
        if command is not None:
            self._command = command
        else:
            self._command = lambda: None
        self.triggered.connect(self.command)

    def command(self, *args):
        if self.group is not None:
            self.group.value = self.value
        self._command()


class QRadioActionGroup(QActionGroup):
    def __init__(self, name, *args, **kwargs):
        QActionGroup.__init__(self, *args, **kwargs)
        self.name = name
        self.setExclusive(True)
        self.value = None

    def set_value(self, value):
        for act in self.actions():
            act.setChecked(value == act.value)


class SubMenu(QMenu):
    """
    Menu or submenu for the system tray icon TrayIcon.

    Qt version.
    """
    def __init__(self, *args, label=None, parent=None, **kwargs):
        """Create a SubMenu instance."""
        if label is None:
            QMenu.__init__(self, parent)
        else:
            QMenu.__init__(self, label, parent)
        self._images = []
        self._groups = {}

    def add_command(self, label="", command=None, image=None):
        """Add an item with given label and associated to given command to the menu."""
        action = QAction(label, self)
        if command is not None:
            action.triggered.connect(lambda *args: command())
        if image is not None:
            self._images.append(QIcon(image))
            action.setIcon(self._images[-1])
        self.addAction(action)

    def add_cascade(self, label="", menu=None, image=None):
        """Add a submenu (SubMenu instance) with given label to the menu."""
        if menu is None:
            menu = SubMenu(label, self)
        action = QAction(label, self)
        action.setMenu(menu)
        if image is not None:
            self._images.append(QIcon(image))
            action.setIcon(self._images[-1])
        self.addAction(action)

    def add_checkbutton(self, label="", command=None):
        """
        Add a checkbutton item with given label and associated to given command to the menu.

        The checkbutton state can be obtained/changed using the ``get_item_value``/``set_item_value`` methods.
        """
        action = QAction(label, self, checkable=True)
        if command is not None:
            action.triggered.connect(lambda *args: command())
        self.addAction(action)

    def add_radiobutton(self, label="", command=None, value=None, group=None):
        """
        Add a radiobutton item with given label and associated to given command to the menu.

        The radiobutton is part of given group name so that not two buttons in the
        same group can be simutlaneously selected. It is associated to given value.
        """
        agroup = self._groups.get(group, None)
        if agroup is None and group is not None:
            agroup = QRadioActionGroup(group, self)
            self._groups[group] = agroup
        action = QRadioAction(label, self, value=value, group=agroup, command=command,
                              checkable=True, checked=(value == agroup.value))
        if agroup is not None:
            agroup.addAction(action)
        self.addAction(action)

    def add_separator(self):
        """Add a separator to the menu."""
        self.addSeparator()

    def delete(self, item1, item2=None):
        """
        Delete all items between item1 and item2 (included).

        If item2 is None, delete only the item corresponding to item1.
        """
        if len(self.actions()) == 0:
            return
        index1 = self.index(item1)
        if item2 is None:
            self.removeAction(self.actions()[index1])
        else:
            index2 = self.index(item2)
            a = self.actions()
            for i in range(index1, index2 + 1):
                self.removeAction(a[i])

    def index(self, item):
        """
        Return the index of item.

        item can be an integer corresponding to the entry number in the menu,
        the label of a menu entry or "end". In the fisrt case, the returned index will
        be identical to item.
        """
        if isinstance(item, int):
            if item <= len(self.actions()):
                return item
            else:
                raise ValueError("%r not in menu" % item)
        elif item == "end":
            return len(self.actions())
        else:
            try:
                i = [i.text() for i in self.actions()].index(item)
            except ValueError:
                raise ValueError("%r not in menu" % item)
            return i

    def get_group_value(self, group):
        """Return group's current value."""
        return self._groups[group].value

    def set_group_value(self, group, value):
        """Set group's current value."""
        self._groups[group].value = value

    def get_item_group(self, item):
        """Return item's group."""
        i = self.actions()[self.index(item)]
        try:
            gr = i.group
            return None if gr is None else gr.name
        except AttributeError:
            raise TypeError("Menu entry {item} is not a radiobutton".format(item=item))

    def set_item_group(self, item, group):
        """Set item's group (radiobuttons only)."""
        i = self.actions()[self.index(item)]
        try:
            value = i.value
        except AttributeError:
            raise TypeError("Menu entry {item} is not a radiobutton".format(item=item))
        gr = self._groups.get(group, None)
        if gr is None and group is not None:
            gr = QRadioActionGroup(group, self)
            self._groups[group] = gr
        i.group = gr
        i.set_active((gr is not None) and (gr.value == value))

    def set_item_image(self, item, image):
        i = self.actions()[self.index(item)]
        try:
            self._images.remove(i.icon())
        except ValueError:
            pass
        self._images.append(QIcon(image))
        i.setIcon(self._images[-1])

    def get_item_label(self, item):
        """Return item's label."""
        return self.actions()[self.index(item)].text()

    def set_item_label(self, item, label):
        """Set the item's label to given label."""
        i = self.actions()[self.index(item)]
        i.setText(label)

    def get_item_menu(self, item):
        """
        Return item's menu.

        It is assumed that the item is a cascade.
        """
        i = self.actions()[self.index(item)]
        return i.menu()

    def set_item_menu(self, item, menu):
        """
        Set item's menu to given menu (SubMenu instance).

        It is assumed that the item is a cascade.
        """
        i = self.actions()[self.index(item)]
        i.setMenu(menu)

    def disable_item(self, item):
        """Put item in disabled (unresponsive) state."""
        self.actions()[self.index(item)].setDisabled(True)

    def enable_item(self, item):
        """Put item in normal (responsive) state."""
        self.actions()[self.index(item)].setDisabled(False)

    def get_item_value(self, item):
        """Return item value (True/False) if item is a checkbutton."""
        i = self.actions()[self.index(item)]
        if not i.isCheckable():
            raise TypeError("Menu entry {item} is neither a checkbutton nor a radiobutton".format(item=item))
        try:
            return i.value
        except AttributeError:
            return i.isChecked()

    def set_item_value(self, item, value):
        """Set item value if item is a checkbutton."""
        i = self.actions()[self.index(item)]
        if not i.isCheckable():
            raise TypeError("Menu entry {item} is neither a checkbutton nor a radiobutton".format(item=item))
        try:
            gr = self._groups.get(i.group, None)
            i.value = value
            if gr is not None:
                i.setChecked(value == gr.value)
        except AttributeError:
            i.setChecked(value)


class TrayIcon(QApplication):
    """System tray icon, Qt version."""
    def __init__(self, icon, fallback_icon_path, **kwargs):
        """Create a TrayIcon instance."""
        QApplication.__init__(self, sys.argv)
        self._fallback_icon = QIcon(fallback_icon_path)
        self._icon = QIcon.fromTheme(icon, self._fallback_icon)
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(self._icon)

        self.menu = SubMenu()
        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()

    def loop(self, tk_window):
        """Update Qt GUI inside tkinter mainloop."""
        self.processEvents()
        tk_window.loop_id = tk_window.after(10, self.loop, tk_window)

    def change_icon(self, icon, desc=''):
        """Change icon."""
        del self._icon
        self._icon = QIcon(icon)
        self.tray_icon.setIcon(self._icon)

    def bind_left_click(self, command):
        """Bind command to left click on the icon."""

        def action(reason):
            """Execute command only on left click (not when the menu is displayed)."""
            if reason == QSystemTrayIcon.Trigger:
                command()

        self.tray_icon.activated.connect(action)

    def bind_middle_click(self, command):
        """Bind command to middle click on the icon."""
        def action(reason):
            """Execute command only on middle click (not when the menu is displayed)."""
            if reason == QSystemTrayIcon.MiddleClick:
                command()

        self.tray_icon.activated.connect(action)

    def bind_double_click(self, command):
        """Bind command to double left click on the icon."""
        def action(reason):
            """Execute command only on double click (not when the menu is displayed)."""
            if reason == QSystemTrayIcon.DoubleClick:
                command()

        self.tray_icon.activated.connect(action)
