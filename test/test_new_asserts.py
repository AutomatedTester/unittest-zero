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
#                 Joel Andersson <janderssn@gmail.com>
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
        Assert.equal("1", "1")
        Assert.equal(1, 1)

    def test_that_are_not_equal_throws_error(self):
        try:
            Assert.equal("1", "2")
        except AssertionError, e:
            pass

    def test_that_items_are_not_equal(self):
        Assert.not_equal("a", "b")
        Assert.not_equal(1, 2)

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
        Assert.false(1 == 2)

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

    def test_is_sorted_ascending_success_1(self):
        Assert.is_sorted_ascending([1])

    def test_is_sorted_ascending_success_3(self):
        Assert.is_sorted_ascending([1, 2, 3])

    def test_is_sorted_ascending_fail(self):
        try:
            Assert.is_sorted_ascending([1, 3, 2], "failure message")
        except AssertionError as e:
            assert e.msg == "2 is not before 3. failure message"

    def test_is_sorted_ascending_fail_no_message(self):
        try:
            Assert.is_sorted_ascending([1, 3, 2])
        except AssertionError as e:
            assert e.msg == "2 is not before 3. "

    def test_is_sorted_ascending_empty(self):
        Assert.is_sorted_ascending([])

    def test_is_sorted_ascending_none(self):
        try:
            Assert.is_sorted_ascending(None)
        except TypeError as e:
            pass

    def test_is_sorted_descending_success_1(self):
        Assert.is_sorted_descending([1])

    def test_is_sorted_descending_success_3(self):
        Assert.is_sorted_descending([3, 2, 1])

    def test_is_sorted_descending_fail(self):
        try:
            Assert.is_sorted_descending([3, 1, 2], "failure message")
        except AssertionError as e:
            assert e.msg == "1 is not before 2. failure message"

    def test_is_sorted_descending_fail_no_message(self):
        try:
            Assert.is_sorted_descending([3, 1, 2])
        except AssertionError as e:
            assert e.msg == "1 is not before 2. "

    def test_is_sorted_descending_empty(self):
        Assert.is_sorted_descending([])

    def test_is_sorted_descending_none(self):
        try:
            Assert.is_sorted_descending(None)
        except TypeError as e:
            pass

    def test_that_assert_raises_catches_exceptions(self):

        Assert.raises(ZeroDivisionError, self._divide_by_zero)

    def test_that_we_raise_when_error_not_thrown(self):
        try:
            Assert.raises(Exception, self._add_num, 5, 4)
        except AssertionError:
            pass

    def test_raises_failure_with_message(self):
        try:
            Assert.raises(Exception, self._add_num, 5, 4, msg="failure message")
        except AssertionError as e:
            Assert.equal(e.msg, "Exception was not raised. failure message")

    def test_raises_failure_without_message(self):
        try:
            Assert.raises(Exception, self._add_num, 5, 4,)
        except AssertionError as e:
            Assert.equal(e.msg, "Exception was not raised. ")

    def test_that_we_can_check_items_contain_something(self):
        Assert.contains("a", "bad")
        Assert.contains("a", ["a", "b", "c"])
        Assert.contains("dog", {"dog": "poodle", "cat": "siamese", "horse": "arabian"})

    def test_that_string_does_not_contain_letter(self):
        try:
            Assert.contains("a", "cde")
        except AssertionError as e:
            pass

    def test_that_list_does_not_contain_element_failure_no_message(self):
        try:
            Assert.contains("d", ["a", "b", "c"])
        except AssertionError as e:
            Assert.equal(e.msg, "d is not found in ['a', 'b', 'c']. ")

    def test_dict_does_not_contain_key_failure_with_message(self):
        try:
            Assert.contains("dog", {"cat": "siamese", "horse": "arabian"},
                            msg="failure message")
        except AssertionError as e:
            Assert.equal(e.msg,
                         "dog is not found in {'horse': 'arabian', 'cat': 'siamese'}. failure message")

    def test_less_success(self):
        Assert.less("1", "2")
        Assert.less(1, 2)

    def test_less_fail_string(self):
        try:
            Assert.less("2", "1")
        except AssertionError, e:
            pass

    def test_less_fail_int(self):
        try:
            Assert.less(2, 1)
        except AssertionError, e:
            pass

    def test_less_fail_string_message(self):
        try:
            Assert.less("2", "1", "message")
        except AssertionError, e:
            pass

    def test_less_fail_int_message(self):
        try:
            Assert.less(2, 1, "message")
        except AssertionError, e:
            pass

    def test_greater_success(self):
        Assert.greater("2", "1")
        Assert.greater(2, 1)

    def test_greater_fail_string(self):
        try:
            Assert.greater("1", "2")
        except AssertionError, e:
            pass

    def test_greater_fail_int(self):
        try:
            Assert.greater(1, 2)
        except AssertionError, e:
            pass

    def test_greater_fail_string_message(self):
        try:
            Assert.greater("1", "2", "message")
        except AssertionError, e:
            pass

    def test_greater_fail_int_message(self):
        try:
            Assert.greater(1, 2, "message")
        except AssertionError, e:
            pass

    def test_greater_equal_success(self):
        Assert.greater_equal("2", "1")
        Assert.greater_equal(2, 1)
        Assert.greater_equal("1", "1")
        Assert.greater_equal(1, 1)

    def test_greater_equal_fail_string(self):
        try:
            Assert.greater_equal("1", "2")
        except AssertionError, e:
            pass

    def test_greater_equal_fail_int(self):
        try:
            Assert.greater_equal(1, 2)
        except AssertionError, e:
            pass

    def test_greater_equal_fail_string_message(self):
        try:
            Assert.greater_equal("1", "2", "message")
        except AssertionError, e:
            pass

    def test_greater_equal_fail_int_message(self):
        try:
            Assert.greater_equal(1, 2, "message")
        except AssertionError, e:
            pass

    def test_less_equal_success(self):
        Assert.less_equal("1", "2")
        Assert.less_equal(1, 2)
        Assert.less_equal("1", "1")
        Assert.less_equal(1, 1)

    def test_less_equal_fail_string(self):
        try:
            Assert.less_equal("2", "1")
        except AssertionError, e:
            pass

    def test_less_equal_fail_int(self):
        try:
            Assert.less_equal(2, 1)
        except AssertionError, e:
            pass

    def test_less_equal_fail_string_message(self):
        try:
            Assert.less_equal("2", "1", "message")
        except AssertionError, e:
            pass

    def test_less_equal_fail_int_message(self):
        try:
            Assert.less_equal(2, 1, "message")
        except AssertionError, e:
            pass

    def test_endswith_success(self):
        Assert.endswith("abcde", "de")
        Assert.endswith("abcde", "abcde")

    def test_endswith_fail(self):
        try:
            Assert.endswith("abcde", "abc")
        except AssertionError, e:
            pass

    def _divide_by_zero(self):
        return 1 / 0

    def _add_num(self, first, second):
        return first + second
