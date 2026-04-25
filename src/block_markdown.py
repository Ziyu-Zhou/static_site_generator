from enum import Enum
import re
from htmlnode import ParentNode, LeafNode, HTMLNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"



def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    # print(blocks)

    # strip spaces
    for i in range(len(blocks)):
        # print(i)
        blocks[i] = blocks[i].strip()

    # cleans the ""
    cleaned = [x for x in blocks if x != ""]

    return cleaned


md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
blocks = markdown_to_blocks(md)


# region/block_to_block_type notes: 
# input: single block of markdown text 
# output: returns the BlockType

# endregion


def block_to_block_type(block):
    
    
    # header 
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    # code 
    if re.match(r"^```([\s\S]*?)```$", block):
        return BlockType.CODE
    
    # quote

    if re.match(r"^> ?.*", block):
        return BlockType.QUOTE
    
    # unordered list 
    if re.match(r"^- ", block, re.MULTILINE):

        return BlockType.ULIST
    
    # ordered list 

    lines = block.split("\n")
    ordered_list = True
    for i, line in enumerate(lines):
        expected_numer = i + 1
        if line.startswith(f"{expected_numer}. "):
            continue
        else:
            ordered_list = False
    
    if ordered_list:
        return BlockType.OLIST
    
    return BlockType.PARAGRAPH


# input = "## Hello"
# input = (
# "1. First item"
# "2. Second item"
# "3. Third item"
# "4. Fourth item"
# )


# result = block_to_block_type(input)
# print(result)

# helper functions 

# text process helper
# input raw text
# output child_node 
def text_to_children_node(text):

    text_nodes = text_to_textnodes(text)
    child_node = []
    for node in text_nodes:
        child_node.append(text_node_to_html_node(node))


    return child_node 

# header helper 

def header_helper(block):
    # input is a block of raw markdown 
    tag = ""
    text = ""
    syntax = block.strip().split(" ", 1)
    print(syntax)
    num = len(syntax[0])
    tag = f"h{num}"
    text = syntax[1]
    print(f"tag: {tag}, text: {text}")
    # returns the tag and text 
    # update: this function needs to return parent node instead
    # since the inline could be nested 
    
    child_node = text_to_children_node(text)


    return ParentNode(tag, child_node)

# quote helper 

def quote_helper(block):
    
    # split by \n 
    # quote is a mult line that start with "> "


    split = block.split("\n") # this should organize each line into a item in a list 
    cleaned_line = []
    for line in split:
        line = line[2:] # "> "
        cleaned_line.append(line)
    text = " ".join(cleaned_line)

    tag = "blockquote"

    children_node = text_to_children_node(text)

    # print(f"quote children_node: {children_node}")

    return ParentNode(tag, children_node)

# unorder list helper 
# input: block 
# process: 
# take in a block of multi-line list markdown
# each line has a "- " as syntax

# output: child_node

def unorder_list_helper(block):

    children_node = []
    list_item_node = []

    # block example:
    # 1. wake up
    # 2. drink coffee
    # 3. write code

    process_split = block.split("\n")

    # split = [1. wake up, 2. drink coffee, 3. write code]

    # take the syntax

    process_clean = [x[2:] for x in process_split]

    # clean = [wake up, drink coffee, write code]

    # print(process_clean)

    for item in process_clean:
        node = text_to_children_node(item)
        
        list_item_node.append(ParentNode("li",node))

    print("list item: ")
    print(list_item_node)

    return ParentNode("ul", list_item_node)


def order_list_helper(block):

    # copied from unorder_list
    children_node = []
    list_item_node = []

    # block example:
    # 1. wake up
    # 2. drink coffee
    # 3. write code

    process_split = block.split("\n")

    # split = [1. wake up, 2. drink coffee, 3. write code]

    # take the syntax

    process_clean = [x[3:] for x in process_split]

    # clean = [wake up, drink coffee, write code]

    # print(process_clean)

    for item in process_clean:
        node = text_to_children_node(item)
        
        list_item_node.append(ParentNode("li",node))

    print("list item: ")
    print(list_item_node)

    return ParentNode("ol", list_item_node)


def code_helper(block):

    process_strip = block[4:-3]
    # process_newline = block[]
    
    text = "".join(process_strip)
    # print(f"text: {text}")

    # print(f"process_strip: {process_strip}")

    text_node = TextNode(process_strip, TextType.CODE)
    html_node = text_node_to_html_node(text_node)

    return ParentNode("pre",[html_node])

def paragraph_helper(block):

    # copied from quote

    split = block.split("\n") # this should organize each line into a item in a list 
    cleaned_line = []
    for line in split:
        cleaned_line.append(line)
    text = " ".join(cleaned_line)

    tag = "p"

    children_node = text_to_children_node(text)

    # print(f"quote children_node: {children_node}")

    return ParentNode(tag, children_node)

def markdown_to_html_node(markdown):
    
    # 1.
    blocks = markdown_to_blocks(markdown)

    # 2. 
    # notes: syntax differ from block type because 
    # for example: HEADING doesn't tell use #, ## or ###

    # sample: 

    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)

        # extract syntax 
        
        # code here need to be able to 
        # 1. parse the header
        # 2. find a matched tag for this header
        # 3. extract text and process
        # 4. add to block_nodes 

        if block_type is BlockType.HEADING:
            node = header_helper(block)
            block_nodes.append(node)
        
        elif block_type is BlockType.QUOTE:
            node = quote_helper(block)

            block_nodes.append(node)
        
        elif block_type is BlockType.ULIST:
            node = unorder_list_helper(block)

            block_nodes.append(node)

        elif block_type is BlockType.OLIST:
            node = order_list_helper(block)

            block_nodes.append(node)

        elif block_type is BlockType.CODE:
            node = code_helper(block)

            block_nodes.append(node)
        
        else:
            node = paragraph_helper(block)

            block_nodes.append(node)
        
        
        
    
    # end of block loop 

    html_node = ParentNode("div", block_nodes)

    return html_node


# md = "> The only way to do great work is to love what you do.\n> If you haven't found it yet, keep looking.\n> Don't settle."

# md = "- apples\n- bananas\n- cherries"

md = """```
def greet(name):
    return f"Hello, {name}"
```"""



result = markdown_to_html_node(md)
# print(f"result: {result}")

print(f"result: {result.to_html()}")



