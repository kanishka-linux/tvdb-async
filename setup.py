"""
Copyright (C) 2018 kanishka-linux kanishka.linux@gmail.com

This file is part of tvdb-async.

tvdb-async is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

tvdb-async is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with tvdb-async.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup

"""
 GNU/Linux users should install dependencies manually using their native
 package manager
"""

setup(
    name='tvdb-async',
    version='0.1',
    license='LGPLv3',
    author='kanishka-linux',
    author_email='kanishka.linux@gmail.com',
    url='https://github.com/kanishka-linux/tvdb-async',
    long_description="README.md",
    packages=['tvdb_async'],
    include_package_data=True,
    install_requires = ['bs4', 'vinanti'],
    description="Async tvdb metadata fetching library",
)
