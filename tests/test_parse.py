# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import io
import json
import os
import re
import sys
import unittest

from oelint_parser.cls_stash import Stash

# Python 2 and 3 support
try:
    # Python 2
    unicode  # NOQA
    bytes = str  # NOQA
    str = unicode  # NOQA
except NameError:
    # Python 3
    unicode = str  # NOQA

_sys_v0 = sys.version_info[0]
py2 = _sys_v0 == 2
py3 = _sys_v0 == 3

test_data_dir = os.path.join(os.path.dirname(__file__), 'data')


def relative_walk(dir_path):
    """
    Walk path for bb files and yield relative path  based on dir_path.
    """
    for base_dir, _dirs, files in os.walk(dir_path):
        for file_name in files:
            if not file_name.endswith('.bb'):
                continue
            file_path = os.path.join(base_dir, file_name)
            file_path = file_path.replace(dir_path, '', 1)
            file_path = file_path.strip(os.path.sep)
            yield file_path


def parse_bb(location):
    """
    Return a mapping parsed from an .bb file.
    """
    stash = Stash()
    stash.AddFile(location)
    stash.Finalize()

    data = {}
    for item in stash.GetItemsFor():
        name = getattr(item, 'RawVarName', None)
        if not name:
            continue
        value = item.VarValueStripped
        if name in data:
            data[name] += '\n' + value
        else:
            data[name] = value

    return data


def check_bb(test_location, regen=False):
    expected_location = test_location + '-expected.json'
    results = parse_bb(test_location)

    if regen:
        with io.open(expected_location, 'w', encoding='utf-8') as df:
            df.write(json.dumps(results, indent=2))

    with io.open(expected_location, encoding='utf-8') as df:
        expected = json.load(df)

    assert expected == results


def create_test_function(test_location, test_name, regen=False):
    """
    Return a test function closed on test arguments for a .bb file at test_location
    """

    def test_bb_parse(self):
        check_bb(test_location, regen=regen)

    # set a proper function name to display in reports and use in discovery
    # function names are best as bytes
    if py2 and isinstance(test_name, unicode):
        test_name = test_name.encode('utf-8')
    if py3 and isinstance(test_name, bytes):
        test_name = test_name.decode('utf-8')

    test_bb_parse.__name__ = test_name
    return test_bb_parse


def nopunctuation(text):
    """
    Replaces any non alphanum symbol (i.e. punctuation) in text with space.
    """
    return re.sub(r'[\W_]', ' ', text.strip(), re.MULTILINE | re.UNICODE)


def python_safe_name(s):
    """
    Return a name derived from string `s` safe to use as a Python identifier.
    """
    s = s.lower()
    s = nopunctuation(s)
    s = ' '.join(s.split())
    return s.replace(' ', '_')


def build_tests(
        test_dir,
        clazz,
        prefix='test_bitbake_parse_',
        regen=False
):
    """
    Dynamically build test methods for each .bb file in `test_dir`  and
    attach the test method to the `clazz` class.
    """
    # loop through all items and attach a test method to our test class
    for test_path in relative_walk(test_dir):
        test_name = prefix + python_safe_name(test_path)
        test_loc = os.path.join(test_dir, test_path)
        test_method = create_test_function(test_loc, test_name, regen=regen)
        # attach that method to the class
        setattr(clazz, test_name, test_method)


class TestPokyBitbakeDataDriven(unittest.TestCase):
    # test functions are attached to this class at module import time
    pass


build_tests(
    test_dir=os.path.join(test_data_dir, 'poky'),
    clazz=TestPokyBitbakeDataDriven,
    prefix='test_bb_parse_poky',
    regen=False)
