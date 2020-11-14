"""
Convert Hebrew gibberish to UTF-8

Usage:
    > python gib2u.py TARGET
    target can be a file or a folder
"""
import os
from sys import argv


def convert_gibberish_to_utf8(s):
    """
    :param str s: The Hebrew gibberish to convert to UTF-8
    :return str: The converted string if successful; the original string otherwise
    """
    try:
        s = bytes(s, "iso-8859-1").decode("windows-1255")
    except:     # No specific exception since it isn't handled anyway
        pass
    return s


def convert_and_rename(full_name_target: str):
    """
    Convert and rename a target file/directory name from Hebrew gibberish to UTF-8
    """
    full_path, target = os.path.split(full_name_target)
    if not target == (converted := convert_gibberish_to_utf8(target)):
        os.rename(full_name_target, f"{full_path}/{converted}")


def convert_entire_directory(target_folder: str):
    """
    Iterate over a directory and rename all files / subdirectories.
    Target folder doesn't have to be an absolute path
    """
    root_dir = os.path.abspath(target_folder)
    for item in os.listdir(target_folder):
        full_item_name = f"{root_dir}/{item}"
        if os.path.isdir(full_item_name):
            convert_entire_directory(full_item_name)
        try:
            convert_and_rename(full_item_name)
        except:
            pass


def main(dest):
    if os.path.isdir(dest):
        convert_entire_directory(dest)
    else:
        convert_and_rename(dest)


if __name__ == '__main__':
    if len(argv) > 1:
        main(argv[1])
    else:
        print(f"Usage:\n\t{__file__} TARGET")
