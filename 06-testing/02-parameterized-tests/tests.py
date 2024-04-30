import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize("string",
    (
        '((()))',
        '()()()',
        '(())()',
        '(())()(())'
    )
)
def test_matching_parentheses_valid_input(string):
    assert matching_parentheses(string)

@pytest.mark.parametrize("string",
    (
        '(((((())))',       
        '(',
        ')',
        '(()))))',
        ')('      
    )
)
def test_matching_parentheses_invalid_input(string):
    assert not matching_parentheses(string)