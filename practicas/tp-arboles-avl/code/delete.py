
def _delete_1(B, node):
  if node.parent == None:
    #
    B.root = None
  elif node.parent.leftnode == node:
    #
    node.parent.leftnode = None
  else:
    #
    node.parent.rightnode = None
  #
  return node.key
  
def _delete_2(B, node, rightValue):
  if node.parent == None:
    #
    if rightValue:
      B.root = B.root.rightnode
    else:
      B.root = B.root.leftnode
  elif node.parent.leftnode == node:
    #
    if rightValue:
      node.parent.leftnode = node.rightnode
    else:
      node.parent.leftnode = node.leftnode
  else:
    #
    if rightValue:
      node.parent.rightnode = node.rightnode
    else:
      node.parent.rightnode = node.leftnode
  #
  return node.key

def _search_menor_mayor(subNode):
  if subNode.leftnode == None:
    return subNode
  return _search_menor_mayor(subNode.leftnode)

def _delete_3(B, node):
  #
  if node.parent == None:
    subNode = _search_menor_mayor(node.rightnode)
    
    if subNode.parent.leftnode == subNode:
      subNode.parent.leftnode = None
    else:
      subNode.parent.rightnode = None

    B.root = subNode
    B.root.parent = None
    B.root.rightnode = node.rightnode
    B.root.leftnode = node.leftnode
  #
  else:
    subNode = _search_menor_mayor(node.rightnode)
    
    if subNode.parent.leftnode == subNode:
      if subNode.leftnode == None and subNode.rightnode == None:
        subNode.parent.leftnode = None
      elif subNode.leftnode != None:
        subNode.parent.leftnode = subNode.leftnode
      else:
        subNode.parent.leftnode = subNode.rightnode
    else:
      if subNode.leftnode == None and subNode.rightnode == None:
        subNode.parent.rightnode = None
      elif subNode.leftnode != None:
        subNode.parent.rightnode = subNode.leftnode
      else:
        subNode.parent.rightnode = subNode.rightnode

    subNode.parent = None
    subNode.rightnode = node.rightnode
    subNode.leftnode = node.leftnode
    
    if node.parent.leftnode == node:
      node.parent.leftnode = subNode
    else:
      node.parent.rightnode = subNode

  return node.key


def deleteREC(B, node, element):
  if node == None:
    return None

  if node.value == element:
    #
    if node.leftnode == None and node.rightnode == None:
      return _delete_1(B, node)
    #
    if node.leftnode != None and node.rightnode != None:
      return _delete_3(B, node)
    #
    if node.leftnode == None:
      return _delete_2(B, node, True)
    return _delete_2(B, node, False)
  
  leftKey = deleteREC(B, node.leftnode, element)

  if leftKey != None:
    return leftKey
  
  rightKey = deleteREC(B, node.rightnode, element)

  if rightKey != None:
    return rightKey