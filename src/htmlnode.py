class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def toHtml(self):
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