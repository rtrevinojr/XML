
import xml.etree.ElementTree as ET


def xml_tree() :
	
	etree = ET.parse('RunXML.in')
	root = etree.getroot()
	
	print type(etree)
	# assert type(etree) == xml.etree.ElementTree
	
	print "\n"
	print "root: ", root
	print "root.tag - ", root.tag
	print "root.attrib - ", root.attrib, "\n"
	
	st = "<Team> <Cooly> </Cooly> </Team>"
	qtree = ET.parse('query.in')
	print "qtree: ", qtree, "\n"
	
	ET.dump(qtree)
	
	index = 0
	edict = {}
	
	for v in etree.iter() :
		print v
		index += 1
		edict[index] = v
	
	print "\n"
	print edict

	ET.dump(root)
	
	

xml_tree()	
	
