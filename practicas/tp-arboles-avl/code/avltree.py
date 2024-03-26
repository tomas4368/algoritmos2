from delete import deleteREC

class AVLTree:
  root = None
class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None

# sector eliminar 
def delete(B, element):  
  if B.root == None:
    return None

  return deleteREC(B, B.root, element)

# sector búsqueda
def _searchREC(node, element):
    if node == None:
      return None
    
    if node.value == element:
      return node.key
    
    leftKey = _searchREC(node.leftnode)

    if leftKey != None:
      return leftKey
    
    rightKey = _searchREC(node.rightnode)

    if rightKey != None:
      return rightKey

def search(B, element):
  
  if B.root == None:
    return None
  
  return _searchREC(B.root, element)

# sector insertar
def _insertREC(node, element, key):
  # Lado derecho
  if key > node.key:
    if node.rightnode == None:
      # Crear nodo 
      nodeAUX = AVLNode()
      nodeAUX.key = key
      nodeAUX.value = element
      nodeAUX.parent = node
      # Remplazar
      node.rightnode = nodeAUX
      # Calcular bf

      return key
    # Llamar recursividad derecha
    return _insertREC(node.rightnode, element, key)
  # Lado Izquierdo
  else:
    if node.leftnode == None:
      # Crear nodo 
      nodeAUX = AVLNode()
      nodeAUX.key = key
      nodeAUX.value = element
      nodeAUX.parent = node
      # Remplazar
      node.leftnode = nodeAUX
      # Calcular bf
      return key
    # Llamar recursividad izquierda
    return _insertREC(node.leftnode, element, key)

def insert(B, element, key):
  # Inserta en nodo root
  if B.root == None:
    nodeAUX = AVLNode()
    nodeAUX.key = key
    nodeAUX.value = element
    nodeAUX.parent = None
    B.root = nodeAUX
    return key
  # Llamar recursividad
  return _insertREC(B.root, element, key)


def rotateLeft(Tree,avlnode):
  # guardo la información
  node = avlnode
  antiguoNodeRight= avlnode.rightnode
  # limpio el hijo-derecho del avlnode
  avlnode.rightnode = None
  # agrego el hijo-derecho al avlnode (este seria el hijo-izquierdo del antiguo-node-derecho)
  avlnode.rightnode = antiguoNodeRight.leftnode
  # agrego al antiguo-node-derecho el avlnode modificado en el lado izquierdo
  antiguoNodeRight.leftnode = avlnode
  # cambio el padre de avlnode por antiguo-node-derecho
  avlnode.parent = antiguoNodeRight
  # cambio el padre antiguo-node-derecho
  if node.parent == None:
    # era raíz del árbol el avlnode
    antiguoNodeRight.parent = None
    Tree.root = antiguoNodeRight
  else:
    # el avlnode no era raíz del árbol
    if node.parent.leftnode == node:
      # esta en nodo izquierdo del padre
      node.parent.leftnode == antiguoNodeRight
      antiguoNodeRight.parent == node.parent
    else:
      # esta en nodo derecho del padre
      node.parent.rightnode == antiguoNodeRight
      antiguoNodeRight.parent == node.parent
  # devolver el árbol
  return Tree

def rotateRight(Tree,avlnode):
  # guardo la información
  node = avlnode
  antiguoNodeLeft= avlnode.leftnode
  # limpio el hijo-izquierdo del avlnode
  avlnode.leftnode = None
  # agrego el hijo-izquierdo al avlnode (este seria el hijo-derecho del antiguo-node-izquierdo)
  avlnode.leftnode = antiguoNodeLeft.rightnode
  # agrego al antiguo-node-derecho el avlnode modificado en el lado derecho
  antiguoNodeLeft.rightnode = avlnode
  # cambio el padre de avlnode por antiguo-node-izquierdo
  avlnode.parent = antiguoNodeLeft
  # cambio el padre antiguo-node-izquiedo
  if node.parent == None:
    # era raíz del árbol el avlnode
    antiguoNodeLeft.parent = None
    Tree.root = antiguoNodeLeft
  else:
    # el avlnode no era raíz del árbol
    if node.parent.leftnode == node:
      # esta en nodo izquierdo del padre
      node.parent.leftnode == antiguoNodeLeft
      antiguoNodeLeft.parent == node.parent
    else:
      # esta en nodo derecho del padre
      node.parent.rightnode == antiguoNodeLeft
      antiguoNodeLeft.parent == node.parent
  # devolver el árbol
  return Tree



def print_binary_tree(root, indent="", last=True):
    if root is not None:
        print(indent, end="")
        if last:
            print("└── ", end="")
            indent += "    "
        else:
            print("├── ", end="")
            indent += "│   "

        print(root.key)  # Puedes cambiar esto a root.value si deseas imprimir valores

        # Llama recursivamente a la función para los hijos izquierdo y derecho
        print_binary_tree(root.leftnode, indent, False)
        print_binary_tree(root.rightnode, indent, True)

# Ejemplo de uso:
# Supongamos que 'tree' es una instancia de la clase BinaryTree con su árbol binario correspondiente.
# Llamaríamos a la función de la siguiente manera:
# print_binary_tree(tree.root)


tree = AVLTree()
insert(tree, 7, 15)
insert(tree, 8, 6)
insert(tree, 9, 20)
insert(tree, 1, 3)
insert(tree, 5, 9)
insert(tree, 85, 18)
insert(tree, 55, 24)
insert(tree, 58, 1)
insert(tree, 598, 4)
insert(tree, 51, 7)
insert(tree, 52, 8)
insert(tree, 56, 12)
insert(tree, 59, 17)
print()
print_binary_tree(tree.root)