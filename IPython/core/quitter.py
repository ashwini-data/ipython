# coding: utf-8
"""
A simple class for quitting IPython.

Authors
-------
* Fernando Perez
* Brian Granger
"""

#-----------------------------------------------------------------------------
#  Copyright (C) 2008-2009  The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

import sys

class Quitter(object):
    """Simple class to handle exit, similar to Python 2.5's.

    It handles exiting in an ipython-safe manner, which the one in Python 2.5
    doesn't do (obviously, since it doesn't know about ipython)."""
    
    def __init__(self, shell, name):
        self.shell = shell
        self.name = name
        
    def __str__(self):
        return 'Type %s() to exit.' % self.name

    def __call__(self):
        self.shell.ask_exit()

    __repr__ = __call__
