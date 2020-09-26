import pytest
from collections import namedtuple
from ..template import *
import json
import inspect


PATH_TO_CASES = 'cases.json'
Case = namedtuple('Case', ['input', 'result'])


def args_wrapper(name: str, case: list):
    """
    Very useful feature to pack your case.
    Make your case as class with __repr__ method and be happy
    :return:
    """
    return pytest.mark.parametrize(name, case, ids=list(map(repr, case)))


def test_t1(case):
    assert t1(case['input']) == case['output']


def test_t2(case):
    assert t2(case['input']) == case['output']


def test_t3(case):
    assert t3(case['input']) == case['output']


def test_t4(case):
    assert t4(case['input'], case['input2']) == case['output']


def test_t5(case):
    assert t5(case['input']) == case['output']


def test_t6(case):
    assert t6(case['input']) == case['output']


def test_t7(case):
    assert t7(case['input']) == case['output']


def test_t8(case):
    assert t8(case['input']) == case['output']


def test_t9(case):
    assert t9(case['input']) == case['output']


def test_t10(case):
    assert t10(case['input']) == case['output']


def test_t11(case):
    assert t11(case['input']) == case['output']


def test_t12(case):
    assert t12(case['input']) == case['output']


def test_t13(case):
    assert t13(case['input'], case['input2']) == case['output']


def test_t14(case):
    assert t14(case['input']) == case['output']


def test_t15(case):
    assert t15(case['input']) == case['output']
