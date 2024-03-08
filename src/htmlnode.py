class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def toHTML(self):
        raise NotImplementedError("Subclass must implement this.")
    
    def propsToHTML(self):
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

    def toHTML(self):
        if self.value is None: 
            raise ValueError("Value cannot be None on a LeafNode")
        if self.tag is None: 
            return self.value
        else: 
            return f"<{self.tag}{super().propsToHTML()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"