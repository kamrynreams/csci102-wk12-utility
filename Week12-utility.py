def PrintOutput(output):
    print("OUTPUT %s" % output)


def LoadFile(filename):
    with open(filename, 'r') as f:
        list = f.readlines()
        return(list)


def UpdateString(string, character, index):
    list = []
    for letter in string:
        list.append(letter)
    list[index] = character
    updated_string = ''.join(list)
    print("OUTPUT", updated_string)


def FindWordCount(list, string):
    counter = 0
    for i in range(len(list)):
        if list[i] == string:
            counter += 1
    return(counter)
