from lib.present import *
import pytest

def test_contents():
    contents_self = Present()

def test_wrap_contents():
    wrap_contents = Present()
    wrap_contents.wrap("hello")
    assert wrap_contents.unwrap() == "hello"

def test_unwrapping_empty_wrap():
    unwrapping = Present()
    with pytest.raises(Exception) as e:
        unwrapping.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."

def test_wrapping_twice_error():
    wrapping_twice = Present()
    wrapping_twice.wrap("morning")
    with pytest.raises(Exception) as e:
        wrapping_twice.wrap("afternoon")
    message = str(e.value)
    assert message == "Contents have already been wrapped."

def test_rewrapping_already_wrapped():
    rewrapping = Present()
    rewrapping.wrap("morning")
    with pytest.raises(Exception) as e:
        rewrapping.wrap("afternoon")
    assert rewrapping.unwrap() == "morning"

