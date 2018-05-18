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

