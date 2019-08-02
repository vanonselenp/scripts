#  """
#  /*
#  * Write a function that builds a string prefix tree from a flat list' -- i.e., if it gets called with ['a', 'a.b', 'a.c', 'a.b.c'] it should return:
#  * 
#  * {
#  *   value: "a",
#  *   children: [
#  *     {
#  *       value: "a.b",
#  *       children: [
#  *         {
#  *           value: "a.b.c"
#  *         }
#  *       ]
#  *     },
#  *     {
#  *       value: "a.c"
#  *     }
#  *   ]
#  * }
#  */
#  """

flat_list = ['a', 'a.b', 'a.c', 'a.b.c']


def create_tree_node(value, c=[]):
    return {
        'value': value,
        'children': c
    }


def parse(items):
    root = None

    for item in items:
        if root is None:
            root = create_tree_node(item)
        else:
            root = insert_into_tree(root, item)
            
    return root


def insert_into_tree(node, item):
    print node, item
    # parent
    if node['value'].startswith(item):
        return create_tree_node(item, [node])

    if item.startswith(node['value']):
        #child
        if node['children'] == []:
            node['children'].append(create_tree_node(item, []))
        
        else:
            found = False
            for child in node['children']:
                if item.startswith(child['value']):
                    found = True
                    child = insert_into_tree(child, item)
            
            #sibling
            if not found:
                node['children'].append(create_tree_node(item))

    return node

if __name__ == '__main__':
        root = parse(flat_list)
        print "---"
        print root