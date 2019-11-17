def PrintOutput(output):
    print("OUTPUT %s" % output)

def LoadFile(filename):
    with open(filename, 'r') as f:
        list = f.readlines()
        return(list)
