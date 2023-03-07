from lib.counter import *

def test_counter_count_0():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

def test_counter_add_single():
    counter = Counter()
    counter.add(6)
    assert counter.report() == "Counted to 6 so far."

def test_counter_add_multiple():
    counter = Counter()
    counter.add(6)
    counter.add(1)
    assert counter.report() == "Counted to 7 so far."

def test_counter_add_pos_neg():
    counter = Counter()
    counter.add(-6)
    counter.add(1)
    assert counter.report() == "Counted to -5 so far."

def test_counter_add_neg_neg():
    counter = Counter()
    counter.add(-6)
    counter.add(-1)
    assert counter.report() == "Counted to -7 so far."

def test_counter_add_pos_neg_multiple():
    counter = Counter()
    counter.add(-6)
    counter.add(1)
    counter.add(-3)
    assert counter.report() == "Counted to -8 so far."