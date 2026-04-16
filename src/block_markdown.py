from enum import Enum
import re

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












input = "## Hello"
input = (
"1. First item"
"2. Second item"
"3. Third item"
"4. Fourth item"
)


result = block_to_block_type(input)
# print(result)



