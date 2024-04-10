import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    return data[field]


def linear_search(sequence, number):
    position = []
    idx = 0
    for item in sequence:
        idx = idx + 1
        if item == number:
            position.append(idx)
    count = len(position)
    
    # results = {"postions": [],"count": 0}
    # for index in range(len(numbers)):
    #   if numbers[index] == number:
    #       results["positions"].append(index)
    #       results["count"] = results["count"] + 1
    # return results

    return {"postions": position, "count": count}


def main():
    sequence = read_data("sequential.json", "unordered_numbers")
    print(sequence)
    number = int(input("Číslo: "))
    print(linear_search(sequence, number))


if __name__ == '__main__':
    main()
