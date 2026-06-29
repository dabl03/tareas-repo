"""
Un arqueólogo digital ha encontrado un pergamino con una secuencia de símbolos astronómicos representados por números enteros positivos (códigos ASCII). Ha descubierto que el texto original se codificaba mediante un Árbol Binario de Búsqueda (ABB) desbalanceado mediante el siguiente proceso:

1. Se tomaba el texto original (cadena de caracteres)
2. Se calculaba el código ASCII de cada carácter
3. Se insertaban esos códigos en un ABB sin equilibrar, en el orden exacto del texto
4. Finalmente, se extraía el árbol en preorden y se guardó esa lista en el pergamino

---

Datos de entrada:

· Un entero N (cantidad de nodos del árbol, 1 ≤ N ≤ 10⁵)
· Una lista P de N números enteros (preorden del ABB, pueden tener duplicados que deben ignorarse)
· Un entero K (1 ≤ K ≤ N)

Salida requerida (3 valores):

1. Texto original: reconstruir el ABB y mostrarlo como cadena de caracteres (recorrido inorden → ASCII a caracter)
2. Altura del árbol: número de niveles (raíz = nivel 1)
3. Firma de Complejidad: recorrer el árbol en inorden, obtener la lista L, y encontrar la suma máxima de cualquier subarreglo contiguo de tamaño K en L

---
""";
def redondear(num:int):
    """Redondea hacia arriba un numero con un decimal de .5

    Args:
        num (int|float): Numero a redondear.

    Returns:
        int: Numero redondeado.
    """
    i_n=int(num);
    return i_n if num<i_n+0.5 else i_n+1;
def get_num_input(msg:str, min:int=None, max:int=None):
    """Obtiene un numero de la entrada del usuario verificando
    Si es valido y está en el rango solicitado.

    Args:
        msg (str): Mensaje para mostrar al usuario.
        min (int, optional): El numero minimo aceptable. Defaults to None.
        max (int, optional): El numero maximo aceptable. Defaults to None.

    Returns:
        int or float
    """
    while True:
        num=input(msg+"\n?> ");
        if num.isnumeric():
            num=int(num);
            if min!=None and num<min:
                print(f"Error: No se puede ingresar menos de {min}.");
                continue;
            if max!=None and num>max:
                print(f"Error: No se puede ingresar mas de {max}.");
                continue;
            return int(num);
        else:
            try:
                return float(num);
            except ValueError:
                pass
        print("Error: Solo se puede pasar numeros.\nIntentalo de nuevo.");

class Node():
    MODE_ORDEN="preorden";# @todo: Ver si convertirlo en atributo.
    def __init__(self, value, parentNode=None):
        self.value=value;
        self.parentNode=parentNode;
        self.leftNode=None;
        self.rightNode=None;        
    def __len__(self):
        return Node.get_size(self.leftNode)+Node.get_size(self.rightNode)+1;
    def __iter__(self):
        """Convierte el nodo binario en una lista.
        > Nota: Se decide el orden con la variable estatica Node.MODE_ORDEN

        Raises:
            ValueError: Node.MODE_ORDEN no tiene un valor tratado.

        Yields:
            list: Los valores del nodo.
        """;
        list_left=list(self.leftNode) if self.leftNode else [];
        list_right=list(self.rightNode) if self.rightNode else [];
        if Node.MODE_ORDEN=="preorden":
            yield self.value;
        elif Node.MODE_ORDEN=="postorden":
            list_right.append(self.value);
        elif Node.MODE_ORDEN=="inorden":
            list_left.append(self.value);
        else:
            raise ValueError("Node.MODE_ORDEN no tiene los valores soportados: (preorden, inorden, postorden).");
        for n in list_left:
            yield n;
        for n in list_right:
            yield n;
    def __str__(self):
        return f"Node({self.value}, {self.leftNode}, {self.rightNode}, {self.parentNode.value if self.parentNode!=None else None})";
    def get_top(node:Node):
        """Obtiene la altura del sub Arbol.

        Args:
            node (Node): Sub Arbol a medir.

        Returns:
            list: [Node, top]: [Hoja mas alta, altura de la hoja].
        """;
        if node==None: return [None, 0];
        left=Node.get_top(node.leftNode);
        right=Node.get_top(node.rightNode);
        mayor=[None, 0];
        mayor=left if left[1]>right[1] else right;
        if mayor[0]==None:
            if node.parentNode==None:
                mayor[0]=node;
            else:
                mayor[0]=[node.parentNode.leftNode, node.parentNode.rightNode];
        mayor[1]+=1;
        return mayor;
    # Orden de busqueda.
    def preorden(searchValue:int, node:Node):
        """Busca el valor en el Nodo en preorden.

        Args:
            searchValue (int): Valor a buscar.
            node (Node): Nodo en donde buscar.

        Returns:
            None|Node: El nodo conseguido, o None si no se consigue.
        """;
        if node==None: return None;
        if searchValue==node.value:
            return node;
        now=Node.preorden(searchValue, node.leftNode);
        if now!=None:
            return now;
        return Node.preorden(searchValue, node.rightNode);
    def inorden(searchValue:int, node:Node):
        """Busca el valor en el Nodo en inorden.

        Args:
            searchValue (int): Valor a buscar.
            node (Node): Nodo en donde buscar.

        Returns:
            None|Node: El nodo conseguido, o None si no se consigue.
        """;
        if node==None: return None;
        now=Node.inorden(searchValue, node.leftNode);
        if now!=None: return now;
        elif node.value==searchValue: return now;
        return Node.inorden(searchValue, node.rightNode);
    def postorden(searchValue:int, node:Node):
        """Busca el valor en el Nodo en postorden.

        Args:
            searchValue (int): Valor a buscar.
            node (Node): Nodo en donde buscar.

        Returns:
            None|Node: El nodo conseguido, o None si no se consigue.
        """;
        if node==None: return None;
        now=Node.postorden(searchValue, node.leftNode);
        if now!=None: return now;

        now=Node.postorden(searchValue, node.rightNode);
        if now!=None: return now;
        return node if node.value==searchValue else None;
    def get_size(node:Node):
        """Obtiene la cantidad de nodo que hay.

        Args:
            node (Node): El nodo a medir.

        Returns:
            int: Cantidad de nodos.
        """
        if node==None: return 0;
        size_left=Node.get_size(node.leftNode);
        rightNode=Node.get_size(node.rightNode);
        return 1+size_left+rightNode;

class RootTree():
    
    ORDEN={
        "preorden":Node.preorden,
        "postorden":Node.postorden,
        "inorden":Node.inorden
    };

    def __init__(self, valueRoot=None):
        self.rootNode=None;
        if valueRoot!=None: self.setRoot(valueRoot);

    def setRoot(self, value):
        self.rootNode=Node(value);
    def searchNode(self, searchValue:int, NowNode=None, orden:str="preorden"):
        """Verifica el tipo de busqueda pedido y llama a la función pedida.

        Args:
            searchValue (int): El valor a buscar en los nodos.
            NowNode (Node, optional): El siguiente a buscar. Defaults to None para usar rootNode.
            orden (str, optional): Tipo de busqueda. Defaults to "preorden". Nota: solo puede pasar lo siguiente:
                - "preorden": Busca el valor desde el nodo actual y despues los hijos.
                - "postorden": Busca el valor desde los hijos y despues el actual.
                - "inorden": Busca primero de hijo izquierdo, nodo actual y finalmente en hijo derecho.

        Returns:
            None: No se ha conseguido el valor.
            Node: El nodo con el valor buscado.
        """
        if NowNode==None: NowNode=self.rootNode;
        orden=orden.lower();
        available_ord=RootTree.ORDEN.keys();
        if orden in available_ord:
            return RootTree.ORDEN[orden](searchValue, NowNode);
        else:
            raise ValueError(f"Solo se puede pasar: {', '.join(available_ord)}.");

    def putLeft(self, parentNode, value:int, is_insert_mode=False, orden:str="preorden"):
        """Agrega un valor a la izquierda en el nodo con el valor parentNode.

        Args:
            parentNode (int): Nodo a buscar.
            value (int): Valor para agregar.
            is_insert_mode (bool, optional): Indica si ignorar el nodo si tiene hijo o no. Defaults to False.
            orden (str, optinal): El orden usado para buscar el padre del nuevo nodo.
                > Nota: Ver la funcion searchNode para mas info.
        Returns:
            Bool: Se pudo agregar?
        """;
        node=self.searchNode(parentNode, orden=orden);
        if node==None: return False;
        if node.leftNode:
            node.leftNode.value=value if is_insert_mode else node.leftNode.value;
        else:
            node.leftNode=Node(value, node);
        return True;
    def putRight(self, parentNode, value, is_insert_mode=False, orden:str="preorden"):
        """Agrega un valor a la derecha en el nodo con el valor parentNode.

        Args:
            parentNode (int): Nodo a buscar.
            value (int): Valor para agregar.
            is_insert_mode (bool, optional): Indica si ignorar el nodo si tiene hijo o no. Defaults to False.
            orden (str, optinal): El orden usado para buscar el padre del nuevo nodo.
                > Nota: Ver la funcion searchNode para mas info.
        Returns:
            Bool: Se pudo agregar?
        """;
        node=self.searchNode(parentNode, orden=orden);
        if node==None:# No se encuentra.
            return False;
        if node.rightNode:
            if is_insert_mode: node.rightNode.value=value;
        else:
            node.rightNode=Node(value, node);
        return True;
    def putChildren(self, parentNode, valueLeft=None, valueRight=None, is_insert_mode=False, orden:str="preorden"):
        """Agrega agrega los valores a los hijos del nodo parentNode.

        Args:
            parentNode (int): Nodo a buscar.
            valueLeft, valueRight (int, optional): Valor de los hijos del nodo.
            is_insert_mode (bool, optional): Indica si ignorar el nodo si tiene hijo o no. Defaults to False.
            orden (str, optinal): El orden usado para buscar el padre del nuevo nodo.
                > Nota: Ver la funcion searchNode para mas info.
        Returns:
            Bool: Se pudo agregar?
        """;
        node=self.searchNode(parentNode);
        if node==None or (valueLeft==None and valueRight==None):
            return False;# No se ha pasado valor...
        if valueLeft!=None:
            if node.leftNode==None:# Se crea uno nuevo.
                node.leftNode=Node(valueLeft, node);
            else:#Existe y insertmode es true, se reemplaza valor.
                if is_insert_mode: node.leftNode.value=valueLeft;
        if valueRight!=None:
            if node.rightNode==None:
                node.rightNode=Node(valueRight, node);
            else:
                if is_insert_mode: node.rightNode.value=valueRight;
        return True;
    def removeNode(self, node:Node):
        """Elimina el nodo pasado y sus sub nodos.

        Args:
            node (Node): Nodo a eliminar.
        """;
        if node.parentNode==None:
            self.rootNode=None;
            return;
        tmp=node.parentNode;
        if node==tmp.leftNode:
            tmp.leftNode=None;
        else:
            tmp.rightNode=None;
        del node;
    def draw(self, node:Node=None, chr:str=' '):
        """Retorna una cadena identada del arbol binario.
        Args:
            node (Node, optional): Nodo actual. Defaults to None para nodo raiz.
        
        Returns:
            str|None: Cadena formateada.
        """;
        if node==None:
            node=self.rootNode;
            if not node:
                return None;
        str_tree=str(node);
        len_=len(str_tree);
        out=[chr for chr in str_tree];
        level=0;
        return str_tree;
        for i in range(len_):
            if level>0:
                # Al inicio no queremos identación.
                if str_tree[i]=='(':
                    out[i]="(\n"+('    '*level);
                    level+=1;
                    continue;
                elif str_tree[i]==')':
                    level-=1;
                    if level<0:
                        raise NotImplementedError("Ha ocurrido un error en la implementacion __str__() de la clase Node().");
                    out[i]=(' '*level)+")\n";
                    continue;
        if out[-1]=='\n':
            out[-1]='';
        return ''.join(out);
    def searchInput(binTree:RootTree, node:Node):
        """Facilita la busqueda al usuario por consola.

        Args:
            binTree (RootTree): El arbol en donde buscar.
            node (Node): En caso de que el usuario quiera buscar desde el nodo actual.
        
        Returns:
            Node|None: Nodo conseguido.
        """;
        PREORDEN=("pr", "preorden");
        POSTORDEN=("po", "postorden");
        INORDEN=("io", "inorden");
        num=int(get_num_input("Ingrese el valor a buscar en los nodos:"));
        type_=PREORDEN[0];
        HELP=f"""Ingrese el tipo de busqueda que desea realizar:
    - {', '.join(PREORDEN)}: Para verificar el valor de los padres, antes de los hijos.
    - {', '.join(INORDEN)}: Para buscar primero el hijo izquierdo, padre he hijo derecho.
    - {', '.join(POSTORDEN)}: Para buscar en los hijos antes de los padres.
Nota: Dejar vacio para preorden.""";
        
        print("Buscador de elemento...");
        while True:
            print(HELP);
            io=input("?> ").lower();
            if not io.split(): break;
            elif io in PREORDEN or io in POSTORDEN or io in INORDEN:
                type_=io;
                break;
        is_now_node=False;
        while True:
            io=input("¿Deseas buscar desde este nodo? (yes, no)\n?> ");
            if io in ('y', 'yes'): is_now_node=True;
            elif io in ('n', "no"): is_now_node=False;
            else: continue;
            break;
        for i in (PREORDEN, POSTORDEN, INORDEN):
            if type_==i[0]:
                type_=i[1];
                break;
        tmp_node=binTree.searchNode(num, None if not is_now_node else node, orden=type_);
        if tmp_node==None: return None;
        return tmp_node;

    def inputToBinTree(max_node:int=1, binTree:RootTree=None):
        """Facilita la creación de un nuevo arbol binario al usuario
        Por consola.

        Args:
            max_node (int, optional): Maximos nodos que debe existir.
            binTree (RootTree, optional): Arbol a sobreescribir. Default None: Crea uno nuevo.

        Raises:
            ValueError: max_node <1

        Returns:
            RooTree: Arbol creado o modificado.
        """;
        if max_node<1:
            raise ValueError("max_node no debe ser menor a 1.");
        SALIR=("t", "terminar", "s", "salir");
        HELP=("m", "menu", "h", "help");
        LEFT=("i", "izquierdo");
        RIGHT=("d", "derecho");
        BACK=("a", "atras", "b", "back");
        SEARCH=("e", "encontrar", "s", "search");
        REMOVE=('r', "remove", 'd', "deleted");
        MENU=f"""Estos son los siguientes comandos para rellenar el arbol binario.
    - Cualquier numero para agregar el valor.
    - {', '.join(LEFT)}: Para el nodo izquierdo.
    - {', '.join(RIGHT)}: para nodo derecho.
    - {', '.join(BACK)}: Para ir al nodo padre.
    - {', '.join(SALIR)}: Para acabar de agregar los datos.
    - {', '.join(HELP)}: Para este menu de ayuda.
    - {', '.join(SEARCH)}: Para buscar un número en el arbol. Nota: search no recoge parametro.
        . Uso incorrecto: "search 4 pr no" es incorrecto porque search no buscara el 4,
            pero al terminar de ejecutarse sobreescribirá el valor que encuentre por el 4.
        . Uso correcto(despues seguir indicaciones claro): search
    - {', '.join(REMOVE)}: Para eliminar el nodo.
        Ejemplo: 10 d 30 i 10 d 30 t""";
        opt=[HELP[0]];
        binTree=RootTree(0) if binTree==None else binTree;
        node=binTree.rootNode;
        node.value=f"*{node.value}";
        is_exit=False;
        level=1;
        while True:
            have_help=False;
            float_avertencia=False;
            max_limit_advertencia=False;
            len_=len(binTree.rootNode);
            for o in opt:
                if o in HELP:
                    if not have_help:
                        # No saturar de ayudas.
                        print(MENU);
                        have_help=True;
                elif o in LEFT or o in RIGHT:
                    #@todo usar longitud aqui da error cuando se supera corregirlo.
                    msg="Advertencia: Has alcanzado el maximo de nodos.";
                    is_error=len_+1>max_node;

                    nowNode=Node(0, node) if not is_error else None;
                    node.value=int(node.value[1:]);
                    selected=None;
                    if o in LEFT:
                        if not node.leftNode:
                            node.leftNode=nowNode;
                        selected=node.leftNode;
                    else:
                        if not node.rightNode:
                            node.rightNode=nowNode;
                        selected=node.rightNode;
                    if selected==None:
                        selected=node;
                        level-=1;
                        if not max_limit_advertencia:
                            print(msg);
                            max_limit_advertencia=True;
                    node=selected;
                    node.value=f"*{node.value}";
                    level+=1;
                elif o in BACK:
                    if node.parentNode!=None:# No usar and con el if anterior.
                        node.value=int(node.value[1:]);
                        node=node.parentNode;
                        node.value=f"*{node.value}";
                        level-=1;
                elif o in SEARCH:
                    node.value=int(node.value[1:]);
                    tmp=RootTree.searchInput(binTree, node);
                    if tmp==None:
                        node.value=f"*{node.value}";
                        print("Error: No se ha encontrado el elemento.");
                        continue;
                    else:
                        tmp.value=f"*{tmp.value}";
                        node=tmp;
                    n=tmp.parentNode;
                    level=1;
                    while n!=None:
                        level+=1;
                        n=n.parentNode;
                elif o in REMOVE:
                    tmp=node.parentNode;
                    binTree.removeNode(node);
                    if tmp==None:
                        binTree.setRoot(0);
                        tmp=binTree.rootNode;
                    node=tmp;
                    node.value=f"*{node.value}";
                elif o in SALIR:
                    node.value=int(node.value[1:]);
                    is_exit=True;
                else:
                    if o.isnumeric():
                        node.value=f"*{o}";
                    else:
                        try:
                            node.value=f"*{int(float(o))}";
                            if not float_avertencia: print("Advertencia: Se ignoran los decimales.");
                        except ValueError:
                            print(f"Error: No se reconoce comando.\nIngresar una de las siguientes opciones {', '.join(HELP)} para ver los comandos disponibles.");
            if is_exit: break;
            print(binTree.rootNode);
            print(f"Nodo Padre: {node.parentNode.value if node.parentNode!=None else 'No tiene'} | Longitud del arbol: {len_}/{max_node} | Altura actual: {level}/{Node.get_top(binTree.rootNode)[1]}");
            print(f"Nodo actual: {node.value} | Hijo Izq: {node.leftNode.value if node.leftNode!=None else 'No tiene'} | Hijo Der: {node.rightNode.value if node.rightNode!=None else 'No tiene'}");
            opt=input("?> ").lower().split();
        return binTree;
    def test():
        binTree=RootTree(10);
        root=binTree.searchNode(10);
        binTree.putLeft(10, 40, is_insert_mode=True);
        binTree.putRight(10, 50, is_insert_mode=True);
        binTree.putLeft(40, 30);
        binTree.putRight(40, 30);
        binTree.putChildren(30, 11, 30, orden="postorden");
        binTree.putChildren(11, 11, 30, orden="postorden");
        binTree.putChildren(50, 11, 30);
        print("El nodo completo:");
        print(binTree.rootNode);
        print("El arbol:");
        out=binTree.draw();
        print(out);
        print("La longitud del arbol es: "+str(len(binTree.rootNode)));
        
        print(f"Lista en preorden del arbol: {list(binTree.rootNode)}");
        Node.MODE_ORDEN="inorden";
        print(f"Lista en inorden del arbol: {list(binTree.rootNode)}");
        Node.MODE_ORDEN="postorden";
        print(f"Lista en postorden del arbol: {list(binTree.rootNode)}");
        
        top=Node.get_top(binTree.rootNode);
        print(f"El nodo con la altura maxima es: {str(top[0][0])}, {str(top[0][1])}.");
        print(f"La altura del nodo: {top[1]}");

        Node.MODE_ORDEN="preorden";
        print(f"Nodo original:\n {binTree.rootNode}");
        print(list(binTree.rootNode));
        binTree.removeNode(binTree.searchNode(30));
        print(f"Nodo copia:\n {binTree.rootNode}");
        print(list(binTree.rootNode));
        print("Longitud: "+str(len(binTree.rootNode)));

if __name__=="__main__":
    print("Decodificador de símbolos astronómicos.");
    print("Hecho por Dabl03.");
    max_node=int(
        get_num_input("Porfavor ingresar la cantidad de nodos del arbol.", min=1, max=10**5)
    );
    k=int(
        get_num_input("Porfavor ingresar la maxima cantidad de valores para la sub lista.", min=1, max=max_node)
    );
    count_node=0;
    binTree=RootTree.inputToBinTree(max_node);
    n=len(binTree.rootNode);
    Node.MODE_ORDEN="inorden";
    msg_d=list(binTree.rootNode);
    len_msg=len(msg_d);
    msg=list(range(len_msg));
    for i in range(len_msg):
        msg[i]=chr(msg_d[i]);
    print(f"El mensaje es: {''.join(msg)}");
    print(f"La altura del arbol es: {Node.get_top(binTree.rootNode)[1]}.");
    print("La complejidad del arbol binario por cada sub arreglo te tamaño k es:");
    now=0;
    sum=0;
    for i in range(len_msg):
        now+=1;
        sum+=msg_d[i];
        if now==k:
            print(f" - {sum}");
            sum=0;
            now=0;
"""
Salida requerida (3 valores):

3. Firma de Complejidad: recorrer el árbol en inorden, obtener la lista L, y encontrar
la suma máxima de cualquier subarreglo contiguo de tamaño K en L
""";
