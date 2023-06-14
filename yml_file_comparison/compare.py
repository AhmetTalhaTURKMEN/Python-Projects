import os

def compare_yaml_files(file1, file2):
    # Find yml files inside the two provided directories
    yml_files1 = find_yaml_files(file1)
    yml_files2 = find_yaml_files(file2)

    # Find files that exist in file1 but not in file2
    missing_files_file1 = sorted(set(yml_files1) - set(yml_files2))
    
    # Find files that exist in file2 but not in file1
    missing_files_file2 = sorted(set(yml_files2) - set(yml_files1))

    # Print missing files and which file they are missing in
    print("Missing yml files in the directories:")
    print(f"{file1}:")
    for i, file in enumerate(missing_files_file1, start=1):
        print(f"{i}. {file}")
        print("************************************************")
    print("----------------------------------------------------------------------")
    print(f"\n{file2}:")
    for i, file in enumerate(missing_files_file2, start=1):
        print(f"{i}. {file}")
        print("************************************************")

def find_yaml_files(directory):
    # Find yml files in the specified directory
    yml_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.yml'):
                yml_files.append(file)
    return yml_files

# Provide the paths and names of the two files
file1 = r'file1'
file2 = r'file2'

# Perform the comparison
compare_yaml_files(file1, file2)
