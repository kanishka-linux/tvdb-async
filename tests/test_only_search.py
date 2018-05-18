import os
import sys
import time
import unittest
from functools import partial

def search_finished(*args):
    print(args)

class TestTVDB(unittest.TestCase):
        
    def test_only_search(self):
        tv = TVDB(lang='en', wait=0.2)
        tv.search('x', onfinished=search_finished)
        tv.search('aria the animation', onfinished=search_finished)
        tv.search('nichijou', onfinished=search_finished)
    
if __name__ == '__main__':
    BASEDIR, BASEFILE = os.path.split(os.path.abspath(__file__))
    parent_basedir, __ = os.path.split(BASEDIR)
    print(parent_basedir)
    sys.path.insert(0, parent_basedir)
    k_dir = os.path.join(parent_basedir, 'tvdb_async')
    sys.path.insert(0, k_dir)
    print(k_dir)
    from tvdb import TVDB
    unittest.main()
