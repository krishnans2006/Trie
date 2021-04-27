class Trie:
    def __init__(self):
        self.start = TrieElement("", None)

    def add(self, name):
        current = self.start
        if len(name) == 1:
            self.start.add(name)
            return
        for letter in name[:-1]:
            current = current.next(letter)
        current.add(name[-1])

    def delete(self, name):
        current = self.start
        for letter in name[:-1]:
            current = current.next(letter)
        current.delete(name[-1])

    def search(self, name):
        current = self.start
        for letter in name:
            current = current.next(letter)
            if not current:
                return False
        return True

    def autocomplete(self, name):
        current = self.start
        for letter in name:
            current = current.next(letter)
        return [n.name for n in current.next()]

    def display(self, current=None, level=0, special=False):
        if not current:
            current = self.start
            to_print = "The Current Trie:"
        else:
            if len(current.parent.children) < 2:
                to_print = " " + current.__repr__()
            else:
                to_print = " " * (level - 1) + "" + current.__repr__()
        if not current.has_children:
            to_print = " " + current.__repr__()
            if special:
                return "\n" + " " * (level - 1) + to_print
            else:
                return to_print
        else:
            for x, child in enumerate(current.children):
                if len(child.parent.children) > 1 and x != 0 and not child.parent == self.start:
                    to_print += self.display(child, level + 1, True)
                elif child.parent == self.start:
                    to_print += "\n" + self.display(child, level + 1)
                else:
                    to_print += self.display(child, level + 1)
            if special:
                return "\n" + " " * (level - 1) + to_print
            else:
                return to_print

    def __repr__(self):
        return self.display()



class TrieElement:
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.has_children = False
        self.parent = parent

    def get_arr(self):
        arr = [self.__repr__()]
        if self.has_children:
            for child in self.children:
                arr.append(child.get_arr())
        return arr

    def next(self, name=None):
        if not name:
            return self.children
        for child in self.children:
            if child.name == name:
                return child
        return None

    def add(self, name):
        if not self.has_children:
            self.has_children = True
        self.children.append(TrieElement(name, self))

    def delete(self, name):
        for x, child in enumerate(self.children):
            if child.name == name:
                del self.children[x]
        if len(self.children) < 1:
            self.has_children = False

    def __repr__(self):
        return self.name

if __name__ == "__main__":
    trie = Trie()
    trie.add("a")
    trie.add("b")
    trie.add("at")
    trie.add("al")
    trie.add("alt")
    trie.add("alte")
    trie.add("alter")
    trie.add("ate")
    trie.add("ar")
    trie.add("art")
    trie.add("are")
    trie.add("aren")
    trie.add("arent")
    trie.add("by")
    trie.add("bye")
    trie.add("bo")
    trie.add("bol")
    trie.add("bold")
    trie.delete("alt")
    print(trie)
