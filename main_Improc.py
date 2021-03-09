#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 10:34:46 2021

@author: molierenguile-makao
"""
# import the package and names 

import argparse
import Impreproc 

# build the arguments 

parser = argparse.ArgumentParser(description='argments of the function modifies the file names')
parser.add_argument('newfileName',help='the new file name')
parser.add_argument('path_repo1',help='the path where the files are located')
parser.add_argument('ext1',help = 'the file extension with the point')
parser.add_argument('unity_number',help = 'number of the unities for the indexation',type=int)
parser.add_argument('-stn','--start_num',type=int,help='the index number to start',default=0)
parser.add_argument('-ph','--path_repo',help='the second path where the files are located',default=None)
parser.add_argument('-e','--ext',help = 'the extension of the file of the second repo',default='.xml')

args = parser.parse_args()

if args.path_repo is None:
    Impreproc.modifyName(args.newfileName,args.path_repo1,args.ext1,args.unity_number,start_num=args.start_num)
else:
    Impreproc.modifyName(args.newfileName,args.path_repo1,args.ext1,args.unity_number,start_num=args.start_num,
                         path_repo2=args.path_repo,ext2=args.ext)
    




    

