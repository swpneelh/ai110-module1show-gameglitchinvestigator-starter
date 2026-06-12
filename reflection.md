# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game started off with 7 attempts. After an attempt it told me to go lower which I did, then I went higher. I eventually got to 8 where it told me to go lower, but at 7 it told me to go higher. I ran out of attempts and the secret was 32 which the hints did not lead to.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The number of attempts changed.
  New game would not work, it would require me to refresh the page.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|Entered 101|"Too high"|Told me to "GO LOWER"|NONE|
|Entered -62|"Too low"|Told me to "GO LOWER" |NONE |
|Pressed "New Game" |Game would restart |Attempt counter reset but could not attempt |"Game over. Start a new game to try again" remained |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Claude Code and Claude AI. The coding assistant helped me with identifying and fixing bugs while I referred to the AI for setup and changes. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I edited the newgame function so when the "New Game" button is pressed it actually resets the game and not just the attempt counter visual. Now I am able to reset the game with that button.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Did not get any issues
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested it myself and once the test_game_logic.py was used I ran test cases which passed with 100% on 30 test cases.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I tested the range by using numbers above and below the range for all modes. It showed that the logic fixes were actually working and worked across all difficulties and with a variety of numbers.
- Did AI help you design or understand any tests? How?
It helped me put together test cases but outside of that I tested it on my own to ensure the glitches I experinced were resolved.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
The reruns can occur by either doing a refresh of the entire page or when programmed properly it will refresh the necessary components of the program without requiring you to reload the entire webpage. This way you can preserve history and build a backend to store data.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to ensure I check the logic myself and understand it. I do not want to become dependent on the AI logic alone.
- What is one thing you would do differently next time you work with AI on a coding task?
I think I want to take a look at all the code myself before I prompt AI. I want to make sure I understand why the error happens.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I think it is extremely helpful and can rapidly speed up the production of code. However, I think the programmer must be able to understand it as well
