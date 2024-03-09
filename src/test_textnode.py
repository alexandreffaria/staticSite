import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("Yoyo", "bold")
        node2 = TextNode("Yoyo", "bold")

        self.assertEqual(node, node2)

    def testNotEq(self):
        node = TextNode("Yo", "old")
        node2 = TextNode("Yoyo", "bold")

        self.assertNotEqual(node, node2)

    def testTextStyleNotEq(self):
        node = TextNode("Yoyo", "old")
        node2 = TextNode("Yoyo", "bold")

        self.assertNotEqual(node.text_type, node2.text_type)

    def testTextEq(self):
        node = TextNode("Yoyo", "old")
        node2 = TextNode("Yoyo", "bold")

        self.assertEqual(node.text, node2.text)

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_splitting_normal_text(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        result = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
             TextNode("This is text with a ", "text"),
             TextNode("code block", "code"),
             TextNode(" word", "text"),
        ]
        self.assertEqual(result, expected)

    def test_splitting_bold_text(self):
        node = TextNode("This is text with a **code block** word", text_type_text)
        result = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [
             TextNode("This is text with a ", "text"),
             TextNode("code block", "bold"),
             TextNode(" word", "text"),
        ]
        self.assertEqual(result, expected)

    def test_exception_on_missing_closing_delimiter(self):
        node = TextNode("This is text with a `code block", "text")
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", text_type_code)

    def test_multiple_node(self):
            nodes = [TextNode("This is text with a `code block` word", "text"), TextNode("**bold** text", "text")]

            results = split_nodes_delimiter(nodes, "`", text_type_code)
            results = split_nodes_delimiter(results, "**", text_type_bold)

            expected  = [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
                TextNode("i bet ", "text"),
                TextNode("bold", "bold"),
                TextNode(" text", "text")
            ]

            self.assertEqual(results, expected)



if __name__ == "__main__":
    unittest.main()