# Python red-black trees

[![Python application](https://github.com/emilydolson/python-red-black-trees/actions/workflows/python-app.yml/badge.svg)](https://github.com/emilydolson/python-red-black-trees/actions/workflows/python-app.yml) [![codecov](https://codecov.io/gh/emilydolson/python-red-black-trees/branch/main/graph/badge.svg?token=0LAOX0AEZY)](https://codecov.io/gh/emilydolson/python-red-black-trees)

A Python implementation of red-black trees. This code was originally copied from [programiz.com](https://www.programiz.com/dsa/red-black-tree), but I have made a few tweaks to improve the user interface. I have also fixed a hard-to-catch but serious bug in the original implementation (which has since been propogated to a number of tutorials on the internet), and added a rigorous testing suite to ensure there are no further bugs.

## What is this for?

I made this repo so that students in my algorithms class can try out red-black trees without needing to use C++. Feel free to use it for similar educational purposes! For more practical use-cases, you're probably better off using the [SortedContainers](http://www.grantjenks.com/docs/sortedcontainers/) library, which is more efficient, more scalable, and better maintained.


## Documentation

This data structure is designed to be used either as a standard red-black binary search tree or as a red-black tree backed dictionary.

### Standard red-black tree interface

#### Constructor

A new red-black tree can be constructed as follows:

```
bst = RedBlackTree()
```

#### Insert

Items can be inserted into a tree using the `insert` method:

```
bst.insert(5)  # inserts a node with value 5
```

#### Delete

Items can be removed from the tree using the `delete` method. This method will do nothing if
there is no item in the tree with the specific key.

```
bst.delete(5)  # removes a node with value 5
```

#### Minimum and maximum

The minimum and maximum value in the tree can be found with the corresponding methods. If the tree is empty, these methods will both return the special value `bst.TNULL`

```
bst.minimum()  # returns minimum value
bst.maximum()  # returns maximum value

bst.minimum() == bst.TNULL  # Check whether tree is empty
```

#### Tree size

Tree size can be accessed via the `size` member variable:

```
bst.size  # contains the tree's size
```

#### Search

To find a specific item in the tree, you can use the search method:

```
bst.search(6)  # returns the node containing 6. Will return bst.TNULL if item is not present.
```

#### Predecessor and successor

To get a node's predecessor or sucessor;

```
bst.predecessor(bst.search(6))  # Gets the predecessor a node containing 6
bst.successor(bst.search(6))  # Gets the successor a node containing 6

```

#### Printing methods

To know more about the contents of the tree, you can use various printing methods:

```
bst.print_tree()  # prints an ASCII representation of the whole tree
bst.preorder()      # prints a preorder traversal
bst.inorder()       # prints an inorder traveral
bst.postorder()     # prints a postorder traversal
```

### Dictionary interface

```
bst[80] = 4  # Store the value 4 with the key 80
bst[80]      # Retrieve the value associated with the key 80
```
