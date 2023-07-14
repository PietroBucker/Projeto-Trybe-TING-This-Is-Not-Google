from ting_file_management.priority_queue import PriorityQueue
import pytest

mock = {"qtd_linhas": 3}
mock2 = {"qtd_linhas": 5}
mock3 = {"qtd_linhas": 9}


def test_basic_priority_queueing():
    teste = PriorityQueue()
    teste.enqueue(mock)
    assert len(teste) == 1

    teste.dequeue()
    assert len(teste) == 0

    teste.enqueue(mock3)
    teste.enqueue(mock)
    teste.enqueue(mock2)

    assert teste.dequeue() == mock

    teste.enqueue(mock)
    assert teste.search(0) == mock
    assert teste.search(1) == mock3

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        teste.search(10)
