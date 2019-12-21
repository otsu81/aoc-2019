import json

def main():
    program = '1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,1,23,6,27,1,6,27,31,1,13,31,35,1,13,35,39,1,39,13,43,2,43,9,47,2,6,47,51,1,51,9,55,1,55,9,59,1,59,6,63,1,9,63,67,2,67,10,71,2,71,13,75,1,10,75,79,2,10,79,83,1,83,6,87,2,87,10,91,1,91,6,95,1,95,13,99,1,99,13,103,2,103,9,107,2,107,10,111,1,5,111,115,2,115,9,119,1,5,119,123,1,123,9,127,1,127,2,131,1,5,131,0,99,2,0,14,0'
    memory = program.split(',')
    for x in range(len(memory)):
        memory[x] = int(memory[x])

    position = 0

    for position in range(0, len(memory)-1, 4):
        value = memory[position]
        print(f"{position}: {value}")
        if value == 1:
            target_pos = memory[position + 3]
            memory[target_pos] = memory[memory[position+1]] + memory[memory[position+2]]
            print(memory[target_pos])
        elif value == 2:
            target_pos = memory[position + 3]
            memory[target_pos] = memory[memory[position+1]] * memory[memory[position+2]]
        elif value == 99:
            break
        else:
            print('error')

    print(json.dumps(memory, indent=4, default=str))


if __name__ == '__main__':
    main()