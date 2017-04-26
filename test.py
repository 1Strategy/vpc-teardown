from teardown_default_route_tables import protected_resource
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_1(capfd):

    out, err = capfd.readouterr()
    assert protected_resource(['resource'], 'resource') == True, 'Something'


def test_2(capfd):

    out, err = capfd.readouterr()
    assert protected_resource(['resource'], 'resourc') == False, 'This is incorrect because, Something'


def test_3(capfd):

    out, err = capfd.readouterr()
    assert protected_resource(['resource'], '') == False


def test_4(capfd):

    out, err = capfd.readouterr()
    assert protected_resource(['resource', 'some_other_resource'], '') == False


def test_5(capfd):

    out, err = capfd.readouterr()
    assert protected_resource(['resource', 'some_other_resource'], 'resource') == True
