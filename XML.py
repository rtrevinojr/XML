
import xml.etree.ElementTree as ET


# q: parameter object & self
class XML(object) :



    def __init__(self, xmlfile) :
        """

        :param xmlfile:
        """
        self.add_root(xmlfile, 'mainRunXML.in')
        self.maintree = ET.parse('mainRunXML.in')
        self.mainroot = self.maintree.getroot()
        self.root_lst = self.mainroot.getchildren()
        self.etree = ET.parse('mainRunXML.in')
        self.etree_list = []

        #self.qtree = qt

    def is_nested_it(self, etree, qtree) :

        eroot = etree.getroot()
        qroot = qtree.getroot()

        etreeit = etree.iter()
        qtreeit = qtree.iter()

        qtit = qtreeit.next()
        nest = True

        try :
            for i in etreeit :

                if i.tag == qtit.tag :
                    qtit = qtreeit.next()
        except StopIteration :
            return True
        else :
            return False



    def xml_search(self, etrees, qtrees) :
        #assert type(et) is types.ET

        count = 0
        linecnt = 0
        line = []
        #qt = qtrees.iter()

        try :
            for i in etrees.iter() :
                linecnt += 1
                qt = qtrees.iter()
                if qtrees.getroot().tag == i.tag :
                    etrees._setroot(i)
                    iq = qt.next()
                    qtrees._setroot(iq)
                    if self.is_nested_it(etrees, qtrees) :
                        count += 1
                        line += [linecnt]
        except StopIteration :
            pass

        result = []
        result.append(count)
        result.append(line)
        return result

    def add_root(self, rfile, wfile) :
        assert type(rfile) is str
        assert type(wfile) is str
        r = open(rfile, 'r')
        assert type(r) is file
        xml_file = r.read()
        r.close()
        w = open(wfile, 'w')
        assert type(w) is file
        w.write("<ROOT> " + "\n" )
        w.write(xml_file)
        #w.write( "\n" )
        w.write( "</ROOT>")
        w.close()


    def parse_trees(root_xml) :
        assert type(root_xml) is str
        maintree = ET.parse(root_xml)
        main_root = maintree.getroot()
        docs = main_root.getchildren()
        return docs


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


def xml_search_2(etrees, qtrees) :
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
                nest_cnt = is_nested_it_2(etrees, qtrees)
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
