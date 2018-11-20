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

The :class:`SubMenu` and :class:`TrayIcon` classes of all three modules have in common the methods documented below.
The aim of this module is to enable a simple switching between toolkits, for instance to allow the end-users
to choose the toolkit best suited to their desktop environment.

get_available_gui_toolkits
--------------------------

.. autofunction:: trayicon.get_available_gui_toolkits()

SubMenu
-------
.. note::

    The methods' argument named :obj:`item` refers to either an integer indicating
    the position of the item in the menu (starting from 0) or the label (str)
    of the item. 

.. warning::

    If the :class:`SubMenu` contains several items with the same label,
    the methods will act on the first item with given label.

.. class:: SubMenu(parent=None)
    
    Menu or submenu for the system tray icon :class:`TrayIcon`.
    
    .. method:: __init__(parent=None)
    
        parent : 
            parent widget

    .. method:: add_cascade(label="", menu=None, image=None)
    
        Add a submenu to the menu.
        
        label : str
            submenu's label
        
        menu : SubMenu
            submenu to add in the menu

        image : str
            path to an image to display on the left of the submenu's label
        
    .. method:: add_checkbutton(label="", command=None)
    
        Add a checkbutton item with given label and associated to given command to the menu.
        
        label : str
            checkbutton's label
        
        command : function
            function executed when the checkbutton is clicked upon
        
        The checkbutton state can be obtained/changed using :meth:`get_item_value`/:meth:`set_item_value`.
        
    .. method:: add_command(label="", command=None, image=None)
        
        Add an item with given label and associated to given command to the menu.
        
        label : str
            command's label

        command : function
            function executed when the checkbutton is clicked upon

        image : str
            path to an image to display on the left of the submenu's label
            
    .. method:: add_radiobutton(self, label="", command=None, value=None, group=None)
        
        Add a radiobutton item with given label and associated to given command to the menu.
        
        label : str
            command's label

        command : function
            function executed when the checkbutton is clicked upon

        group : str
            name of the group in which this radiobutton will be put.
            All radiobuttons in a group are mutually exclusive.
            
        value : str
            value associated to the group when this radiobutton is selected.
            Each radiobutton in the group should have a unique value.
            The current value of the group can be obtained/changed using
            :meth:`get_group_value`/:meth:`set_group_value`.  The
            value of the item can be obtained/changed using
            :meth:`get_item_value`/:meth:`set_item_value`.
    
    .. method:: add_separator()
    
        Add a separator to the menu.
        
    .. method:: delete(item1, item2=None)
        
        Delete all items between item1 and item2 (included).
        
        item1 : int or str
            first item's index or label
            
        item2 : int, str or None
            second item's index or label, :obj:`"end"` or :obj:`None`. 
            If item2 is None, delete only the item corresponding to item1. 
            If item2 is "end" delete all items after item1 (included).
            
    
    .. method:: index(item)
    
        Return the index of item.
        
        item : int or str 
            item's index or label

    .. method:: get_group_value(group)
    
        Return group's current value.
        
        group : str
            group's name

    .. method:: set_group_value(group, value)
    
        Change group's current value, hence the selected radiobutton.

        group : str
            group's name

        value : str
            new value of the group
        

    .. method:: get_item_group(item)

        Return item's group (radiobuttons only).

        item : int or str 
            item's index or label
        
    .. method:: set_item_group(item, group):

        Set item's group (radiobuttons only).
        
        item : int or str 
            item's index or label

        group : str
            group's name

    .. method:: set_item_image(item, image)
    
        Set the item's image to given image.
        
        item : int or str 
            item's index or label   
            
        image : str
            path to the new image
            
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
    
        Return item's value if item is a checkbutton or a radiobutton.
        
        item : int or str 
            item's index or label    
    
    .. method:: set_item_value(item, value)
    
        Set item's value if item is a checkbutton or a radiobutton.
        
        item : int or str 
            item's index or label    
            
        value : bool (checkbutton) or str (radiobutton)
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
        
        
            
    
    

