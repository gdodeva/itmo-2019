# -*- coding: utf-8 -*-

import os
import subprocess  # noqa S404
import unittest
import pytest

from cats_composition import CatProcessor, main
from cats_direct import fetch_cat_fact, fetch_cat_image, save_cat


class CatsCompositionTests(unittest.TestCase):
    """Cats_composition tests class."""
    @pytest.mark.remote_data
    def test_main(self):
        """Main function test."""
        file_name = 'temp/cat_1_fact.txt'
        if os.path.exists(file_name):
            os.remove(file_name)
        cat_processor = CatProcessor(
            fetch_cat_fact,
            fetch_cat_image,
            save_cat,
        )
        main(
            1,
            process_cat=cat_processor,
            show_information=print,  # noqa: T002
        )
        assert os.path.isfile(file_name)
        assert os.stat(file_name).st_size != 0

    def test_integration(self):
        """Test func."""
        format_str = 'python cats_composition.py {0}'  # noqa E800
        command_str = format_str.format('--count=1')
        assert subprocess.call(command_str, shell=True) == 0  # noqa: S602, E501


if __name__ == '__main__':
    unittest.main()
