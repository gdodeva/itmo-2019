# -*- coding: utf-8 -*-

import argparse
import os
from datetime import datetime


def create_parser():
    """Create parser for command line."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'command',
        type=str,
        nargs='*',
        help='Command to work with. May have additional parameters',
    )
    return parser


def ls_entered(directory=None):
    """Ls command functionality."""
    if directory is None:
        directory = os.getcwd()
    ls_command = []
    for dir_name in os.listdir(directory):
        if '.' not in dir_name:
            ls_command.append(dir_name)
    for file_name in os.listdir(directory):
        if '.' in file_name:
            ls_command.append(file_name)
    return ls_command


def mk_entered(file_name):
    """Mk command functionality."""
    try:  # noqa: WPS229
        if os.path.isfile(file_name):
            return False
        else:
            my_file = open(file_name, 'w+')  # noqa: WPS515
            my_file.close()
        return True
    except OSError:
        return False


def rm_entered(file_name):
    """Rm command functionality."""
    if os.path.isfile(file_name):
        os.remove(file_name)
    else:
        return False
    return True


def contains_entered(file_name):
    """Contains command functionality."""
    if os.path.isfile(file_name):
        return True
    return False


def since_entered(given_datetime, directory=None):  # noqa C901
    """Since command functionality."""
    if directory is None:
        directory = os.getcwd()
    try:  # noqa: WPS229
        date = datetime.strptime(given_datetime, '%Y-%m-%d_%H:%M:%S')
        files_for_return = []
        for file_name in os.listdir(directory):
            if directory == os.getcwd():
                file_datetime = datetime.fromtimestamp(
                    os.path.getctime(file_name),
                )
            else:
                file_datetime = datetime.fromtimestamp(
                    os.path.getctime(directory / file_name),
                )
            if file_datetime > date:
                files_for_return.append(file_name)
        return files_for_return
    except ValueError:
        return 'Use mask Y-M-D_H:M:S'


def main():
    """Main function code."""
    command = create_parser().parse_args()
    caller = command.command[0]
    parameter = None
    command_list = {
        'ls': ls_entered,
        'mk': mk_entered,
        'rm': rm_entered,
        'contains': contains_entered,
        'since': since_entered,
    }
    if caller in command_list:
        if len(command.command) > 1:
            parameter = command.command[1]
        function_to_call = command_list[caller]
        print(function_to_call(parameter))  # noqa: T001
    else:
        print('Command is not given or not given correctly')  # noqa: T001


if __name__ == '__main__':
    main()
