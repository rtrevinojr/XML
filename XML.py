
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



#
# is_nested_it function: Returns count for qtree nesting occurances
#
def is_nested_it(etree, qtree) :

    etreeit = etree.iter()
    qtreeit = qtree.iter()

    qtit = qtreeit.next()
    nest = True
    nest_cnt = 0

    try :
        for i in etreeit :
            if i.tag == qtit.tag :
                qtit = qtreeit.next()
                nest_cnt += 1
                print "nest_cnt - ", nest_cnt
    except StopIteration :
        return True
    else :
        return False

def is_nested_it_2(etree, qtree) :

    temp_etree = ET.parse('file3')
    temp_qt = ET.parse('query.in')

    etreeit = etree.iter()
    qtreeit = qtree.iter()

    next_qtreeit = qtreeit.next()
    nest_cnt = 0

    try :
        for i in etreeit :

            if i.tag == next_qtreeit.tag :

                #next_qtreeit = qtreeit.next()
                temp_etree._setroot(i)
                temp_etreeit = temp_etree.iter()

                temp_qtit = temp_qt.iter()
                next_temp_qtit = temp_qtit.next()

                for i2 in temp_etreeit :

                    try :
                        if i2.tag == next_temp_qtit.tag :
                            next_temp_qtit = temp_qtit.next()
                    except StopIteration :
                        nest_cnt += 1
                        temp_qtit = temp_qt.iter()
                        next_temp_qtit = temp_qtit.next()
                        next_temp_qtit = temp_qtit.next()

    except StopIteration :
        return nest_cnt

    return nest_cnt



def xml_search(etrees, qtrees) :
    #assert type(et) is types.ET
    count = 0
    linecnt = 0
    line = []

    try :
        for i in etrees.iter() :
            linecnt += 1
            qt = qtrees.iter()
            if qtrees.getroot().tag == i.tag :
                etrees._setroot(i)
                iq = qt.next()
                qtrees._setroot(iq)
                if is_nested_it(etrees, qtrees) :
                    count += 1
                    line += [linecnt]
    except StopIteration :
        pass

    result = []
    result.append(count)
    result.append(line)
    return result
