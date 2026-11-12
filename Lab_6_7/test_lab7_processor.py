import pytest
from hypothesis import given, strategies as st

from lab7_processor import parse_request, total_travel, load_percent


@given(st.text())
def test_parse_request_rejects_or_parses_arbitrary_strings(value):
    try:
        result = parse_request(value)
    except ValueError:
        return
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(isinstance(floor, int) for floor in result)


@given(st.text())
def test_total_travel_rejects_or_returns_nonnegative_integer(value):
    try:
        result = total_travel(value)
    except ValueError:
        return
    assert isinstance(result, int)
    assert result >= 0


@given(st.text())
def test_load_percent_rejects_or_returns_integer(value):
    try:
        result = load_percent(value)
    except ValueError:
        return
    assert isinstance(result, int)
    assert result >= 0


@given(st.integers(), st.integers())
def test_parse_request_round_trip(start, end):
    assert parse_request(f"{start}->{end}") == (start, end)


@given(st.lists(st.integers(), min_size=1, max_size=30))
def test_total_travel_matches_adjacent_floor_distance(floors):
    csv = ",".join(str(floor) for floor in floors)
    expected = sum(abs(floors[index + 1] - floors[index]) for index in range(len(floors) - 1))
    assert total_travel(csv) == expected


@given(st.integers(min_value=0), st.integers(min_value=1))
def test_load_percent_matches_integer_percentage(load, capacity):
    assert load_percent(f"{load} of {capacity}") == load * 100 // capacity


@pytest.mark.parametrize("value", [None, 1, 1.5, [], {}])
def test_parse_request_rejects_non_string(value):
    with pytest.raises(TypeError):
        parse_request(value)


@pytest.mark.parametrize("value", [None, 1, 1.5, [], {}])
def test_total_travel_rejects_non_string(value):
    with pytest.raises(TypeError):
        total_travel(value)


@pytest.mark.parametrize("value", [None, 1, 1.5, [], {}])
def test_load_percent_rejects_non_string(value):
    with pytest.raises(TypeError):
        load_percent(value)


@pytest.mark.parametrize("value", ["", " ", "1", "1-2", "1->", "->2", "1->2->3", "a->2"])
def test_parse_request_rejects_invalid_format(value):
    with pytest.raises(ValueError):
        parse_request(value)


@pytest.mark.parametrize("value", ["", " ", "1,,2", ",1", "1,", "a,2", "1.5,2"])
def test_total_travel_rejects_invalid_floor_lists(value):
    with pytest.raises(ValueError):
        total_travel(value)


@pytest.mark.parametrize("value", ["", "1", "1/2", "1 of 0", "-1 of 10", "a of 10", "1 of -5", "1 of "])
def test_load_percent_rejects_invalid_loads(value):
    with pytest.raises(ValueError):
        load_percent(value)
