from lib.check_codeword import check_codeword

def test_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_near_codeword():
    result = check_codeword("he")
    assert result == "Close, but nope."

def test_wrong_codeword():
    result = check_codeword("blabla")
    assert result == "WRONG!"