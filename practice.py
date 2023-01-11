def add_money_to_vm(coin):
    for c in coin:
        if c == 'q':
            return .25
        elif c == 'd':
            return .1
        elif c == 'n':
            return .05

money_input = []
money_in_machine = 0
x = input("q for quarter").split()
money_input.append(x)
for y in money_input:
    money_in_machine += add_money_to_vm(y)
    money_input.remove(y)
    
print(money_in_machine)
