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
    for idx in range(len(sequence)):
        if sequence[idx] == number:
            position.append(idx + 1)
    count = len(position)

    # results = {"postions": [],"count": 0}
    # for index in range(len(numbers)):
    #   if numbers[index] == number:
    #       results["positions"].append(index)
    #       results["count"] = results["count"] + 1
    # return results

    return {"postions": position, "count": count}


def pattern_search(sequence, pattern):
    positions = set()
    for idx in range(len(sequence)):
        pattern_len = len(pattern)
        if sequence[idx: idx + pattern_len] == pattern:
            positions.add(idx + pattern_len // 2 + 1)

    return positions


def main():
    sequence = read_data("sequential.json", "dna_sequence")
    print(sequence)
    # number = int(input("Číslo: "))
    # print(linear_search(sequence, number))
    print(pattern_search(sequence, "ATA"))


if __name__ == '__main__':
    main()
