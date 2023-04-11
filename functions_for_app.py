FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH ): #the default will be the todos.txt but we can change the arguemnt inside the func.
    """ read a text file and the return the list of the to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# print(help(get_todos)) #here we will get the docstring that we wrote


def write_todos(todos_arg,filepath=FILEPATH ):
    """ write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet":feet,"inches":inches}

def convert(feet,inches):
    meters = feet * 0.3048 + inches* 0.0254
    return meters

FREEZING_POINT = 0
BOILING_POINT = 100
def get_state(temperature):
    temperature = float(temperature)
    if temperature <= FREEZING_POINT:
        return "gas"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "liquid"
    else:
        return "solid"

