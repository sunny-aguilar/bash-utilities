#!/usr/bin/python3
####################################################################
# Author:               Sandro Aguilar
# Date:                 March 20, 2020
# Class:                Coursera - unit testing
# Description:          Enter description here
####################################################################
import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)











