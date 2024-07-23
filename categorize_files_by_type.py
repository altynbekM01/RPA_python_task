import os
def categorize_files_by_type(folder_path):
    ## Cheking is there exists such path and is it directory
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"'{folder_path}' does not exist.")
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"'{folder_path}' is not a directory.")

    file_dict = {}
    ## root is the current directory path, directories is a list of subdirectories, files is list of file names
    for root, directories, files in os.walk(folder_path):
        for file_name in files:
            # forming path to file
            full_path = os.path.join(root, file_name)
            # extracting file's extension
            directories, ext = os.path.splitext(file_name)
            # forming our dictionary
            if ext not in file_dict:
                file_dict[ext] = []
            file_dict[ext].append(full_path)
    # case if there was no file without extension
    if '' not in file_dict:
        file_dict[''] = []

    return file_dict

folder_path = input()
result = categorize_files_by_type(folder_path)
print(result)
