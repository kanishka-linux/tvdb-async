import os
import sys
import time
import unittest
from functools import partial

def search_finished(*args):
    if len(args) == 3:
        obj = args[1]
    else:
        obj = args[0]
    print(obj.title)
    print(obj.summary)

class TestTVDB(unittest.TestCase):
        
    def test_backend_search(self):
        tv = TVDB(lang='en', backend='ddg', wait=0.1)
        tv.search('x', onfinished=partial(search_finished, 'x'), backend='no', episode_summary=True)
        tv.search('aria the animation', onfinished=search_finished, backend='no', episode_summary=True)
        tv.search('nichijou', onfinished=search_finished)
        tv.search('legend galactic heroes', onfinished=search_finished, backend='g')
    
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
