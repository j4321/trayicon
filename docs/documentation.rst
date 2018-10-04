Documentation
=============

Package structure
-----------------

::

    trayicon
    ├── get_available_gui_toolkits (function)
    ├── gtkicon (module)
    │   ├── SubMenu (class)
    │   └── TrayIcon (class)
    ├── qticon (module)
    │   ├── SubMenu (class)
    │   └── TrayIcon (class)
    └── tkicon (module)
        ├── SubMenu (class)
        └── TrayIcon (class)

The ``SubMenu`` and ``TrayIcon`` classes of all three modules have in common the methods documented below.
The aim of this module is to enable a simple switching between toolkits, for instance to allow the end-users
to choose the toolkit best suited to their desktop environment.

get_available_gui_toolkits
--------------------------

.. autofunction:: trayicon.get_available_gui_toolkits()

SubMenu
-------
.. note::

    The methods' argument named ``item`` refers to either an integer indicating
    the position of the item in the menu (starting from 0) or the label (str)
    of the item. 

    .. warning::

        If the ``SubMenu`` contains several items with the same label,
        the methods will act on the first item with given label.

.. class:: SubMenu(parent=None)
    
    Menu or submenu for the system tray icon TrayIcon.
    
    .. method:: __init__(parent=None)
    
        parent : 
            parent widget

    .. method:: add_cascade(label="", menu=None)
    
        Add a submenu to the menu.
        
        label : str
            submenu's label
        
        menu : SubMenu
            submenu to add in the menu
        
    .. method:: add_checkbutton(label="", command=None)
    
        Add a checkbutton item with given label and associated to given command to the menu.
        
        label : str
            checkbutton's label
        
        command : function
            function executed when the checkbutton is clicked upon
        
        The checkbutton state can be obtained/changed using the ``get_item_value``/``set_item_value`` methods.
        
    .. method:: add_command(label="", command=None)
        
        Add an item with given label and associated to given command to the menu.
        
        label : str
            command's label
        
        command : function
            function executed when the checkbutton is clicked upon
    
    .. method:: add_separator()
    
        Add a separator to the menu.
        
    .. method:: delete(item1, item2=None)
        
        Delete all items between item1 and item2 (included).
        
        item1 : int or str
            first item's index or label
            
        item2 : int, str or None
            second item's index or label, ``"end"`` or ``None``. 
            If item2 is None, delete only the item corresponding to item1. 
            If item2 is "end" delete all items after item1 (included).
            
    
    .. method:: index(item)
    
        Return the index of item.
        
        item : int or str 
            item's index or label    
            
    .. method:: get_item_label(item)
        
        Return item's label.
        
        item : int or str 
            item's index or label    
    
    .. method:: set_item_label(item, label)
    
        Set the item's label to given label.
        
        item : int or str 
            item's index or label   
            
        label : str
            item's new label
    
    .. method:: get_item_menu(item)
        
        Return item's menu. It is assumed that the item is a cascade.
        
        item : int or str 
            item's index or label    
    
    .. method:: set_item_menu(item, menu)
        
        Set item's menu to given menu (SubMenu instance). It is assumed that the item is a cascade.
        
        item : int or str 
            item's index or label   
            
        menu : SubMenu
            item's new menu
    
    .. method:: get_item_value(item)
    
        Return item's value (True/False) if item is a checkbutton.
        
        item : int or str 
            item's index or label    
    
    .. method:: set_item_value(item, value)
    
        Set item's value if item is a checkbutton.
        
        item : int or str 
            item's index or label    
            
        value : bool
            item's new value
    
    .. method:: disable_item(item)
    
        Put item in disabled (unresponsive) state.
        
        item : int or str 
            item's index or label    
    
    .. method:: enable_item(item)
    
        Put item in normal (responsive) state.
        
        item : int or str 
            item's index or label    
    
TrayIcon
--------

.. warning::

    - The way the icon is displayed and integrated in the desktop
      environment varies depending on both the toolkit and the toolkit used by
      the desktop environment. Therefore, the same image might have a different 
      rendering in the system tray depending on the toolkit (e.g. resizing issues).

    - Click bindings might have different behavior depending on the GUI toolkit.
      For instance, click bindings do not work at all with the Gtk toolkit if
      AppIndicator3 is used.

.. class:: TrayIcon(icon, fallback_icon_path)

    System tray icon.
    
    .. method:: __init__(icon, fallback_icon_path)
    
        icon : str
            icon path or name (the Gtk and Qt system tray icons can fetch the icon from the current theme)
            
        fallback_icon_path : str
            path to image to use as icon if the first one fails (useful if the current theme does not have the desired icon for instance)
            
    .. method:: bind_left_click(command)
        
        Bind command to left click on the icon.
        
        command : function
            function executed on left click on the icon
    
    .. method:: bind_middle_click(command)
        
        Bind command to middle click on the icon.
        
        command : function
            function executed on middle click on the icon
    
    .. method:: bind_double_click(command)
        
        Bind command to double left click on the icon.
        
        command : function
            function executed on double left click on the icon
    
    .. method:: change_icon(icon, desc='')
    
        Change system tray icon.
        
        icon : str
            new icon path
            
        desc : str
            icon description, useful only for Gtk toolkit
            
    .. method:: loop(tk_window)
        
        Peridodically update the system tray icon inside tkinter mainloop.
        
        tk_window : Tk instance
            main GUI window
        
        
            
    
    

