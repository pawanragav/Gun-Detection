# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 23:42:23 2023

@author: harib
"""

import threading
if __name__ =="__main__":
   
    t1 = threading.Thread(target = lk, args=())
    t2 = threading.Thread(target = msg, args=())
 
    t1.start()
   
    t2.start()
 
    t1.join()
 
    t2.join()
 
    print("Done!")