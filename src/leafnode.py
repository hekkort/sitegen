from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError('LeafNode must have a value')
        elif self.tag == None:
            return self.tag
        
        return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
    def props_to_html(self):
        if self.props is not None:
            return ' '.join([f'{key}="{value}"' for key, value in self.props.items()])
        return ''
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    def __eq__(self, other):
        if isinstance(other, LeafNode):
            return self.tag == other.tag and self.value == other.value and self.props == other.props
        return False    