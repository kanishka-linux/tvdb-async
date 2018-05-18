import os
import sys
import time
import unittest
from functools import partial

def process_series(tv, *args):
    obj = args[0]
    val = args[1]
    if val == 'episode-info':
        print('>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(len(obj.episode_summary), obj.total)
        print(obj.title)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>')
    elif val == 'season-info':
        print(obj.season_episode_dict)
    elif val == 'info':
        print(obj.summary)
        for i, j in obj.info.items():
            print(i, j)
    elif val in ['poster', 'fanart', 'banners']:
        e = eval('obj.{}'.format(val))
        print(e)
    elif isinstance(val, list):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(len(obj.episode_summary), obj.total)
        print(obj.title)
        print(val)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>')
        
    print('total={};done={};remaining={}'.format(tv.vnt.tasks_count(), tv.vnt.tasks_done(), tv.vnt.tasks_remaining()))
    print(time.time() - tv.time)


class TestTVDB(unittest.TestCase):
    
    def test_search_and_grab(self):
        tv = TVDB(lang='en', wait=0.2, search_and_grab=True)
        tv.search('x', onfinished=partial(process_series, tv))
        tv.search('aria the animation', onfinished=partial(process_series, tv))
        tv.search('nichijou', onfinished=partial(process_series, tv))
        tv.search('legend of the galactic heroes', onfinished=partial(process_series, tv))
        
    
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
