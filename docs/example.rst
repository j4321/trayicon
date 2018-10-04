Example
=======

You will need to have an image named ``icon.png`` in the same folder as
the code below. You can use `this one <https://raw.githubusercontent.com/j4321/trayicon/master/example/icon.png>`_ for instance.

.. code:: python

    import trayicon
    import os
    import tkinter as tk

    icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')


    def make_icon(gui):

        def cmd1():
            print('Item 1')

        def cmd2():
            print('Item 2: %s' % icon.menu.get_item_value('Item 2'))

        if gui == 'qt':
            module = trayicon.qticon
        elif gui == 'gtk':
            module = trayicon.gtkicon
        else:
            module = trayicon.tkicon

        icon = module.TrayIcon('icon.png', fallback_icon_path=icon_path)

        # command
        icon.menu.add_command(label='Item 1', command=cmd1)
        # checkbutton
        icon.menu.add_checkbutton(label='Item 2', command=cmd2)
        # submenu
        submenu = module.SubMenu(parent=icon.menu)
        submenu.add_command('Subitem 1')
        submenu.add_command('Subitem 2')

        icon.menu.add_cascade(label='Submenu', menu=submenu)
        # separator
        icon.menu.add_separator()

        icon.menu.add_command(label='Quit', command=root.destroy)

        # start icon event loop
        icon.loop(root)


    toolkits = trayicon.get_available_gui_toolkits()

    root = tk.Tk()

    for gui in toolkits:
        tk.Button(root, text=gui, command=lambda g=gui: make_icon(g)).pack()

    root.mainloop()
