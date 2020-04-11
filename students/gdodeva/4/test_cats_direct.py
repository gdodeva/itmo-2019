# -*- coding: utf-8 -*-

import os
import subprocess  # noqa S404
import unittest
import pytest
import cats_direct


class CatsDirectTester(unittest.TestCase):  # noqa WPS230
    """Tests for cats_direct."""

    def test_parser(self):
        """Create_parser function test."""
        parsed = cats_direct.create_parser().parse_args(['--count', '1'])
        assert parsed.count == 1

    @pytest.mark.remote_data
    def test_fetch_cat_fact(self):
        """Fetch_cat_fact function test."""
        fact = cats_direct.fetch_cat_fact()
        assert fact != ''

    @pytest.mark.remote_data
    def test_fetch_cat_image(self):
        """Fetch_cat_image function test."""
        img_info = cats_direct.fetch_cat_image()
        assert len(img_info[0]) > 2
        assert int(img_info[1].headers['Content-length']) != 0

    def test_save_cat(self):
        """Save_cat function test."""
        assert os.path.isfile('image.jpg')
        with open('image.jpg', 'rb') as img:
            cats_direct.save_cat(
                index=1,
                fact='cats are great',
                image=('jpg', img),
            )
        assert os.path.isfile('temp/cat_1_image.jpg')
        with open('temp/cat_1_fact.txt', 'r') as facts:
            assert facts.read() == 'cats are great'

    def test_integration(self):
        """Integration test."""
        callable_string = 'python cats_direct.py {0}'  # noqa E800
        callable_string = callable_string.format('--count=1')
        assert subprocess.call(callable_string, shell=True) == 0  # noqa: S602, E501


if __name__ == '__main__':
    unittest.main()
