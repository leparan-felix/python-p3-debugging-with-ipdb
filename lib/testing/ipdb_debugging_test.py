#!/usr/bin/env python3

from ipdb_debugging import plus_two  # Import the function

class TestIpdbDebugging:
    '''Tests for ipdb_debugging.py'''

    def test_adds_two(self):
        '''Test that plus_two() adds 2 to the input argument and returns the correct result.'''
        result = plus_two(3)  # Call the function
        assert result == 5     # Assert that the result is 5
