from bs4 import BeautifulSoup as bs
"""
Program for reading the xml file as a normal file and then passing it
into BeautifulSoup.
"""

content = []
# read the xml file
with open('sample.xml', 'r') as file:
    ## Finding tags by name ##
    print('_____________________________________\n')
    print('\tFinding tags by name\n')
    # read each line in file (sample.xml); readlines() returns a list of lines
    content = file.readlines()
    # combine lines in list into a string
    content = "".join(content)
    bs_content = bs(content, 'lxml')

    # returns first matching element in query.  If none, returns None
    result = bs_content.find('unique')
    print(f'\nwith find:\n{result}\n')

    # returns list of all child elements; if none found matching query, empty list returned
    result_all = bs_content.findAll('child')
    print(f'\nwith findAll:\n{result_all}\n')

    # returning the first child tag found in query with matching k:v pair (can be used with findAll as well)
    att_result = bs_content.find('child', {'name': 'Rose'})
    print(f'\nfinding tag with attribute:\n{att_result}\n')

    ## Finding tags by relationships (parent, child, or sibling) ##
    print('_____________________________________\n')
    print('    Finding tags by relationship\n')
    
    # Finding parent(s)
    print('Finding parent(s):\n')
    third_child = bs_content.find('child', {'name': 'Blue Ivy'})
    print(f'\nthird_child:\n{third_child}\n')

    find_parent = third_child.parent
    print(
        f'\nparent of third_child (and respective children):\n{find_parent}\n')

    # Finding children
    print('\nFinding children:\n')
    # returns children tags as a generator, so must be converted to a list
    find_children = list(third_child.children)
    print(
        f'\nchildren of third_child (and subsequent children):\n{find_children}\n')
    # NOTE: The children attribute doesn’t only return the children tags, it also returns the text in the reference tag.

    # Finding siblings
    print('\nFinding sibling(s):\n')
    # previous_siblings attribute will return the sibling tags before the reference tag
    # next_siblings attribute will return the sibling tags after it
    # both return generatos
    prev_siblings = list(third_child.previous_siblings)
    print(f'\nthird_child\'s previous sibling(s):\n{prev_siblings}\n')

    next_siblings = list(third_child.next_siblings)
    print(f'\nthird_child\'s next sibling(s):\n{next_siblings}\n')

    print('_____________________________________\n')
