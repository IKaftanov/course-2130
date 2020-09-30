import pytest
import json
import os


def pytest_addoption(parser):
    parser.addoption(
        "--hidden", action="store_true", default=False, help="run hidden tests"
    )


def pytest_configure(config):
    pytest.path_to_cases = 'hidden_cases.json' if config.getoption("--hidden") else 'cases.json'
    with open(os.path.join(os.path.dirname(__file__), pytest.path_to_cases), 'r', encoding="utf-8") as file:
        pytest.cases = json.load(file)


def pytest_generate_tests(metafunc):
    metafunc.parametrize('case', pytest.cases[metafunc.function.__name__.split('_')[-1]])
