import pytest

from lab6_elevator_dispatch import next_direction, door_action, pick_elevator


def test_next_direction_up_with_request_above():
    assert next_direction(3, "up", [5, 1]) == "up"


def test_next_direction_up_reverses_when_no_request_above():
    assert next_direction(3, "up", [1, 2]) == "down"


def test_next_direction_up_idle_without_requests():
    assert next_direction(3, "up", []) == "idle"


def test_next_direction_down_with_request_below():
    assert next_direction(5, "down", [2, 8]) == "down"


def test_next_direction_down_reverses_when_no_request_below():
    assert next_direction(5, "down", [6, 8]) == "up"


def test_next_direction_down_idle_without_requests():
    assert next_direction(5, "down", []) == "idle"


def test_next_direction_idle_prefers_above():
    assert next_direction(4, "idle", [7, 2]) == "up"


def test_next_direction_idle_uses_below_when_nothing_above():
    assert next_direction(4, "idle", [1, 3]) == "down"


def test_next_direction_idle_without_requests():
    assert next_direction(4, "idle", []) == "idle"


def test_emergency_holds_doors_regardless_of_load_and_blockage():
    assert door_action(900, True, True) == "hold_open"


def test_overload_is_detected_above_limit():
    assert door_action(631, False, False) == "overload"


def test_load_at_limit_is_not_overload():
    assert door_action(630, False, False) == "close"


def test_blocked_door_reopens():
    assert door_action(200, True, False) == "reopen"


def test_door_closes_when_safe():
    assert door_action(200, False, False) == "close"


def test_pick_elevator_returns_none_for_empty_list():
    assert pick_elevator([], 5) is None


def test_pick_elevator_selects_nearest_idle_car():
    cars = [("A", 1, True), ("B", 4, True), ("C", 9, True)]
    assert pick_elevator(cars, 5) == "B"


def test_pick_elevator_applies_moving_car_penalty():
    cars = [("A", 4, False), ("B", 10, True)]
    assert pick_elevator(cars, 5) == "B"


def test_pick_elevator_keeps_first_car_on_tie():
    cars = [("A", 4, True), ("B", 6, True)]
    assert pick_elevator(cars, 5) == "A"


def test_pick_elevator_uses_penalty_when_comparing_cars():
    cars = [("A", 2, False), ("B", 6, True)]
    assert pick_elevator(cars, 5) == "B"
