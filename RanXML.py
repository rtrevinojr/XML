
# generate random xml code

import random
import StringIO


tag_list = [
    "THU",
    "Team",
    "JiaJia",
    "ACRush",
    "Jelly",
    "Cooly",
    "Ahyangi",
    "Dragon",
    "Cooly",
    "Amber",

    "Hector",
    "Rene",
    "Trevino",
    "Jr",
    "Ember",
    "Brandee",
    "Becca",
    "Lexi",
    "Lindsey",
    "Lauren",
    "Catherine",

    "Apple",
    "Orange",
    "Blue",
    "Car",
    "Chevy",
    "Black",
    "Corvette"

]

def randtag_len() :
    length = len(tag_list)
    #print "tag_list length: ", length
    return length

def gen_xml(tagno, qtagno, docno, insert) :

    cnt = 0
    outfile = 'RunXML.in'
    out = open('RunXML.in', 'w')
    nest_prob = 8

    for d_it in docno :
        for t_it in tagno :
            r_index = random.randint(0, randtag_len() - 1)
            r_prob = random.randint(0, 10)

            r_ele = tag_list[r_index]
            #out.write( "<" + r_ele + ">" )

            if r_prob < 2 :

                out.write( "</" + r_ele + ">" )
                if nest_prob > 1 :
                    nest_prob -= 1
            else :
                out.write( "<" + r_ele + ">" + out + "</" + r_ele + ">" )


def xml_test(tagno, qno) :

    nest_prob = 8
    out = open('RunXML.in', 'w')
    t_it = 0
    str = ""
    while t_it < tagno :
        r_index = random.randint(0, randtag_len() - 1)
        r_prob = random.randint(0, 10)
        r_ele = tag_list[r_index]
        if r_prob < 2 :
            tstr = str
            str = tstr +  "\t" + "<" + r_ele + "> </" + r_ele + "> " + "\n" + "\b"

            if nest_prob > 1 :
                nest_prob -= 1
        else :
            tstr = str
            str = " <" + r_ele + ">" + tstr + "</" + r_ele + "> " + "\n"

        t_it += 1

    out.write(str + "\n")

    t_it = 0
    qstr = ""
    while t_it < qno :
        r_index = random.randint(0, randtag_len() - 1)
        r_prob = random.randint(0, 10)

        r_ele = tag_list[r_index]
        #out.write( "<" + r_ele + ">" )

        if r_prob < 2 :
            qtstr = qstr
            qstr = qtstr + "\t" +  " <" + r_ele + "> </" + r_ele + "> "

            if nest_prob > 1 :
                nest_prob -= 1
        else :
            qtstr = qstr
            qstr = "\n" + " <" + r_ele + "> " + "\n" + "\t" + qtstr + "\n" + " </" + r_ele + "> " + "\n"

        t_it += 1

    out.write(qstr)


#randtag_len()

xml_test(15, 5)
