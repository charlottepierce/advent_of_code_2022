#!/usr/bin/env python3
import math
from functools import reduce

class Monkey(object):
    def __init__(self, number):
        self.number = number
        self.inspection_count = 0
        self.items = []
        self.operator = None
        self.operation_amount = None # can be a number, or "old"
        self.test_operator = None # always "divisible"
        self.test_amount = None
        self.throw_if_true = None
        self.throw_if_false = None

    def _apply_operator(self, item):
        operation_amount = item if self.operation_amount == "old" else int(self.operation_amount)

        match self.operator:
            case "+":
                return item + operation_amount, "increases", operation_amount
            case "*":
                return item * operation_amount, "is multiplied", operation_amount

    def _run_test(self, item):
        return item % self.test_amount == 0


    def take_turn(self, other_monkeys, worry_mod=None):
        # print(f"Monkey {self.number}")
        while len(self.items) > 0:
            self.inspection_count += 1
            item = self.items.pop(0)
            # print(f"Monkey inspects an item with a worry level of {item}.")
            item, operation_descriptor, amount = self._apply_operator(item)
            # print(f"Worry level {operation_descriptor} by {amount} to {item}.")
            # item = math.floor(item / 3) # only for part 1
            if worry_mod:
                item %= worry_mod
            # print(f"Monkey gets bored with item. Worry level is divided by 3 to {item}.")
            passes_test = self._run_test(item)
            # msg = "is" if passes_test else "is not"
            # print(f"Current worry level {msg} divisible by {self.test_amount}.")
            pass_to = self.throw_if_true if passes_test else self.throw_if_false
            other_monkeys[pass_to].items.append(item)
            # print(f"Item with worry level {item} is thrown to monkey {pass_to}.")


def read_monkey(lines, number):
    new_monkey = Monkey(number)

    items = list(map(int, lines.pop(0).split(":")[1].split(",")))
    new_monkey.items.extend(items)

    operator, amount = lines.pop(0).split(" ")[-2:]
    new_monkey.operator = operator
    new_monkey.operation_amount = amount

    test_operator, amount = lines.pop(0).split(" ")[-3::2]
    amount = int(amount)
    new_monkey.test_operator = test_operator
    new_monkey.test_amount = amount

    if_true = int(lines.pop(0).split(" ")[-1])
    new_monkey.throw_if_true = if_true
    if_false = int(lines.pop(0).split(" ")[-1])
    new_monkey.throw_if_false = if_false

    return new_monkey


if __name__ == "__main__":
    monkeys = {} # id number : Monkey object

    lines = []
    with open("input.txt", 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    while len(lines) > 0:
        next_line = lines.pop(0)
        if next_line.startswith("Monkey"):
            number = int(next_line.strip().split(" ")[1].replace(":", ""))
            monkeys[number] = read_monkey(lines, number)

    # part 1
    # for round in range(20):
    #     for i in range(len(monkeys)):
    #         monkeys[i].take_turn(monkeys)

    # inspection_counts = [m.inspection_count for m in monkeys.values()]
    # inspection_counts.sort()
    # product_of_two_busiest = reduce(lambda x, y: x * y, inspection_counts[-2:])
    # print(f"Part 1: {product_of_two_busiest}")

    # part 2
    worry_mod = reduce(lambda a, b: a * b, [monkeys[k].test_amount for k in monkeys.keys()])
    for round in range(10000):
        for i in range(len(monkeys)):
            monkeys[i].take_turn(monkeys, worry_mod=worry_mod)

    inspection_counts = [m.inspection_count for m in monkeys.values()]
    inspection_counts.sort()
    product_of_two_busiest = reduce(lambda x, y: x * y, inspection_counts[-2:])
    print(f"Part 2: {product_of_two_busiest}")