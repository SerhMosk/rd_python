import pytest

from task_2_func_summ_args import summ_args


def test_summ_args():
    assert summ_args(1, 2, 3, 4) == 10
    assert summ_args(1, 1, 1, 1, 1) == 5
    assert summ_args(0, 0) == 0
    assert summ_args(-1, 1) == 0


def test_summ_args_invalid_args():
    with pytest.raises(TypeError):
        assert summ_args(None, 0)
        assert summ_args('1', 0)
        assert summ_args((1, 2), 0)


if __name__ == '__main__':
    test_summ_args()
    test_summ_args_invalid_args()
