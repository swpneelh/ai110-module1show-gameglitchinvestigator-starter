# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 37
2. Game returns "Too Low"
3. User enters a guess of 79 → "Too High"
4. Score updates correctly after each guess
5. Hint correctly indicates what to guess
6. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
python -m pytest test_game_logic.py -v
=============================================== test session starts ===============================================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\Acer\AppData\Local\Python\pythoncore-3.13-64\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Acer\OneDrive\Desktop\AI110\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 30 items                                                                                                 

test_game_logic.py::test_too_high_tells_you_to_go_lower PASSED                                               [  3%]
test_game_logic.py::test_too_low_tells_you_to_go_higher PASSED                                               [  6%]
test_game_logic.py::test_correct_guess_wins PASSED                                                           [ 10%]
test_game_logic.py::test_comparison_is_numeric_not_lexicographic[9-10-Too Low] PASSED                        [ 13%]
test_game_logic.py::test_comparison_is_numeric_not_lexicographic[10-9-Too High] PASSED                       [ 16%]
test_game_logic.py::test_comparison_is_numeric_not_lexicographic[100-2-Too High] PASSED                      [ 20%]
test_game_logic.py::test_comparison_is_numeric_not_lexicographic[2-100-Too Low] PASSED                       [ 23%]
test_game_logic.py::test_check_guess_handles_ints_consistently PASSED                                        [ 26%]
test_game_logic.py::test_first_try_win_scores_full_100 PASSED                                                [ 30%]
test_game_logic.py::test_win_score_decreases_by_10_per_attempt PASSED                                        [ 33%]
test_game_logic.py::test_win_score_floored_at_10 PASSED                                                      [ 36%]
test_game_logic.py::test_win_adds_to_existing_score PASSED                                                   [ 40%]
test_game_logic.py::test_too_high_always_penalizes[1] PASSED                                                 [ 43%]
test_game_logic.py::test_too_high_always_penalizes[2] PASSED                                                 [ 46%]
test_game_logic.py::test_too_high_always_penalizes[3] PASSED                                                 [ 50%]
test_game_logic.py::test_too_high_always_penalizes[4] PASSED                                                 [ 53%]
test_game_logic.py::test_too_low_always_penalizes[1] PASSED                                                  [ 56%]
test_game_logic.py::test_too_low_always_penalizes[2] PASSED                                                  [ 60%]
test_game_logic.py::test_too_low_always_penalizes[3] PASSED                                                  [ 63%]
test_game_logic.py::test_too_low_always_penalizes[4] PASSED                                                  [ 66%]
test_game_logic.py::test_high_and_low_penalties_are_equal PASSED                                             [ 70%]
test_game_logic.py::test_get_range_for_difficulty[Easy-expected0] PASSED                                     [ 73%]
test_game_logic.py::test_get_range_for_difficulty[Normal-expected1] PASSED                                   [ 76%]
test_game_logic.py::test_get_range_for_difficulty[Hard-expected2] PASSED                                     [ 80%]
test_game_logic.py::test_get_range_for_difficulty[Unknown-expected3] PASSED                                  [ 83%]
test_game_logic.py::test_parse_guess_valid PASSED                                                            [ 86%]
test_game_logic.py::test_parse_guess_float_is_truncated PASSED                                               [ 90%]
test_game_logic.py::test_parse_guess_empty PASSED                                                            [ 93%]
test_game_logic.py::test_parse_guess_non_numeric PASSED                                                      [ 96%]
test_game_logic.py::test_parse_guess_out_of_range PASSED                                                     [100%]

=============================================== 30 passed in 0.26s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
