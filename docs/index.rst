.. trayicon documentation master file, created by
   sphinx-quickstart on Thu Oct  4 15:06:40 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

trayicon
========

|Linux| |License|


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


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   documentation
   example
   genindex

.. |Linux| image:: https://img.shields.io/badge/platform-Linux-blue.svg
    :alt: Platform
.. |License| image:: https://img.shields.io/github/license/j4321/trayicon.svg
    :target: https://www.gnu.org/licenses/gpl-3.0.en.html
    :alt: License
