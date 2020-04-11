# -*- coding: utf-8 -*-

"""Conftest file homework 3."""
import pytest  # noqa I001
import os  # noqa I001


dot = '.'
directory = 'directory'
test_file = 'testFile.py'
name_py = 'name1.py'
date_time = '2017-01-03_02:02:02'


@pytest.fixture(params=[
    ('empty',
        [],
        [],
     ),
    ('dirsOnly',
        [directory],
        [directory],
     ),
    ('filesOnly',
        [test_file],
        [test_file],
     ),
    ('dirsAndFiles',
        [
            directory,
            test_file,
        ],
        [
            directory,
            test_file,
        ],
     ),
])
def ls_fixture(tmp_path, request):
    """Fixture for ls command."""
    param0 = request.param[0]
    path = tmp_path / param0
    path.mkdir()
    for name in request.param[1]:
        element = path / name
        if dot in request.param[1]:
            element.join()
        else:
            element.mkdir()
    yield (path, request.param[2])


@pytest.fixture(params=[
    (name_py, True),
    ('имя.py', True),
    ('conftest1.py', False),
    ('unable/.py', False),
])
def mk_fixture(request):
    """Fixture for mk command."""
    param0 = request.param[0]
    if param0 == 'conftest1.py':
        my_file = open(param0, 'w+')  # noqa WPS515
        my_file.close()
    yield request.param
    if os.path.isfile(param0):
        os.remove(param0)


@pytest.fixture(params=[
    (name_py, True),
    (directory, False),
    ('unable/.py', False),
])
def rm_fixture(tmp_path, request):
    """Fixture for rm command."""
    param0 = request.param[0]
    if dot in param0:
        try:  # noqa WPS229
            my_file = open(param0, 'w+')  # noqa WPS515
            my_file.close()
        except FileNotFoundError:
            pass  # noqa WPS420
    else:
        new_element = tmp_path / param0
        new_element.mkdir()
    yield request.param


@pytest.fixture(params=[
    ('conftest2.py', True),
    ('unable/.py', False),
    (directory, False),
])
def contains_fixture(tmp_path, request):
    """Fixture for contains command."""
    param0 = request.param[0]
    if dot not in param0:
        new_element = tmp_path / param0
        new_element.mkdir()
    elif param0 == 'conftest2.py':
        my_file = open(param0, 'w+')  # noqa WPS515
        my_file.close()
    yield request.param
    if os.path.isfile(param0):
        os.remove(param0)


@pytest.fixture(params=[
    ('empty',
        date_time,
        [],
        [],
     ),
    ('dirsOnly',
        date_time,
        [directory],
        [directory],
     ),
    ('filesOnly',
        date_time,
        [test_file],
        [test_file],
     ),
    ('dirsAndFiles',
        date_time,
        [
            directory,
            test_file,
        ],
        [
            test_file,
            directory,
        ],
     ),
    ('wrongDate',
        '20137-031-03_02:02:02',
        [test_file],
        'Use mask Y-M-D_H:M:S',
     )])
def since_fixture(tmp_path, request):
    """Fixture for since command."""
    param0 = request.param[0]
    path = tmp_path / param0
    path.mkdir()
    for name in request.param[2]:
        element = path / name
        if dot in request.param[2]:
            element.join()
        else:
            element.mkdir()
    yield (request.param[1], path, request.param[3])


@pytest.fixture(params=[
    ('ls', ''),
    ('mk', name_py),
    ('contains', name_py),
    ('since', date_time),
    ('rm', name_py),
])
def integration_fixture(request):
    """Fixture for integration tests."""
    yield request.param
