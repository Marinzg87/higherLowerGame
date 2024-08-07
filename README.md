# Project Higher Lower Game

Steps: 
- breakdown the problem for the small chunks;
- prepare to-do list;
- choose the easy item from the to-do list;
- turn the problem into comments;
- loop: (write code > run code > fix code);
- go to next task.

## Breakdown requirements
- [x] Program will compare the highest score between to randomly chosen elements.
- [x] If user guess was correct, the score will be increase by 1.
- [x] If user guess wasn't correct, the game end and the user will see final score.

## To Do's
- [x] Prepare the flow chart
- [x] Prepare comments or pseudo-code
- [x] Write down the functionalities
- [x] Code
- [x] Test
- [x] Have fun!

## Pseudo-code & Comments
### Comments
Program randomly choose two items from game-data directory.
User will make a guess, which item is higher A or B.
Program will check the answer.
If guess was correct, score will be increased by 1, if guess wasn't correct, game end
and final score will be shown.

### Pseudo-code
```
import random
from art import logo, vs
from game_data import data

print(logo)
randomly choose two items from game_data, assign them respectively to A and B
print(f"Compare A: {item_name_1}, a {item_description_1}, from {item_country_1}"
print(vs)
print(f"Compare B: {item_name_2}, a {item_description_2}, from {item_country_2}"
user make a guess "Who has more followers? Type 'A' or 'B':
check_higher_lower between item_followers_count_1 and item_followers_count_2 and return A or B
check if the user guess == check_higher_lower output
    if yes:
        scorea increase by 1
        start over again from randomly choosen items
    if no:
        end the game, and show the final score
```

## Functionalities
- function to randomly choose the items from game-data, and assign them to variables A and B;
- function to compare the highest value, and return the result.