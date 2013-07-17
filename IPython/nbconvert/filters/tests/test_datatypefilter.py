"""
Module with tests for DataTypeFilter
"""

#-----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------


from ...tests.base import TestsBase
from ..datatypefilter import DataTypeFilter


#-----------------------------------------------------------------------------
# Class
#-----------------------------------------------------------------------------

class Test_DataTypeFilter(TestsBase):
    """Contains test functions for datatypefilter.py"""


    def test_constructor(self):
        """Can an instance of a DataTypeFilter be created?"""
        DataTypeFilter()


    def test_junk_types(self):
        """Can the DataTypeFilter pickout a useful type from a list of junk types?"""
        filter = DataTypeFilter()
        assert filter(["hair", "water", "png", "rock"]) == ["png"]
        assert filter(["pdf", "hair", "water", "png", "rock"]) == ["pdf"]
        assert filter(["hair", "water", "rock"]) == []


    def test_null(self):
        """Will the DataTypeFilter fail if no types are passed in?"""
        filter = DataTypeFilter()
        assert filter([]) == []
