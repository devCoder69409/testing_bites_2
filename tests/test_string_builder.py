from lib.string_builder import *

def test_empty():
    empty = StringBuilder()
    assert empty.output() == ""

def test_single_string():
    single = StringBuilder()
    single.add("anything")
    assert single.output() == "anything"

def test_size_string():
    size = StringBuilder()
    size.add("anything")
    assert size.size() == 8

def test_multiple_string():
    multiple = StringBuilder()
    multiple.add("one")
    multiple.add(" two")
    assert multiple.output() == "one two"

def test_multiple_size():
    multiple_size = StringBuilder()
    multiple_size.add("one")
    multiple_size.add(" two")
    assert multiple_size.size() == 7

def test_multiple_size_one_empty():
    multiple_size2 = StringBuilder()
    multiple_size2.add("one")
    multiple_size2.add("")
    assert multiple_size2.size() == 3

def test_multiple_size_both_empty():
    multiple_size3 = StringBuilder()
    multiple_size3.add("")
    multiple_size3.add("")
    assert multiple_size3.size() == 0






