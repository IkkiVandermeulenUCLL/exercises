from intervals import overlapping_intervals
import pytest

@pytest.mark.parametrize(
        "interval1, interval2",
        (    
            ((1,5),(4,6)),
            ((1,3),(2,3)),
            ((5,9),(6,10)),
            ((0,8),(1,9)),
            ((5,6),(7,6)),
            ((1,9),(9,5)),
            ((9,6),(1,8)),
            
        ))
def test_overlapping_intervals(interval1, interval2):
    assert overlapping_intervals(interval1, interval2) == True