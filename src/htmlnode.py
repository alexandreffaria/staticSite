class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclass must implement this.")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props = ""
        for key in self.props:
            props += f' {key}="{self.props[key]}"'
        return props
    
    def __repr__(self) -> str:
        return f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:

        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None: 
            raise ValueError("Value cannot be None on a LeafNode")
        if self.tag is None: 
            return self.value
        else: 
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None: 
            raise ValueError("Tag cannot be None on a LeafNode")
        if self.children is None: 
            raise ValueError("Can't be a parent without children")
        
        allHTML = f"<{self.tag}{super().props_to_html()}>"
        for child in self.children:
            if child.to_html():
                allHTML += child.to_html()

        allHTML += f"</{self.tag}>"

        return allHTML
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

