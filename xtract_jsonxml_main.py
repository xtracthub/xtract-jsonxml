import json
import xmltodict
import statistics as s
import math
import argparse
import time


def xml_to_json(xml_file):
    """Converts an xml file to a json file for processing.

    Parameter:
    xml_file (.xml file)

    Return:
    json_string (str): json string of xml_file.
    """
    with open(xml_file, 'r') as f:
        xml_string = f.read()
    json_string = json.dumps(xmltodict.parse(xml_string), indent=4)
    return json_string


def get_depth(d, level=1):
    """Recursively finds the depth of a dictionary.

    Parameters:
    d (dictionary): Dictionary loaded from a json file.
    level (int): Current level of d.

    Return:
    (int): Depth of d.
    """
    if not isinstance(d, dict) or not d:
        return level
    return max(get_depth(d[k], level + 1) for k in d)


def check_uniform_type(list_of_items, percent_check=1):
    """Checks whether the items in a list have the same type as the first item.

    Parameters:
    list_of_items (list): List of items to check uniformity on.
    percent_check (float): Percentage of items in list_of_items to check for
    uniformity.

    Return:
    (bool): Whether not percent_check% of items in list_of_items are the
    same type as the first item.
    """
    if percent_check < 1:
        num_fields = math.floor(len(list_of_items) * percent_check)
        return all(isinstance(item, type(list_of_items[0])) for item in
                   list_of_items[:num_fields])
    else:
        return all(isinstance(item, type(list_of_items[0])) for item in
                   list_of_items)


def get_numerical_metadata(list_of_items):
    """Gets the mean, mode, 3 largest, and 3 smallest value of a list.

    Parameter:
    list_of_items (list): List of numerical items to find the mean, mode,
    3 largest, and 3 smallest values for.

    Return:
    (dictionary): Dictionary of mean, mode, 3 largest, and 3 smallest values.
    """
    try:
        modeval = s.mode(list_of_items)
    except:
        modeval = "No mode"
    meanval = s.mean(list_of_items)
    max_3 = sorted(list_of_items, reverse=True)[:3]
    min_3 = sorted(list_of_items)[:3]
    return {"mean": meanval, "mode": modeval, "Max 3": max_3, "Min 3": min_3}


def return_string(string, str_file):
    """Writes a string to a file.

    Parameters:
    strings (str): String to write to a file.
    str_file (str): Name of file to output to.
    """
    f = open(str_file, 'a')
    f.write(string + '\n')


def return_list_of_strings(list_of_items, str_file):
    """Writes a list of strings or non-uniform data to a file.

    Parameters:
    list_of_items (list): List of strings or non-uniform data to write to a
    file.
    str_file (str): Name of file to output to.
    """
    f = open(str_file, 'a')
    for item in list_of_items:
        try:
            str(item)
            f.write(str(item) + '\n')
        except:
            continue


def json_tree_data(d, headers, columns, str_file, percent_check=1):
    """Extracts data from a json file.

    Parameters:
    d (dictionary): Dictionary loaded from a json file.
    headers (list): List of headers from d.
    columns (dictionary): Dictionary mapping a key from d to its data.
    str_file (str): Name of file to output strings to.
    percent_check (float): Percentage of items in a list to check
    for uniformity.

    Return:
    (tuple): 2-tuple of headers and columns.
    """
    for k, v in d.items():
        if isinstance(v, dict):
            headers.append(k)
            json_tree_data(v, headers, columns, str_file, percent_check)
        else:
            headers.append(k)
            columns[k] = [type(v)]

            if type(v) == list:

                presumed_type = type(v[0])
                if not check_uniform_type(v, percent_check):
                    presumed_type = str

                if presumed_type in [int, float]:
                    columns[k].append(get_numerical_metadata(v))
                elif presumed_type == str:
                    return_list_of_strings(v, str_file)
            elif type(v) == str:
                return_string(v, str_file)

    return headers, columns


def extract_json_metadata(filename, str_file, percent_check):
    """Extracts metadata from json or xml file.

    Parameter:
    filename (str):  Name of json or xml file to get metadata from.

    Return:
    metadata (dictionary): Dictionary of depth, headers, and columns from
    filename.
    """
    headers = []
    columns = {}

    if filename.endswith(".xml"):
        json_data = json.loads(xml_to_json(filename))
    else:
        with open(filename, 'r') as f:
            json_data = json.loads(f)

    depth = get_depth(json_data)

    json_tree = json_tree_data(json_data, headers, columns, str_file,
                               percent_check)
    headers = json_tree[0]
    columns = json_tree[1]

    metadata = {"maxdepth": depth, "headers": headers, "columns": columns}
    return metadata


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--path", type=str, help="path to json or xml file",
                        required=True)
    parser.add_argument("--percent_check", type=float, default=1,
                        help="percent of columns to check for uniformity")
    args = parser.parse_args()
    parser.add_argument("--str_output", type=str,
                        default="{}-strings.txt".format(args.path),
                        help="file name for string output")
    args = parser.parse_args()

    t0 = time.time()
    meta = {"json/xml": extract_json_metadata(args.path, args.str_output,
                                              args.percent_check)}
    print(meta)
    t1 = time.time()
    print(t1 - t0)
