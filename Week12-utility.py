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


def ScoreFinder(names_list, scores_list, player):
    new_names_list = []
    player_to_find = player.lower()
    for name in names_list:
        new_names_list.append(name.lower())
    if player_to_find in new_names_list:
        for i in range(len(new_names_list)):
            if new_names_list[i] == player_to_find:
                index = i
        score = scores_list[index]
        player = player_to_find.capitalize()
        print("Output %s got a score of %d" %(player , score))
    else:
        print("OUTPUT player not found")
