
import time

def execute_extractor(file_path):

    t0 = time.time()
    with open(file_path, 'r') as f:
        f.close()

    t1 = time.time()

    return {'open_close_time': t1-t0}


# x = execute_extractor('xtract_jsonxml_main.py')
# print(x)
