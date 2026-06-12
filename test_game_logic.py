"""
Pytest suite covering the bugs that were fixed in logic_utils.py.

Run from the project folder with:
    pytest test_game_logic.py -v
"""

import pytest

from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


# ---------------------------------------------------------------------------
# Bug 1: hint messages were swapped (too-high told you to go HIGHER, etc.)
# ---------------------------------------------------------------------------

def test_too_high_tells_you_to_go_lower():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_tells_you_to_go_higher():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_correct_guess_wins():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


@pytest.mark.parametrize(
    "guess, secret, expected",
    [
        (9, 10, "Too Low"),    # lexicographically "9" > "10" — caught the old string bug
        (10, 9, "Too High"),
        (100, 2, "Too High"),
        (2, 100, "Too Low"),
    ],
)
def test_comparison_is_numeric_not_lexicographic(guess, secret, expected):
    outcome, _ = check_guess(guess, secret)
    assert outcome == expected


# ---------------------------------------------------------------------------
# Bug 2: secret was stringified on even attempts, breaking int comparison.
# check_guess must work with integer arguments (the only type app.py now passes).
# ---------------------------------------------------------------------------

def test_check_guess_handles_ints_consistently():
    # Same inputs should give the same result regardless of "attempt parity".
    assert check_guess(42, 42) == ("Win", "🎉 Correct!")
    assert check_guess(7, 7) == ("Win", "🎉 Correct!")


# ---------------------------------------------------------------------------
# Bug 3: win score was off by one (penalized an attempt never taken).
# ---------------------------------------------------------------------------

def test_first_try_win_scores_full_100():
    assert update_score(current_score=0, outcome="Win", attempt_number=1) == 100


def test_win_score_decreases_by_10_per_attempt():
    assert update_score(0, "Win", 2) == 90
    assert update_score(0, "Win", 3) == 80


def test_win_score_floored_at_10():
    assert update_score(0, "Win", 50) == 10


def test_win_adds_to_existing_score():
    assert update_score(current_score=25, outcome="Win", attempt_number=1) == 125


# ---------------------------------------------------------------------------
# Bug 4: wrong-guess penalty was inconsistent (Too High could ADD points).
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("attempt", [1, 2, 3, 4])
def test_too_high_always_penalizes(attempt):
    assert update_score(100, "Too High", attempt) == 95


@pytest.mark.parametrize("attempt", [1, 2, 3, 4])
def test_too_low_always_penalizes(attempt):
    assert update_score(100, "Too Low", attempt) == 95


def test_high_and_low_penalties_are_equal():
    assert update_score(100, "Too High", 2) == update_score(100, "Too Low", 2)


# ---------------------------------------------------------------------------
# Supporting helpers (range + input parsing) — guard against regressions.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "difficulty, expected",
    [
        ("Easy", (1, 20)),
        ("Normal", (1, 100)),
        ("Hard", (1, 50)),
        ("Unknown", (1, 100)),  # falls back to default
    ],
)
def test_get_range_for_difficulty(difficulty, expected):
    assert get_range_for_difficulty(difficulty) == expected


def test_parse_guess_valid():
    assert parse_guess("15", 1, 20) == (True, 15, None)


def test_parse_guess_float_is_truncated():
    ok, value, err = parse_guess("15.9", 1, 20)
    assert ok is True
    assert value == 15
    assert err is None


def test_parse_guess_empty():
    ok, value, err = parse_guess("", 1, 20)
    assert ok is False
    assert value is None


def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc", 1, 20)
    assert ok is False
    assert "not a number" in err


def test_parse_guess_out_of_range():
    ok, value, err = parse_guess("99", 1, 20)
    assert ok is False
    assert "between 1 and 20" in err
