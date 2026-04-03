import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)
    
    def test_not_eq_text(self):
        node = TextNode("This is text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_default_url(self):
        node = TextNode("hello", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_noteq_url(self):
        node1 = TextNode("Click", TextType.LINK, "https://example.com")
        node2 = TextNode("Click", TextType.LINK, "https://other.com")
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = TextNode("hello", TextType.TEXT)
        self.assertEqual(repr(node), "TextNode(hello, text, None)")

    def test_eq_raises_for_non_textnode(self):
        node = TextNode("hello", TextType.TEXT)
        with self.assertRaises(AttributeError):
            _ = (node == "not a TextNode")


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_print(self):
        print("---------print_test____________")
        node = TextNode("this is img", TextType.IMAGE, "www.google.com")
        html_node = text_node_to_html_node(node)
        print(html_node)



if __name__ == "__main__":
    unittest.main()
