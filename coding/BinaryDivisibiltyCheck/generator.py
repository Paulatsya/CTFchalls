import random

def generate_binary_line():
    #Generate a random binary string of length 20-50.
    length = random.randint(20, 50)
    return ''.join(random.choices('01', k=length))

def satisfies_condition(line):
    #Check if the line satisfies the (zero % 3 == 0) or (one % 2 == 0) condition.
    zero_count = line.count('0')
    one_count = line.count('1')
    return (zero_count % 3 == 0) or (one_count % 2 == 0)

def generate_data_file(filename, total_lines=10000, valid_count=7777 ):#can change count later
    valid_lines = []
    invalid_lines = []

    while len(valid_lines) < valid_count or len(invalid_lines) < (total_lines - valid_count):
        line = generate_binary_line()
        if satisfies_condition(line):
            if len(valid_lines) < valid_count:
                valid_lines.append(line)
        else:
            if len(invalid_lines) < (total_lines - valid_count):
                invalid_lines.append(line)

    all_lines = valid_lines + invalid_lines
    random.shuffle(all_lines)  # Shuffle so valid and invalid lines are mixed

    with open(filename, "w") as f:
        f.write("\n".join(all_lines))

    print(f"File '{filename}' generated with {total_lines} lines.")
    print(f"Lines satisfying condition: {valid_count}")

# Generate the file
generate_data_file("data.dat")
