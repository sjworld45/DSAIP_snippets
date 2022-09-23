import random

prize_results = []
prizes = [0, 1, 2]

TRIALS = 10**5

for i in range(TRIALS):
    prize_results.append(random.choice(prizes))
  
def solve(trials, change = False):
    res = 0
    for i in range(trials):
        doors = [0, 1, 2]
        choice = random.choice(doors)
        # remove one option with no prize
        for door in doors:
            if door != choice and door != prize_results[i]:
                reveal_door = door
                break
        doors.pop(reveal_door)
        # change choice
        if change:
            choice = random.choice(doors)
                
        if choice == prize_results[i]:
            res += 1
            
    return res/trials
    
    

print(f'Ratio of wins when choosing not to switch: {solve(TRIALS):.2f}')
print(f'Ratio of wins when choosing to switch: {solve(TRIALS, True):.2f}')