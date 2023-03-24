from rbtree import Node


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
    node.set_color("red")
    assert node.get_color() == "red"
    assert node.is_red()


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
    assert second_node.depth == 1
    
