trayicon
========

|Linux| |License| |Doc|


trayicon is a multi-GUI-toolkit system tray icon package. It is intended 
for use with a tkinter main GUI in Linux. 

The system tray icon integration in desktop environments often depends
on the GUI toolkit used by the desktop environment. 
So this package aims at providing standardized classes enabling switching 
between GUI toolkits depending which one gives the best system tray icon integration.

trayicon provides the ``TrayIcon`` and ``SubMenu`` classes using qt 
(qticon submodule), gtk (gtkicon submodule) and tktray (tkicon submodule) 
GUI toolkits. The classes possess the same methods in all three toolkits 
and can therefore be used in the same way regardless of the toolkit. 
However, tktray does not handle icon resizing so the icon rendering in 
the system tray is very toolkit dependent.


Requirements
------------

- Linux
- Python 3
- tclsh for the ``get_available_gui_toolkits`` function (usually provided by the tcl package)
- the python modules for the GUI toolkits you want to use: Qt, GTK3, `tktray <https://code.google.com/archive/p/tktray/downloads>`_


Documentation
-------------

See the example in the *example/* folder.

Full documentation on https://trayicon.readthedocs.io.

.. |Linux| image:: https://img.shields.io/badge/platform-Linux-blue.svg
    :alt: Platform
.. |License| image:: https://img.shields.io/github/license/j4321/trayicon.svg
    :target: https://www.gnu.org/licenses/gpl-3.0.en.html
    :alt: License
.. |Doc| image:: https://readthedocs.org/projects/trayicon/badge/?version=latest
    :target: https://trayicon.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
