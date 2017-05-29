import pytest

pytestmark = pytest.mark.django_db


def test_pytest_running(mock_fixture):
    assert mock_fixture == 1
