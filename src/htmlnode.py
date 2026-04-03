class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value 
        self.children = children
        self.props = props

    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = " "
        for key in self.props:
            html_string += key
            html_string += self.props[key]
            html_string += " "

        return html_string
    
    def __repr__(self):
        return (f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}")
    
class LeafNode(HTMLNode):
    

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value

        html_string = ""

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return (f"tag: {self.tag}, value: {self.value}, props: {self.props}")


class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    
    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError
        
        html_string = ""

        html_string += f"<{self.tag}>"

        # iterate throught all child

        # recursively check if it's a parentNode
        # if so use it's to_html
        # actually 
        # leafNode and parentNode has different to_html
        # maybe we dont need to check 
        for child in self.children:
            html_string += child.to_html()
        
        html_string += f"</{self.tag}>"
        
        return html_string







    


    

