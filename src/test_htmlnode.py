import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def testEq(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("a", props=props)
        self.assertEqual(node.propsToHTML(), ' href="https://www.google.com" target="_blank"')

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.toHTML(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.toHTML(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()