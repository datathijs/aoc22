def file_to_list(filename):
    empty_to_zero = lambda i : i or 0
    lines = []
    with open(filename) as f:
        lines = [int(empty_to_zero(line.rstrip('\n'))) for line in f]
    return lines

def main():
    input = file_to_list('aoc1input.txt')
    print(input[:5])

if __name__ == '__main__':
    print("this code shouldn't be executed when imported")
    main()