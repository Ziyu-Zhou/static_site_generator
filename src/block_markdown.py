from enum import Enum
import re
from htmlnode import ParentNode, LeafNode, HTMLNode

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

# header helper 

def header_helper(markdown):
    
    # input is a block of raw markdown 
    tag = ""
    text = ""
    syntax = markdown.strip().split(" ", 1)
    print(syntax)
    num = len(syntax[0])
    tag = f"h{num}"
    text = syntax[1]
    print(f"tag: {tag}, text: {text}")
    # returns the tag and text 
    return tag, text


def markdown_to_html_node(markdown):
    
    # 1.
    blocks = markdown_to_blocks(markdown)

    # 2. 
    # notes: syntax differ from block type because 
    # for example: HEADING doesn't tell use #, ## or ###

    # sample: 
    for block in blocks:
        block_type = block_to_block_type(block)

        # extract syntax 
        
        # code here need to be able to 
        # 1. parse the header
        # 2. find a matched tag for this header
        # 3. 

        if block_type is BlockType.HEADING:
            tag, text = header_helper(block)
            child_text_node = TextNode(text, TextType.TEXT)
            child_node = text_node_to_html_node(child_text_node)
            return ParentNode(tag, [child_node]).to_html()
            

        # extract text


input = """# My Adventure

This is a **bold** tale of _courage_.

- Found a sword
- Slew a dragon
"""
result = markdown_to_html_node(input)
print(f"result: {result}")

