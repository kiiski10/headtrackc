import sys
import helpers

import sighandler
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
	def gtk_main_quit(*args):
		global serial
		print("ByeBye!")
		if "serial" in globals():
			if hasattr(serial, "close"):
				serial.close()
		run = False
		sys.exit()

	def xp_clicked(*args):
		sb = helpers.builder.get_object("spinbutton1")
		mod = sb.get_value()
		try:
			c = 1
			while c <= mod:
				c += 1
				serial.write("X")
		except Exception, e:
			print "XP CLICKED ERROR"
			print e

	def xm_clicked(*args):
		sb = helpers.builder.get_object("spinbutton1")
		mod = sb.get_value()
		try:
			c = 1
			while c <= mod:
				c += 1
				serial.write("x")
		except Exception, e:
			print "XM CLICKED ERROR"
			print e

	def ym_clicked(*args):
		sb = helpers.builder.get_object("spinbutton1")
		mod = sb.get_value()
		try:
			c = 1
			while c <= mod:
				c += 1
				serial.write("y")
		except Exception, e:
			print "YM CLICKED ERROR"
			print e

	def yp_clicked(*args):
		sb = helpers.builder.get_object("spinbutton1")
		mod = sb.get_value()
		try:
			c = 1
			while c <= mod:
				c += 1
				serial.write("Y")
		except Exception, e:
			print "YP CLICKED ERROR"
			print e

	def sm_clicked(*args):
		sb = helpers.builder.get_object("spinbutton1")
		mod = sb.get_value()
		try:
			c = 1
			while c <= mod:
				c += 1
				serial.write("m")
		except Exception, e:
			print "SP CLICKED ERROR"
			print e

	def sp_clicked(*args):
		sb = helpers.builder.get_object("spinbutton1")
		mod = sb.get_value()
		try:
			c = 1
			while c <= mod:
				c += 1
				serial.write("M")
		except Exception, e:
			print "SM CLICKED ERROR"
			print e

	def port_selected(*args):
		global port
		ch = helpers.builder.get_object("checkbutton1")
		ch.set_sensitive(True)
		port = str(args[1].get_active_text())

	def serialToggle(*args):
		global serial, port
		ch = helpers.builder.get_object("checkbutton1")
		active = ch.get_active()

		if not active:									# Connection NOT alive
			ch.set_active(False)
			if "serial" in globals():
				if hasattr(serial, "close"):
					try:
						serial.close()
					except AttributeError, e:
						print "SERIAL CLOSE ERROR: \n", e
			c = 0
			while c < 6:
				c += 1
				name = "button" + str(c)
				btn = helpers.builder.get_object(name)
				btn.set_sensitive(False)

			ch = helpers.builder.get_object("checkbutton1")
			state = ch.set_sensitive(False)

		else:												# Connection alive
			serial = helpers.serialConnect(port)
			if hasattr(serial, "isOpen"):
				if serial.isOpen():
					c = 0
					while c < 6:
						c += 1
						name = "button" + str(c)
						btn = helpers.builder.get_object(name)
						btn.set_sensitive(True)
					ct = helpers.builder.get_object("comboboxtext1")
					ct.set_sensitive(False)
			try:
				ct = helpers.builder.get_object("checkbox1")
				if hasattr(ct, "set_sensitive"):
					ct.set_sensitive(False)
			except Exception, e:
				print "TOGGLE ERROR", e
