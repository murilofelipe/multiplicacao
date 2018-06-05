import pytest
from principal import multiplicar


def teste_multiplicar():
    assert multiplicar(2,3)== 6
    assert multiplicar(4, 3) == 12
    assert multiplicar(4, 4) == 16
    assert multiplicar(5, 7) == 37