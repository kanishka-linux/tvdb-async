# tvdb-async

Async TVDB metadata fetching library

### Installation
        
		$ git clone https://github.com/kanishka-linux/tvdb-async
        
		$ cd tvdb-async
        
		$ python setup.py sdist (or python3 setup.py sdist)
        
		$ cd dist
        
		$ (sudo) pip install pkg_available_in_directory (or pip3 install pkg_available_in_directory) 
        
          where 'pkg_available_in_directory' is the exact name of the package
          
          created in the 'dist' folder
          
        
        OR
        
        
        $ (sudo) pip install git+https://github.com/kanishka-linux/tvdb-async.git
        
        
        Note: use 'sudo' depending on whether you want to install package system-wide or not
        
        Note: use pip or pip3 depending on what is available on your system
			
### Uninstall
		
		$ (sudo) pip uninstall tvdb-async (OR pip3 uninstall tvdb-async)
		

### Dependencies

1. python 3.5+

2. bs4

3. [vinanti](https://github.com/kanishka-linux/vinanti)

----------

### Usage:
    
    1. Only search for titles if available
        
        from tvdb_async import TVDB
    
        def hello(*args):
            # here args[0] will hold dictionary of search results
            # print args to know more about arguments
            print(args) 
            
        tv = TVDB(lang='en')
        
        tv.search('legend of the galactic heroes', onfinished=hello)
        
        # In above code first argument of callback hello will return
        # dictionary of search result
            
    2. Search and grab most suitable title from search result
        
        from tvdb_async import TVDB
    
        def hello(*args):
        
            #This function will return metadata asynchronously as it is available
            # here args[0] will hold tvdb series object
            # And args[1] will hold type of information that has been returned
            # print args to know more about arguments
            
            obj = args[0] 
            val = args[1]
            
            if val == 'info':
            
                print(obj.summary) #summary of series
                print(obj.title) #title of series
                
                #other metadata like running status, network etc available in
                #obj.info dict. Iterate over it to know more
                
                for i, j in obj.info.items():
                    print(i, j)
                    
            elif val in ['poster', 'fanart', 'banners']:
            
                # Here one can access posters, fanart and banners links
                #obj.poster, obj.fanart, obj.banners will contain list of images
                print(obj.poster, obj.fanart, obj.banners)
                
            elif val == 'episode-info':
            
                #This field is available only when 'episode_summary' set to 'True'
                #during initialization. 
                print(len(obj.episode_summary), obj.total)
                
                #obj.episode_summary is a dict in which episode numbers are keys
                #iterate over it to more about values
                
                for key, val in obj.episode_summary.items():
                    print(key, val)
                
            elif val == 'season-info':
            
                # Here one can access season information as available in obj.season_episode_dict
                # format: dict = {'season number':[list of episodes with name, list of season posters if available]}
                # This dict contains all the metadata about every episode except its summary
                
                print(obj.season_episode_dict)
            
            elif isinstance(val, list):
            
                #In episode-info field as mentioned above, one can get final complete information
                # about all episodes, but not information about single episode as it is made available.
                
                #So, Here one can access single episode information as it is fetched, without 
                #having to wait for fetching of all episode.
                
                #print val to know about its contents
                
                print(val)
            
        
        # initialize TVDB and grab most appropriate entry from search results.
        
        tv = TVDB(lang='en', search_and_grab=True) 
        
        # initialize TVDB and grab most appropriate entry from search results,
        # along with episode summary of each individual episode.
        
        tv = TVDB(lang='en', search_and_grab=True, episode_summary=True)
        
        
        # initialize TVDB same as above, but wait for 0.2 seconds before making
        # consecutive requests. This wait field is very important, as it limits
        # http requests. So always use it with some rational value.
        
        tv = TVDB(lang='en', search_and_grab=True, episode_summary=True, wait=0.2)
        
        #finally search 
        
        tv.search('legend of the galactic heroes', onfinished=hello)
        
        # directly use already available url
        
        tv.getinfo('https://www.thetvdb.com/series/legend-of-the-galactic-heroes', onfinished=hello)
        
    3. check [tests ](https://github.com/kanishka-linux/tvdb-async/tree/master/tests) folder to know more about api usage
        
----------


