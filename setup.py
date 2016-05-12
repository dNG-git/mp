# -*- coding: utf-8 -*-
##j## BOF

"""
MediaProvider
A device centric multimedia solution
----------------------------------------------------------------------------
(C) direct Netware Group - All rights reserved
http://www.direct-netware.de/redirect.py?mp

This is a meta package with different but compatible license agreements.
Please validate the individual license agreements and their requirements for
your purposes.
----------------------------------------------------------------------------
setup.py
"""

def get_version():
#
	"""
Returns the version currently in development.

:return: (str) Version string
:since:  v0.1.03
	"""

	return "v0.1.03"
#

from distutils.core import setup
from distutils.command.build_py import build_py
from distutils.command.install_data import install_data
from subprocess import Popen
from os import path
import os
import sys

class BuildPy(build_py):
#
	"""
python.org: Build the .py/.pyc files of a package

:author:    direct Netware Group
:copyright: direct Netware Group - All rights reserved
:package:   mp
:since:     v0.1.03
:license:   https://www.direct-netware.de/redirect?licenses;mpl2
            Mozilla Public License, v. 2.0
	"""

	def run(self):
	#
		"""
Build modules, packages, and copy data files to build directory

:since: v0.1.03
		"""

		root_path = path.abspath(self.build_lib)

		for module in os.listdir("."):
		#
			# Handle "js_djt" specially
			if (module == "js_djt"): continue

			if (path.isdir(module) and os.access(path.join(module, "setup.py"), os.R_OK)):
			#
				process = Popen([ sys.executable,
				                  "setup.py",
				                  "install_lib",
				                  "--install-dir={0}".format(root_path)
				                ],
				                cwd = module
				               )

				process.wait()
			#
		#
	#
#

class InstallData(install_data):
#
	"""
python.org: Implements the Distutils 'install_data' command, for installing
platform-independent data files

:author:    direct Netware Group
:copyright: direct Netware Group - All rights reserved
:package:   mp
:since:     v0.1.03
:license:   https://www.direct-netware.de/redirect?licenses;mpl2
            Mozilla Public License, v. 2.0
	"""

	def run(self):
	#
		"""
Build modules, packages, and copy data files to build directory

:since: v0.1.03
		"""

		root_path = path.abspath(self.install_dir)

		for module in os.listdir("."):
		#
			module_install_path = root_path

			# Handle "js_djt" specially
			if (module == "js_djt"):
			#
				module_install_path = path.join(root_path,
				                                "data",
				                                "mmedia",
				                                "djt"
				                               )
			#

			if (path.isdir(module) and os.access(path.join(module, "setup.py"), os.R_OK)):
			#
				process = Popen([ sys.executable,
				                  "setup.py",
				                  "install_data",
				                  "--install-dir={0}".format(module_install_path)
				                ],
				                cwd = module
				               )

				process.wait()
			#
		#
	#
#

setup(name = "MediaProvider",
      version = get_version(),
      description = "A device centric multimedia solution",
      author = "direct Netware Group et. al",
      author_email = "web@direct-netware.de",
      license = "GPLv2+",
      url = "https://www.mediaprovider.net",

      packages = [ "dNG" ],

      data_files = [ ( "docs", [ "LICENSE", "README" ] ) ],

      # Override build_py to first run builder.py over all PAS modules
      cmdclass = { "build_py": BuildPy,
                   "install_data": InstallData
                 }
)

##j## EOF