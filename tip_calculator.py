print('''

 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|


''')

print("Welcome to the Tip Calculator.")

bill = input("What was the total bill?  $ ")

tip = input("What percentage tip would you like to give? 10, 12, or 15?  ")

people = input("How many people to split the bill?  ")

tip_cost = (float(bill) * float(tip)) / 100

total_bill = float(bill) + float(tip_cost)

per_head = round(float(total_bill) / float(people),3)

print(f"Each person should pay: $ {per_head}")


print('''

  ___                            ___
 ||  |   ___         ___        ||  |
 || _|__/  _\_______/  _\_______|| _|
 ||(___(  (________(  (_________||((_)
 ||  |  \___/       \___/       ||  |
 ||  |         ___              ||  |
 || _|________/  _\_____________|| _|
 ||(_________(  (_______________||((_)
 ||  |        \___/             ||  |
 ||  |                          ||  |
 ||  |                          ||  | 
 ||  |                          ||  |


''')