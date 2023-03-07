from lib.report_length import *

def test_report_length0():
    result = report_length("")
    assert result == "This string was 0 characters long."

def test_report_length1():
    result = report_length("9")
    assert result == "This string was 1 characters long."

def test_report_length10():
    result = report_length("qwertyuiop")
    assert result == "This string was 10 characters long."

def test_report_length6():
    result = report_length("sixsix")
    assert result == "This string was 6 characters long."

