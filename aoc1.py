from aoc_template import file_to_list

def main():
    input = file_to_list('aoc1input.txt')

    # for line in input:
    #     print(line)
    max = 0
    rolling_sum = 0
    for each in input:
        print(max, rolling_sum, each)
        if each:
            rolling_sum += each
        else:
            if rolling_sum > max:
                max = rolling_sum
            rolling_sum = each
    if rolling_sum > max:
        max = rolling_sum
            
    print(max)

if __name__ == '__main__':
    main()