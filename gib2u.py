"""
Convert Hebrew gibberish to UTF-8

Usage:
    > python gib2u.py TARGET
    target can be a file or a folder
"""
import os
from time import time
from argparse import ArgumentParser


__author__ = "Ben Baryo"
__version__ = "0.3"


class GhebbrishConverter:
    """
    Convert Hebrew Gibberish (Ghebbrish) to UTF-8
    """
    def __init__(self, target, quiet=False, verbose=True):
        self.target = target
        self.quiet = quiet
        self.verbose = verbose
        if quiet and verbose:
            raise Exception("Unable to set both quiet and verbose at the same time!")
        self.converted_items = 0
        self.all_items = 0

    def run(self):
        start_time = time()
        if os.path.isdir(self.target):
            self.convert_entire_directory(self.target)
        else:
            self.convert_and_rename(self.target)
        if not self.quiet:
            print(f"[!] Conversion of {self.converted_items}/{self.all_items} took {time() - start_time} seconds")

    @staticmethod
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

    def convert_and_rename(self, full_name_target: str):
        """
        Convert and rename a target file/directory name from Hebrew gibberish to UTF-8
        """
        full_path, target = os.path.split(full_name_target)
        if not target == (converted := self.convert_gibberish_to_utf8(target)):
            os.rename(full_name_target, f"{full_path}/{converted}")
            if not self.quiet:
                print(f"[+] Renamed {target} to {converted}")
        else:
            if self.verbose:
                print(f"[-] Unable to convert {target}")

    def convert_entire_directory(self, target_folder: str):
        """
        Iterate over a directory and rename all files / subdirectories.
        Target folder doesn't have to be an absolute path
        """
        root_dir = os.path.abspath(target_folder)
        for item in os.listdir(target_folder):
            full_item_name = f"{root_dir}/{item}"
            if os.path.isdir(full_item_name):
                self.convert_entire_directory(full_item_name)
            try:
                self.convert_and_rename(full_item_name)
            except:
                pass


def create_parser():
    parser = ArgumentParser(description="Fix gibberish Hebrew in file/folder names by converting them to UTF-8.")
    parser.add_argument("target", action="store", help="The target folder / file")
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument("-q", "--quiet", action="store_true", help="Don't print any output")
    verbosity.add_argument("-v", "--verbose", action="store_true", help="Print each successful conversion")
    return parser.parse_args()


def main():
    args = create_parser()
    gib = GhebbrishConverter(args.target, args.quiet, args.verbose)
    gib.run()


if __name__ == '__main__':
    main()
