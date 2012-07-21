#!/usr/bin/env python
import xml.etree.cElementTree as ET
import xml.etree.ElementTree
from xml.etree.cElementTree import tostring
import sys
import os

def clearscreen(numlines=100):
	if os.name == "posix":
	# Unix/Linux/MacOS/BSD/etc
		os.system('clear')
	elif os.name in ("nt", "dos", "ce"):
	# DOS/Windows
		os.system('CLS')
	else:
	# Fallback for other operating systems.
		print '\n' * numlines

sat_key = 0
tp_key = 0

if os.path.exists('satellites.xml'):
	tree = ET.ElementTree(file='satellites.xml')
	root = tree.getroot()
	root.set('progdb_version', '1.0.0')
	root.set('tuner_num', '1')

	for sat in root.getiterator("sat"):
		if (sat_key < 64):
			longitude = sat.get("position")
			sat.set("longitude", longitude)
			name = sat.get("name")
			sat.set("longitude", longitude)
			sat.set("tuner_type_idex", "1")
			sat.set("diseqc1.0", "OFF")
			sat.set("diseqc1.1", "OFF")
			sat.set("power", '13/18')
			sat.set("motor", "OFF")
			sat.set("UserFreq", "5150")
			sat.set("sat_type", "S2")
			sat.set("v12", "ON")
			sat.set("k22", "AUTO")
			sat.set("lnb", "Uni.(9750/10600)")
			name = name[:-8]
			sat.set("name", name)
			del sat.attrib['flags']
			del sat.attrib['position']
			sat_key = sat_key + 1
			sat.set("sat_key", str(sat_key))
			this_sat_key = sat.get("sat_key")
			for transponder in sat.getiterator("transponder"):
				tp_key = tp_key + 1
				transponder.set("tp_key", str(tp_key))
				modulation = transponder.get("modulation")
				if (modulation == "1"):
					transponder.set("modulation_mode", "QPSK")
				if (modulation == "2"):
					transponder.set("modulation_mode", "8PSK")
				del transponder.attrib['modulation']
				frequency = transponder.get("frequency")
				frequency = frequency[:-3]
				transponder.set("frequency", frequency)

				symbol_rate = transponder.get("symbol_rate")
				symbol_rate = symbol_rate[:-3]
				transponder.set("symbol_rate", symbol_rate)

				polarization = transponder.get("polarization")
				if (polarization == "0"):
					transponder.set("polarization", "H")
				if (polarization == "1"):
					transponder.set("polarization", "V")

				fec = transponder.get("fec_inner")
				if (fec == "0"):
					transponder.set("fec", "AUTO")
				if (fec == "1"):
					transponder.set("fec", "1/2")
				if (fec == "2"):
					transponder.set("fec", "2/3")
				if (fec == "3"):
					transponder.set("fec", "3/4")
				if (fec == "4"):
					transponder.set("fec", "4/5")
				if (fec == "5"):
					transponder.set("fec", "5/6")
				if (fec == "6"):
					transponder.set("fec", "6/7")
				if (fec == "7"):
					transponder.set("fec", "7/8")
				if (fec == "8"):
					transponder.set("fec", "8/9")
				if (fec == "9"):
					transponder.set("fec", "AUTO")
				del transponder.attrib['fec_inner']
				transponder.set("transport_stream_id", "0")
				transponder.set("original_network_id", "0")
				del transponder.attrib['system']
				transponder.set("sat_key", this_sat_key)
		else:
			for sat in root:
				if sat.attrib.has_key('flags'):
					root.remove(sat)

	for sat in root:
		if sat.attrib.has_key('flags'):
			root.remove(sat)
	for sat in root:
		if sat.attrib.has_key('flags'):
			root.remove(sat)		
	for sat in root:
		if sat.attrib.has_key('flags'):
			root.remove(sat)		
	for sat in root:
		if sat.attrib.has_key('flags'):
			root.remove(sat)		
	for sat in root:
		if sat.attrib.has_key('flags'):
			root.remove(sat)		
			
	if not os.path.exists("to_import"):
		os.makedirs("to_import")

	xmlString = tostring(tree.getroot())
	xmlString = '<?xml version="1.0"?>\n%s' % xmlString

	with open("to_import/sat.xml", "w") as outFile:
		outFile.write(xmlString)
		
	with open("to_import/tv_prog.xml", "w") as tv_prog:
		tv_prog.write('<?xml version="1.0"?><programs progdb_version="1.0.0"></programs>')

	with open("to_import/tv_fav.xml", "w") as tv_fav:
		tv_fav.write('<?xml version="1.0"?><favourites progdb_version="1.0.0"></favourites>')

	with open("to_import/radio_prog.xml", "w") as radio_prog:
		radio_prog.write('<?xml version="1.0"?><programs progdb_version="1.0.0"></programs>')

	with open("to_import/radio_fav.xml", "w") as radio_fav:
		radio_fav.write('<?xml version="1.0"?><favourites progdb_version="1.0.0"></favourites>')

	clearscreen()
	raw_input("ALWAYS BACKUP/EXPORT YOUR EXISTING SATELLITES/FAVOURITES BEFORE USING THIS\nAPPLICATION! THE GENERATED FILES FROM IT WILL REPLACE/DELETE YOUR PROGRAMS &\nFAVOURITES WHEN IMPORTED TO YOUR RECEIVER SINCE THIS IS NEEDED IN ORDER\nEVERYTHING TO START WORKING AFTER THE IMPORT!\n\n\t\tsatellites.xml converted successfuly! \n\n\nNow put the \"to_import\" directory I just created/updated in the current\n\ndirectory onto a usb flash drive and plug it in your receiver from where\n\nyou can import the NEW satellites from the usb.\n\n\t\t\t\t********\n\nWARNING: If your satellites.xml input file contains more than 64 satellites you'll get only the first 64 converted and the rest will be cut off! This limitation is needed because Spark Linux receivers can list channels by satellite correctly only if you have 64 or less satellites in the list.\n\n\t\tPress [ENTER] to close this window...")
	print "\t\t\t\tGoodBye!\n\n"

else:
	print "\n\n\tWelcome to \"satellites.xml to sat.xml\" converter by linkrage!\n\n\n\tThis application converts satellites.xml files downloaded from\n\n\thttp://www.satellites-xml.eu/ website to Spark Linux compatible format!\n\n\n\nERROR: satellites.xml NOT found in the current directory!\n\n\nPlease put such file here and try again by simply re-running this application ;)"
	raw_input("\n\n\t\tPress [ENTER] to close this window...")