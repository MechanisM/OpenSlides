#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Unit test for OpenSlides __init__.py

    :copyright: 2011, 2012 by OpenSlides team, see AUTHORS.
    :license: GNU GPL, see LICENSE for more details.
"""

from django.test import TestCase

from openslides import get_version

class InitTest(TestCase):
    def test_get_version(self):
        self.assertEqual(get_version((1, 3, 0, 'beta', 2)), '1.3-beta2')
        self.assertEqual(get_version((1, 0, 0, 'final', 0)), '1.0')
        self.assertEqual(get_version((2, 5, 3, 'alpha', 0)), '2.5.3-alpha0')
        git_version = get_version((2, 5, 0, 'dev', 0))
        if 'unknown' in git_version:
            self.assertEqual(len(git_version), 14)
        else:
            self.assertEqual(len(git_version), 47)
