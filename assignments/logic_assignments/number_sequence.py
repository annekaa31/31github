def find_next_sequence(sequence):
    if len(sequence) < 2:
        print("The sequence should have at least 2 numbers")

sequence = [2, 4, 8, 16]
ratio = 2
next_num = sequence[-1] * ratio
print(f"The next number in the sequence is {next_num}")
