class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return f'{self.data}'

class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = float(rating)

    def __str__(self):
        return f'{self.title}({self.rating})'

class AVLTree:
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        if not node:
            return -1
        return node.height

    def get_balance_factor(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def insert(self, root, movie):
        if not root:
            return Node(movie)
        
        if movie.rating < root.data.rating:
            root.left = self.insert(root.left, movie)
        else:
            root.right = self.insert(root.right, movie)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance_factor(root)

        if balance > 1 and self.get_balance_factor(root.left) >= 0:
            return self.rotate_right(root)
        if balance < -1 and self.get_balance_factor(root.right) <= 0:
            return self.rotate_left(root)
        if balance > 1 and self.get_balance_factor(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance_factor(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def removeMovie(self, movieName):
        movie_to_remove = self._find_movie_by_title(self.root, movieName)
        if movie_to_remove:
            self.root = self._remove_by_rating_and_title(self.root, movie_to_remove.rating, movie_to_remove.title)

    def _find_movie_by_title(self, node, movieName):
        if not node:
            return None
        
        if node.data.title == movieName:
            return node.data
        
        left_result = self._find_movie_by_title(node.left, movieName)
        if left_result:
            return left_result
            
        return self._find_movie_by_title(node.right, movieName)
    
    def _remove_by_rating_and_title(self, node, movieRating, movieTitle):
        if not node:
            return node
        
        if movieRating < node.data.rating:
            node.left = self._remove_by_rating_and_title(node.left, movieRating, movieTitle)
        elif movieRating > node.data.rating:
            node.right = self._remove_by_rating_and_title(node.right, movieRating, movieTitle)
        else:
            if node.data.title != movieTitle:
                node.right = self._remove_by_rating_and_title(node.right, movieRating, movieTitle)
                if not node:
                    return node
            else:
                if not node.left:
                    temp = node.right
                    node = None
                    return temp
                elif not node.right:
                    temp = node.left
                    node = None
                    return temp
                
                temp = self.getMin(node.right)
                node.data = temp.data
                node.right = self._remove_by_rating_and_title(node.right, temp.data.rating, temp.data.title)

        if not node:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance_factor(node)

        if balance > 1 and self.get_balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def top(self, number):
        return self._top(self.root, number)

    def _top(self, node, number: int):
        if node is None or number == 0:
            return []
        
        result = self.rev_in_order_traversal(node)
        return result[:number]
    
    def rev_in_order_traversal(self, root):
        if not root:
            return []
        
        return self.rev_in_order_traversal(root.right) + [root.data] + self.rev_in_order_traversal(root.left)

    def getRatingRange(self, start, end):
        return self._getRatingRange(self.root, start, end)

    def _getRatingRange(self, node, start, end):
        if node is None:
            return []

        result = []
        if node.data.rating >= start:
            result.extend(self._getRatingRange(node.left, start, end))
        
        if start <= node.data.rating <= end:
            result.append(node.data)
        
        if node.data.rating <= end:
            result.extend(self._getRatingRange(node.right, start, end))

        return result
    
    def insertMovie(self, movie):   
        self.root = self.insert(self.root, movie)
    
    def getMin(self, node): 
        current = node
        while current.left:
            current = current.left
        return current
    
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('    ' * level, node)
            self.printTree(node.left, level + 1)

    def isAVL(self):
        return self._isAVL(self.root)

    def _isAVL(self, node):
        if not node:
            return True
        balance = self.get_balance_factor(node)
        if abs(balance) > 1:
            return False
        return self._isAVL(node.left) and self._isAVL(node.right)
    
    def isBST(self):
        return self._isBST(self.root)

    def _isBST(self, node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True
        if not (min_val <= node.data.rating < max_val):
            return False
        return (self._isBST(node.left, min_val, node.data.rating) and
                      self._isBST(node.right, node.data.rating, max_val))

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

if __name__ == "__main__":
    rottenPotato = AVLTree()
    movies = [
        ("Megalodon", 5.0),
        ("Inception", 9.1),
        ("The_Dark_Knight", 8.9),
        ("Interstellar", 9.4),
        ("Tenet", 7.2),
        ("Memento", 7.9),
        ("Dunkirk", 7.7),
        ("The_Prestige", 8.3),
        ("Avatar", 7.8),
        ("Titanic", 8.1),
        ("Gladiator", 8.6),
        ("The_Matrix", 9.3),
        ("John_Wick", 7.5),
        ("Parasite", 9.0),
        ("Whiplash", 8.5),
        ("La_La_Land", 8.0),
        ("The_Godfather", 9.2),
        ("Pulp_Fiction", 8.4),
        ("Fight_Club", 8.7),
        ("Forrest_Gump", 8.8)
    ]

    for title, rating in movies:
        rottenPotato.insertMovie(Movie(title, rating))

    inp = input("The Requests From User: ").split(", ")
    for request in inp:
        req = request.strip().split(" ")
        if req[0] == "I":
            rottenPotato.insertMovie(Movie(req[1], float(req[2])))
        elif req[0] == "D":
            rottenPotato.removeMovie(req[1])
        elif req[0] == "T":
            print(f"Top {req[1]}")
            print([str(movie) for movie in rottenPotato.top(int(req[1]))])
            print()
        elif req[0] == "R":
            print(f'Rating range from {req[1]} to {req[2]}')
            print([str(movie) for movie in rottenPotato.getRatingRange(float(req[1]), float(req[2]))])
            print()
        elif req[0] == 'P':
            rottenPotato.printTree(rottenPotato.root)
    print(f'Is this AVL Tree? {rottenPotato.isAVL()}')
