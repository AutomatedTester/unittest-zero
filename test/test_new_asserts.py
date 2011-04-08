#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is UnittestZero.
#
# The Initial Developer of the Original Code is
# Mozilla Corp.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns 
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

import pytest
from unittestzero import Assert

class TestNewAsserts:

    def test_that_are_equal(self):
        Assert.equal("1","1")
        Assert.equal(1,1)

    def test_that_are_not_equal_throws_error(self):
        try:
            Assert.equal("1", "2")
        except AssertionError, e:
            pass

    def test_that_items_are_not_equal(self):
        Assert.not_equal("a","b")
        Assert.not_equal(1,2)

    def test_that_we_can_check_for_true(self):
        Assert.true(True)
        Assert.true("a" in "bad")
        Assert.true(1 == 1)

    def test_that_get_an_exception_if_not_true(self):
        try:
            Assert.true(False)
        except AssertionError, e:
            pass

    def test_that_we_can_check_for_false(self):
        Assert.false(False)
        Assert.false("z" in "bad")
        Assert.false(1==2)

    def test_that_we_get_an_exception_if_not_false(self):
        try:
            Assert.false(True)
        except:
            pass

    def test_that_something_is_none(self):
        Assert.none(None)


    def test_that_if_not_none_exception_thrown(self):
        try:
            Assert.none(1)
        except:
            pass

    def test_that_not_none_passes(self):
        Assert.not_none(1)
        Assert.not_none("a")
        Assert.not_none("a" in "bad")

    def that_we_can_throw_when_we_fail(self):
        try:
            Assert.fail("omg!!!!")
        except AssertionError as e:
            pass
