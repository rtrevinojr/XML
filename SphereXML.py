

import xml.etree.ElementTree as ET
import sys


class XML(object) :


    def __init__(self, xmlfile) :

        self.add_root(xmlfile, 'masterRunXML.in')
        self.maintree = ET.parse('masterRunXML.in')
        self.mainroot = self.maintree.getroot()
        self.root_lst = self.mainroot.getchildren()



    def add_root(self, rfile, wfile) :

        w = open(wfile, 'w')
        w.write("<ROOT> " + "\n" )
        for v in rfile :
            w.write(v)
        w.write( "</ROOT>")
        w.close()


    def is_nested(self, etree, qtree) :

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

    w.write( str(l[0]) + "\n" )
    l = l[1]
    for i in l :
        w.write( str(i) + "\n" )
    w.write("\n")



def xml_run(xmlin, out) :

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


xml_run(sys.stdin, sys.stdout)
