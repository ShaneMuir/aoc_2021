from aocd.models import Puzzle
from aocd import submit
day_1 = Puzzle(year=2021, day=1)
my_data = day_1.input_data

def puzzle_one():
	""" algorithm for puzzle one part 1 aoc"""
	numbers = []
	counter = 0

	for line in my_data.splitlines():
		numbers.append(int(line))

	first_num = numbers[0]

	for n in numbers[1:]:
		if n > first_num:
			counter += 1
		first_num = n

	submit(counter, part="a", day=1, year=2021) # Correct ONTO part 2

def puzzle_one_part_two():
	numbers = []

	for line in my_data.splitlines():
		numbers.append(int(line))

	count = sum(
		numbers[i] > numbers[i - 3]
		for i in range(1, len(numbers))
		)

	submit(count, part="b", day=1, year=2021) # Correct ONTO puzzle 2

