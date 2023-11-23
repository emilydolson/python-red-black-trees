import pytest
from rbtree import Node
from typing import Any


def test_constructor() -> None:
    node = Node(0)
    assert isinstance(node, Node)


def test_set_get_color() -> None:
    """
    I don't really care what the initial color is so I'm not going to
    mandate that with a test.
    """
    node = Node(0)
    node.set_color("black")
    assert node.get_color() == "black"
    assert node.is_black()
    assert not node.is_red()
    node.set_color("red")
    assert node.get_color() == "red"
    assert node.is_red()
    assert not node.is_black()


def test_not_null() -> None:
    """
    A null node is a special type of node.
    A node should not be null unless created as such.
    """
    node = Node(0)
    assert not node.is_null()


def test_depth() -> None:
    """
    Bad things can happen if users try to link nodes together outside of the
    tree, so do not do this at home.
    """
    node = Node(0)
    assert node.depth() == 0

    second_node = Node(1)
    second_node.parent = node
    node.left = second_node
    assert second_node.depth() == 1


def test_color_exception() -> None:
    node = Node(0)
    with pytest.raises(Exception):
        node.set_color("spam")


get_key_data = [-1, 0, 42]


@pytest.mark.parametrize("key", get_key_data)
def test_get_key(key: Any) -> None:
    node = Node(key)
    assert node.get_key() == key


def test_null_node() -> None:
    null = Node.null()
    assert null.is_null()
    assert null.is_black()


def test_repr() -> None:
    """
    Test:
    Key only
    Key/Value
    Null
    """
    node = Node(2)
    assert repr(node) == "Key: 2 Value: None"