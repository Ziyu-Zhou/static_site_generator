import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    # def test_eq(self):
    #     node = TextNode("This is a text node", TextType.BOLD)
    #     node2 = TextNode("This is a text node", TextType.BOLD)
    #     self.assertEqual(node, node2)


    # def test_print(self):
    #     print("-------print test for split------------")
    #     node = TextNode("This is text with a `code block` word", TextType.TEXT)
    #     new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    #     print(new_nodes)

    #     print()
    #     print()
    pass





if __name__ == "__main__":
    unittest.main()