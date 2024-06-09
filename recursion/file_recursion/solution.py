import os



def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if path == "":
        return []

    final_list = []
    file_name_list = os.listdir(path)
    for file_name in file_name_list:
        sub_list = []
        sub_path = os.path.join(path, file_name)
        if os.path.isdir(sub_path):
            sub_list = find_files(suffix, sub_path)
            final_list = final_list + sub_list
        elif os.path.isfile(sub_path) and sub_path.endswith(suffix):
            final_list.append(sub_path)

    return final_list



# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1  (the folder "testdir" is downloaded form the problem page)
path = os.path.join(os.getcwd(), "testdir") 
result_list = find_files(".c", path)

print(".............test case 1.................")
print("result:\n", "\n".join(result_list))
expected_result = ["subdir1\a.c", "subdir3\subsubdir1\b.c", "subdir5\a.c", "t1.c"]
print("expected result:\n",  "\n".join([os.path.join(path, s) for s in expected_result]))

# Test Case 2 (empty path)
path = ""
result_list = find_files(".c", path)
print(".............test case 2.................")
print("result:\n", result_list)
print("expected result:\n", [])

# Test Case 3 (empty suffix)
path = os.path.join(os.getcwd(), "testdir") 
result_list = find_files("", path)
print(".............test case 3.................")
print("result:\n", "\n".join(result_list))
expected_result = ["subdir1\a.c", "subdir1\a.h", "subdir2\.gitkeep", 
                   "subdir3\subsubdir1\b.c", "subdir3\subsubdir1\b.h",
                   "subdir4\.gitkeep", "subdir5\a.c", "t1.c", "t1.h"]

print("expected result:\n",  "\n".join([os.path.join(path, s) for s in expected_result]))