# -*- coding: utf-8 -*-

import subprocess  # noqa: S404
from cli import contains_entered, ls_entered
from cli import mk_entered, rm_entered, since_entered


def test_ls_entered(ls_fixture):
    """Tests for ls command."""
    assert ls_entered(ls_fixture[0]) == ls_fixture[1]


def test_mk_entered(mk_fixture):
    """Tests for mk command."""
    assert mk_entered(mk_fixture[0]) == mk_fixture[1]


def test_rm_entered(rm_fixture):
    """Tests for rm command."""
    assert rm_entered(rm_fixture[0]) == rm_fixture[1]


def test_contains_entered(contains_fixture):
    """Tests for contains command."""
    assert contains_entered(contains_fixture[0]) == contains_fixture[1]


def test_since_entered(since_fixture):
    """Tests for since command."""
    assert since_entered(
        since_fixture[0],
        since_fixture[1],
    ) == since_fixture[2]


def test_integration(integration_fixture):
    """Integration Tests."""
    command, parameter = integration_fixture
    callable_string = 'python students/Krokos1/3/cli.py {0} {1}'
    callable_string = callable_string.format(command, parameter)
    assert subprocess.call(callable_string, shell=True) == 0  # noqa: S602
