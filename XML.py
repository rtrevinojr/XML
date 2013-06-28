

import xml.etree.ElementTree as ET
import sys


class XML(object) :


    def __init__(self, xmlfile) :
        """
        XML Constructor: Reads input file and will parse RunXML.in by adding a master root then convert back into an Element Tree.
        """
        #assert type(xmlfile) is str
        self.add_root(xmlfile, 'masterRunXML.in')
        self.maintree = ET.parse('masterRunXML.in')
        self.mainroot = self.maintree.getroot()
        self.root_lst = self.mainroot.getchildren()



    def add_root(self, rfile, wfile) :
        """
        Read rfile and writes to wfile with a master root for parsing
        """

        w = open(wfile, 'w')
        w.write("<ROOT> " + "\n" )
        for v in rfile :
            w.write(v)
        w.write( "</ROOT>")
        w.close()


    def is_nested(self, etree, qtree) :
        """
        Returns a count for the number of times qtree is nested in etree
        """
        temp_etree = etree
        temp_qt = qtree

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


    def xml_search(self, etrees, qtrees) :
        """
        Method will iterate through etrees and return a list with a count and list of occurences where qtrees exist
        """
        #assert type(etrees) is ET
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
                    nest_cnt = self.is_nested(etrees, qtrees)
                    if nest_cnt > 0 :
                        count += nest_cnt
                        while nest_cnt != 0 :
                            line += [linecnt]
                            nest_cnt -= 1
        except StopIteration :
            pass

        result = []
        result.append(count)
        result.append(line)
        return result


def xml_print(w, l) :
    """
    Function will output the result of xml_search the way Sphere desires
    """
    w.write( str(l[0]) + "\n" )
    l = l[1]
    for i in l :
        w.write( str(i) + "\n" )
    w.write("\n")



def xml_run(xmlin, out) :
    """
    Function will use the XML constructor to parse RunXML.in into a list of root nodes and output the results of the program.
    """
    xmlobj = XML(xmlin)
    rlist = xmlobj.root_lst

    etree1 = ET.parse('masterRunXML.in')
    qtree1 = ET.parse('masterRunXML.in')

    xmlout = out

    cnt = 0
    for v in rlist :
        if cnt % 2 == 0 :
           etree1._setroot(v)
        else :
            qtree1._setroot(v)
            ans = xmlobj.xml_search(etree1, qtree1)
            xml_print(xmlout, ans)
            #print "ans - ", ans
        cnt += 1


