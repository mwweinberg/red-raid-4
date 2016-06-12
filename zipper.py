fout=open('pd-all-2009-2015.csv', 'a')


def zipper(input):
    for line in open(input):
        fout.write(line)

zipper('rrs4_output-2009-01-01.csv')
zipper('rrs4_output-2009-07-01.csv')
zipper('rrs4_output-2010-01-01.csv')
zipper('rrs4_output-2010-07-01.csv')
zipper('rrs4_output-2011-01-01.csv')
zipper('rrs4_output-2011-07-01.csv')
zipper('rrs4_output-2012-01-01.csv')
zipper('rrs4_output-2012-07-01.csv')
zipper('rrs4_output-2013-01-01.csv')
zipper('rrs4_output-2013-07-01.csv')
zipper('rrs4_output-2014-01-01.csv')
zipper('rrs4_output-2014-07-01.csv')
zipper('rrs4_output-2015-01-01.csv')
zipper('rrs4_output-2015-07-01.csv')


fout.close()
