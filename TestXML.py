
#!/usr/bin/env python

"""
To test the program:
    % python TestXML.py >& TestXML.py.out
    % chmod ugo+x TestXML.py
    % TestXML.py >& TestXML.py.out
"""

# -------
# imports
# -------

import xml.etree.ElementTree as ET
import StringIO
import unittest

from XML import is_nested, xml_search

#
# TestXML
#

class TestXML(unittest.TestCase) :

	# global constant:
	xml = """
	<THU>
		<Team>
			<ACRush></ACRush>
			<Jelly></Jelly>
			<Cooly></Cooly>
		</Team>
		<JiaJia>
			<Team>
				<Ahyangyi></Ahyangyi>
				<Dragon></Dragon>
				<Cooly><Amber></Amber></Cooly>
			</Team>
		</JiaJia>
	</THU>
	"""
	
	# global query constant
	query = " <Team> <Cooly> </Cooly> </Team> "
	query2 = " <Team> </Team> "
	query3 = " <Team> <Cooly> <Amber> </Amber> </Cooly> </Team> "
	
	
	'''
	# Constructor
	def __init__(self, query, xml) :
		fxml = StringIO.StringIO(xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		qfile = StringIO.StringIO(query)
	'''
	 
	#
	# test_is_nested
	#
	def test_is_nested(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query)
		qtree = ET.parse(fquery)
		result = is_nested(etree, qtree)
		self.assert_(result == True)
		
	def test_is_nested_2(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query2)
		qtree = ET.parse(fquery)
		result = is_nested(etree, qtree)
		self.assert_(result == True)
		
	def test_is_nested_3(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query2)
		qtree = ET.parse(fquery)
		result = is_nested(etree, qtree)
		self.assert_(result == True)
		
	#
	# test_xml_search
	#
	def test_xml_search(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query)
		qtree = ET.parse(fquery)
		result = xml_search(etree, qtree)
		self.assert_(result == [2,[2,7]])
		
	def test_xml_search_2(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query)
		qtree = ET.parse(fquery)
		result = xml_search(etree, qtree)
		self.assert_(result == [2,[2, 7]])
		
	def test_xml_search_3(self) :
		fxml = StringIO.StringIO(self.xml)
		etree = ET.parse(fxml)
		eroot = etree.getroot()
		fquery = StringIO.StringIO(self.query3)
		qtree = ET.parse(fquery)
		result = xml_search(etree, qtree)
		self.assert_(result == [1,[7]])
		
			
		
		


#
# main
#
	print xml

print "TestXML.py"
unittest.main()
print "Done."
	
	
