import pytest
from answer import test


def add(x, y):
    return x + y


def test_example():
    # 測試邏輯
    assert 1 + 1 == 2, "測試失敗時的錯誤訊息"


def test_add():
    assert add(1, 2), '反為值應為兩數合'
