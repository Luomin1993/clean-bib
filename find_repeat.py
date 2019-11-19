#!/usr/bin/python
# -*-coding:utf-8-*-

import os;
import re;
from collections import Counter;
import sys;


__author__ = 'hanss401';

def not_only_blank(STRING):
    STRING = STRING.replace(' ','');
    if len(STRING)>0:return True;
    return False;

def main():
    # ---------- load data  ----------
    BIB_FILE_NAME = sys.argv[1];
    with open(BIB_FILE_NAME, 'r') as BIB_FILE:
        BIB_LINES = BIB_FILE.read().split('\n');
    # ---------- collect titles -------
    TITLE_NAME_SET = [];
    for LINE in BIB_LINES:
        TITLE_NAME = re.findall(r'(.*?)title(.*?)=(.*?){(.*?)},', LINE);
        #z-h-u ERROR_NAME = re.findall(r'(.*?)title(.*?)},', LINE);
        #z-h-u if ERROR_NAME!=[]:
        #z-h-u     print ERROR_NAME;
        #z-h-u     if len(ERROR_NAME[0][0])>0:
        #z-h-u         continue;
        if TITLE_NAME!=[]:
            if not_only_blank(TITLE_NAME[0][0]): continue; 
            TITLE_NAME = TITLE_NAME[0][-1];
        else:continue;    
        TITLE_NAME_SET.append(TITLE_NAME);
    #z-h-u print TITLE_NAME_SET[0:5]
    # ---------- find repeat ones ------
    STAT_TIMES_DICT = dict(Counter(TITLE_NAME_SET));
    print('Repeat Articles and Times:')
    #z-h-u print({PAPER_NAME:TIMES for PAPER_NAME,TIMES in STAT_TIMES_DICT.items() if TIMES > 1});
    for PAPER_NAME,TIMES in STAT_TIMES_DICT.items():
        if TIMES > 1:
            print PAPER_NAME + ' ---:--- ' + str(TIMES);


if __name__ == '__main__':
    main()