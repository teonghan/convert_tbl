#!/usr/bin/python3
###########################################################################
# filename      : convert.py
# date written  : 04/11/2014
# written by    : THChew (teonghan@gmail.com)
# description   : conversion format?
# last update   : 
###########################################################################

import sys

if len(sys.argv)!=int(2):
    print ("Usage        : python3 convert.py input_file")
    print ("Example      : python3 convert.py input.tbl")
    print ("")
    sys.exit()

else:
    input_file = str(sys.argv[1])
    out_file = input_file + '.out'

    #----------------------
    # reading all the input
    #----------------------
    f = open(input_file, 'r')
    data = f.readlines()
    f.close()

    indices = []

    #---------------------------------
    # get the index of all the contigs
    #---------------------------------
    for i in range(0, len(data)):
        if '>' in data[i]:
            indices.append(i)

    #------------
    # output file
    #------------
    fout = open(out_file, 'w')

    for i in range(0, len(indices)):

        #--------------------------------
        # getting start and end of contig
        #--------------------------------
        start = indices[i]
        
        if not i == len(indices)-1:
            end = indices[i+1]
        else:
            end = len(data)

        #-------------------------
        # extract the whole contig
        #-------------------------
        contig = data[start:end]
        fout.write(contig[0])
        
        sub_contig_indices = []

        #--------------------------
        # get index of sub contigs?
        #--------------------------
        for j in range(1, len(contig)):
            try:
                int(contig[j].split('\t')[0])
                sub_contig_indices.append(j)
            except:
                pass

        for j in range(0, len(sub_contig_indices)):
            start_s = sub_contig_indices[j]
            
            if not j == len(sub_contig_indices)-1:
                end_s = sub_contig_indices[j+1]
            else:
                end_s = len(contig)

            #-----------------------
            # extract the sub contig
            #-----------------------
            sub_contig = contig[start_s:end_s]

            #--------------
            # prep the gene
            #--------------
            sub_contig_gene = []
            tmp = sub_contig[0].strip().split('\t')[0:2]
            tmp.append('gene\n')
            tmp = '\t'.join(tmp)
            sub_contig_gene.append(tmp)

            for k in sub_contig:
                if 'locus_tag' in k:
                    sub_contig_gene.append(k)

            #------------
            # write stuff
            #------------
            fout.write(''.join(sub_contig_gene))
            fout.write(''.join(sub_contig))

    fout.close()
