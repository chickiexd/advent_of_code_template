file_path = "./day_00/input.txt"
test_data = []


def read_file_to_list(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


def get_input_data_as_string(test=False):
    if test:
        return "\n".join(test_data)
    with open(file_path, "r") as file:
        return file.read()


def get_input_data_as_list(test=False):
    if test:
        return test_data
    list_from_file = read_file_to_list(file_path)
    return list_from_file
