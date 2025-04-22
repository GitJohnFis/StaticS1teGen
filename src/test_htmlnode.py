import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Hello World!", None, {"class": "greeting", "href": "https://www.google.com","target": "_blank"}
        )
         self.assertEqual(
        node.props_to_html(),
        ' class="greeting" href="https://www.google.com" target="_blank"',
        )

    def test_values(self):
        node = HTMLNode("div", "I wish I could read",
        )
         self.assertEqual(
            node.tag,
            "div",
        )
         self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "what a strange world",
            None,
            {"class": "primary"},
        )
         self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, what a strange world, children: None,{'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild node])
        parent_node = ParentNode("div", [child node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal Text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold Text</b></p>Normal Text<i>Italic Text</i>Normal Text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal Text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold Text</b></p>Normal Text<i>Italic Text</i>Normal Text</h2>",
        )

    def test_to_html_mixed_children(self):
        node = ParentNode(
             "div",
            [
             LeafNode("span", "Text"),
             ParentNode(
                "p",
                [
                    LeafNode("a", "Link"),
                    LeafNode("b", "Bold Text"),
                    LeafNode("img", "Image"),
                    LeafNode("b", "Bold Text"),
                ],
            )  
        ]
    )
    self.assertEqual(
        node.to_html(),
        "<div><span>Text</span><p><a>Link</a><b>Bold Text</b><img>Image</img><b>Bold Text</b></p></div>",
    )

def test_to_html_with_props(self):
    parent_with_props = ParentNode(
        "div",
        [
            LeafNode("span", "Text"),         
        ], # add a comma here 
        {"class": "container", "id": "main"}  
    )
    self.assertEqual(
        parent_with_props.to_html(),
        '<div class="container" id="main"><span>Text</span></div>',
    )


   # test nested structures with multiple levels
    children_with_props = ParentNode(
        "ul",
        [
            LeafNode("li", "Item 1",
            {"class": "list-item"})
        ],
        complex_node = ParentNode(
            "div",
            [
                LeafNode("h1", "Title"),
                children_with_props,    
            ],
            {"id": "content"}
        )
        self.assertEqual(
            complex_node.to_html(),
            '<div id="content"><h1>Title</h1><ul><li class="list-item">Item 1</li></ul></div>',
        )
    )
if __name__ == "__main__":
    unittest.main()