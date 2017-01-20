# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject
from gi.repository import Gtk

import threading
import serial as ser
import time

builder = Gtk.Builder()						 # create an instance of the Gtk.Builder

def insertText(text):
	tv = builder.get_object("textview1")
	text = text + "\n"
	try:
		buffer = tv.get_buffer()
		position = buffer.get_start_iter()
		buffer.insert(position, text)
	except Exception, e:
		print "TEXT INSERT ERROR:", e

def serialConnect(port):
	global listenerThread
	try:
		run = True
		serial = ser.Serial(port, 115200, timeout=2)
		insertText(str(port) + " connected")
		listenerThread = threading.Thread(target=listener, args=(serial, run, port,))
		listenerThread.start()
		return serial
	except Exception, e:
		insertText(str(e))
		ch = builder.get_object("checkbutton1")
		state = ch.set_active(False)

def listener(serial, run, port):
	if hasattr(serial, "isOpen"):
		while serial.isOpen() and run == True:
			try:
				data = str(serial.readline())
				data = data.strip('\n')
				if data != "":
					#print data
					insertText(data)
					time.sleep(0.1)
			except Exception, e:
				print "listener closed"
				c = 0
				while c < 6:
					c += 1
					name = "button" + str(c)
					btn = builder.get_object(name)
					btn.set_sensitive(False)
				ch = builder.get_object("checkbutton1")
				ch.set_active(False)
'''
def listener(serial, run, port):
	GObject.idle_add(insertText, "Communication started")
	try:
		if hasattr(serial, "isOpen"):
			while serial.isOpen() and run == True:
				try:
					data = str(serial.readline())
					data = data.strip('\n')
					if data != "":
						insertText(data)
						time.sleep(0.05)
				except Exception, e:
					print "LISTENER ERROR:", e
					serial.close()
					c = 0
					while c < 6:
						c += 1
						name = "button" + str(c)
						btn = builder.get_object(name)
						btn.set_sensitive(False)
					ch = builder.get_object("checkbutton1")
					ch.set_active(False)
'''
		GObject.idle_add(insertText, str(port) + " disconnected")
		GObject.idle_add(insertText, "Communication terminated")
		ch = builder.get_object("checkbutton1")
		state = ch.set_sensitive(True)

		ct = builder.get_object("comboboxtext1")
		ct.set_sensitive(True)
	except Exception, e:
		print "LISTENER ERROR: \n", e

