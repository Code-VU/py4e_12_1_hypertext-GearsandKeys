
from random import randint
from unittest.mock import Mock
import socket1

def test_calculateAbsolute_printsABS_lessThan21(capfd, monkeypatch):
    in_num = randint(-100, 21)
    input = [in_num]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    socket1.getWebData()

    out, err = capfd.readouterr()
       
    assert "Why should you learn to write programs?" in out
    assert "Writing programs (or programming) is a very creative " in out
    assert "and rewarding activity.  You can write programs for" in out
    assert "many reasons, ranging from making your living to solving" in out
    assert "a difficult data analysis problem to having fun to helping" in out
    assert "someone else solve a problem.  This book assumes that " in out
    assert "everyone needs to know how to program, and that once " in out
    assert "you know how to program you will figure out what you want " in out
    assert "to do with your newfound skills. " in out
