from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("ParentNode must have a tag.")
        super().__init__(tag, children=children, props=props)
        if not hasattr(self, "children"):
            raise ValueError("ParentNode must have children.")
    
    def to_html(self):
        children_html = ""
        for child in self.children:
            children_html += "".join(child.to_html())           
            
        props_str = self.props_to_html()
        if props_str:
            return f"<{self.tag} {props_str}>{children_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{children_html}</{self.tag}>"
