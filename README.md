This script converts satellites.xml format from many Enigma1 or Enigma2 powered Set-Top-Boxes (like DreamBox and others)
to Spark Linux compatible format (e.g. Edision's Pingulux, Amiko's Alien etc.).
Such file (containing list of satellites) can also be generated on this website http://satellites-xml.eu

I am releasing this code as it is with no warrenty at all under GNU GPLv3 license! You must always make sure you have exported (backed up)
you data (channels lis, favourites etc.) from the STB to a USB mass-storage device BEFORE using this script/APP

A lot of code optimizations are needed but since the script is working for me I am not going spend time on it anymore.
Contributors are always welcome of course :)

USAGE:

Linux / Mac OS X
just download the satellites_xml-2-sat_xml.py file and run the following in the Terminal:
cd /location_where/you_have/saved_the_file/
python satellites_xml-2-sat_xml.py 

Follow the on screen instructions.


WINDOWS:
Install Python2.7 from http://www.python.org/download/windows/
Or wait for me or somebody else to build this as an .EXE App using py2exe Python module...

Contacts:
zdravko.iskrenov__AT__linkrage.net