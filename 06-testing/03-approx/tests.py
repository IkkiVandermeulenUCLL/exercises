import pytest
from pytest import approx
from mystatistics import average

@pytest.mark.parametrize(
        "ns",(
        (1,5,2,3,5,8,3,6,7),
        (1,5,2,4,8,5,11,2,2,2,8),
        (1,2,5,8,7,4,1,23,3,6,88,5,2,5)
        )
)
def test_average(ns):
    assert approx(average(ns), abs=0.01) == round(sum(ns)/len(ns),2)