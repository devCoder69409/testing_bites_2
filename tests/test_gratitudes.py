from lib.gratitudes import *

def test_gratitude_returns_blank():
    result_blank = Gratitudes()
    assert result_blank.gratitudes == []

def test_things_I_am_grateful_for():
    things_me_grateful = Gratitudes()
    things_me_grateful.add("house")
    things_me_grateful.add("dog")
    things_me_grateful.add("cat")
    assert things_me_grateful.format() == "Be grateful for: house, dog, cat"



    # result_blank.add("")
    # assert result_blank.format == "Be grateful for: "