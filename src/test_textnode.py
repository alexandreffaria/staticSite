import unittest

from textnode import *
from inline_markdown import *

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
                TextNode("bold", "bold"),
                TextNode(" text", "text")
            ]

            self.assertEqual(results, expected)


class TestMarkdownImageAndLinks(unittest.TestCase):
    def test_return_image(self):
        
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        tuples = extract_markdown_images(text)
        expected =  [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")]

        self.assertEqual(tuples, expected)

    def test_return_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        tuples = extract_markdown_links(text)
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]

        self.assertEqual(tuples, expected)

    def test_raise_error(self):
        text = "This is text with a link](https://www.example.com) and [another(https://www.example.com/another)"
        with self.assertRaises(Exception):
            extract_markdown_links(text)

        text = "This is text with an [image(https://i.imgur.com/zjjcJKZ.png) and another](https://i.imgur.com/dfsdkjfd.png)" 
        with self.assertRaises(Exception):
            extract_markdown_images(text)

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) bla bla bla",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", "text", None), 
            TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"), TextNode(" and another " , "text", None), 
            TextNode("second image", "image", "https://i.imgur.com/3elNhQu.png"), 
            TextNode(" bla bla bla", "text", None)
                    ]

        self.assertEqual(new_nodes, expected)

    def test_split_link(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png) bla bla bla",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with an ", "text", None), 
            TextNode("image", "link", "https://i.imgur.com/zjjcJKZ.png"), TextNode(" and another " , "text", None), 
            TextNode("second image", "link", "https://i.imgur.com/3elNhQu.png"), 
            TextNode(" bla bla bla", "text", None)
                    ]

        self.assertEqual(new_nodes, expected)



if __name__ == "__main__":
    unittest.main()