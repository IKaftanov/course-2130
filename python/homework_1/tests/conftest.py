import pytest
import json


def pytest_addoption(parser):
    parser.addoption(
        "--hidden", action="store_true", default=False, help="run hidden tests"
    )

def pytest_configure(config):
    pytest.path_to_cases = 'hidden_cases.json' if config.getoption("--hidden") else 'cases.json'


def pytest_generate_tests(metafunc):
    with open(f'tests\\{pytest.path_to_cases}', 'r', encoding="utf-8") as file:
        cases = json.load(file)
    metafunc.parametrize('case', cases[metafunc.function.__name__.split('_')[-1]])
