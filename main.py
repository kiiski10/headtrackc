# -*- coding: utf-8 -*-
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import sighandler
import helpers

run = True
port = "none"

sigHandler = sighandler.Handler()
helpers.builder.add_from_file("HTCgui.glade")		 # add the xml file to the Builder
helpers.builder.connect_signals(sigHandler)

window = helpers.builder.get_object("mainWindow")	 # This gets the 'mainWindow' objectwindow = builder.get_object("mainWindow")	 # This gets the 'mainWindow' object

statusbar = helpers.builder.get_object("statusbar1")
status = "© Pekka L. (2017)"
statusbar.push(1, status)
statusbar.set_sensitive(False)

sb = helpers.builder.get_object("spinbutton1")
adj = Gtk.Adjustment(value=1, lower=1, upper=100, step_incr=1, page_incr=10)
sb.set_adjustment(adj)

window.show()
Gtk.main()