#!/usr/bin/python
# -*-coding:utf-8-*-

import os;
import re;
from collections import Counter;
import sys;


__author__ = 'hanss401';

__author__ = 'hanss401';

def not_only_blank(STRING):
    STRING = STRING.replace(' ','');
    if len(STRING)>0:return True;
    return False;

def title_line(LINE):
    TITLE_NAME = re.findall(r'(.*?)title(.*?)=(.*?){(.*?)},', LINE);
    if TITLE_NAME!=[]:
        if not_only_blank(TITLE_NAME[0][0]):return ''; 
        TITLE_NAME = TITLE_NAME[0][-1];
    else:return '';            
    return TITLE_NAME;

def main():
    # ---------- load data  ----------
    BIB_FILE_NAME = sys.argv[1];
    with open(BIB_FILE_NAME, 'r') as BIB_FILE:
        BIB_LINES = BIB_FILE.read().split('\n');
    # ---------- collect titles -------
    TITLE_NAME_SET = [];
    for LINE in BIB_LINES:
        TITLE_NAME = re.findall(r'(.*?)title(.*?)=(.*?){(.*?)},', LINE);
        if TITLE_NAME!=[]:
            if not_only_blank(TITLE_NAME[0][0]): continue; 
            TITLE_NAME = TITLE_NAME[0][-1];
        else:continue;    
        TITLE_NAME_SET.append(TITLE_NAME);
    # ---------- find repeat ones ------
    STAT_TIMES_DICT = dict(Counter(TITLE_NAME_SET));
    #-z-h-u- for PAPER_NAME,TIMES in STAT_TIMES_DICT.items():
    #-z-h-u-     if TIMES > 1:
    #-z-h-u-         print PAPER_NAME + ' ---:--- ' + str(TIMES);
    BIB_FILE_NEW = [];
    for INDEX_OF_LINE in range(len(BIB_LINES)):
        # ----- locate the start of the sec ---------
        if BIB_LINES[INDEX_OF_LINE][0] == '@':
            END_OF_SEC  = 0;
            # --------- file end -------
            if BIB_LINES[INDEX_OF_LINE+1]=='' :break;
            # --------- find end of the sec -------
            while BIB_LINES[INDEX_OF_LINE+END_OF_SEC][0]!='}' :
                END_OF_SEC+=1;
            END_OF_SEC+=1;    
            for INDEX_OF_SEC in range(END_OF_SEC+1):
                TITLE_NAME = title_line(BIB_LINES[INDEX_OF_LINE+INDEX_OF_SEC]);
                if TITLE_NAME!='':
                    # print TITLE_NAME;
                    break;
            # --------- multi-line title -------
            if TITLE_NAME=='' and INDEX_OF_SEC==END_OF_SEC:
                for INDEX_OF_SEC in range(END_OF_SEC+1):
                    TITLE_NAME = re.findall(r'(.*?)title(.*?)=(.*?){(.*?)', LINE);
                    if TITLE_NAME!=[]:
                        if not_only_blank(TITLE_NAME[0][0]):continue; 
                        TITLE_NAME = TITLE_NAME[0][-1];
                if len(TITLE_NAME)>0:           
            	    IS_REPEAT = False;
                    for MANU_FIND_SAME in TITLE_NAME_SET:
                        if TITLE_NAME in MANU_FIND_SAME:            
                            IS_REPEAT = True;
                else:continue;
                # --------- repeat sec! ------------
                if IS_REPEAT:print"catch U!";continue;            
            # if TITLE_NAME=='' and INDEX_OF_SEC==END_OF_SEC:
            #     print('Warning: fix the format of line: '+str(INDEX_OF_LINE+INDEX_OF_SEC));
            #     continue;
            # --------- repeat sec! ------------
            if STAT_TIMES_DICT[TITLE_NAME]>1:
                STAT_TIMES_DICT[TITLE_NAME] -= 1;
                continue;
        # --------- not repeat sec ------------        
        if BIB_LINES[INDEX_OF_LINE][0] == '@' and END_OF_SEC>0:
            for INDEX_OF_SEC in range(INDEX_OF_LINE,INDEX_OF_LINE+END_OF_SEC+1): 
            	# why +2? add the blank line;
                BIB_FILE_NEW.append(BIB_LINES[INDEX_OF_SEC]);
    # --------- make new file ------------        
    NEW_FILE_NAME = sys.argv[-1];
    with open(NEW_FILE_NAME,'a+') as FILE_STREAM:
        for LINE in BIB_FILE_NEW:
            # FILE_STREAM.write(LINE.encode('utf-8'));
            FILE_STREAM.write(LINE);
            FILE_STREAM.write('\n');
    # print NEW_FILE_NAME;
    # print BIB_FILE_NEW[0:10];        

if __name__ == '__main__':
    main()