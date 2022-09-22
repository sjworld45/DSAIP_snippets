import random

prize_results = []
prizes = [0, 1, 2]

trials = 10**5

for i in range(trials):
    prize_results.append(random.choice(prizes))
    
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
    choice = random.choice(doors)
            
    if choice == prize_results[i]:
        res += 1
    
        
        
print(res/trials)