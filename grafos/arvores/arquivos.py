class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

    def __str__(self):
        return f"File: {self.name}"


class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, node):
        if node.name not in self.children:
            self.children[node.name] = node

    def __str__(self):
        return f"Directory: {self.name}"

    def list_content(self):
        return list(self.children.keys())

    def find(self, path):
        parts = path.split("/")
        if len(parts) == 1 and parts[0] in self.children:
            return self.children[parts[0]]
        if parts[0] not in self.children or not isinstance(self.children[parts[0]], Directory):
            return None
        return self.children[parts[0]].find("/".join(parts[1:]))

    def create_file(self, name, content=""):
        if name not in self.children:
            file = File(name, content)
            self.children[name] = file
        else:
            print(f"File '{name}' already exists.")

    def create_directory(self, name):
        if name not in self.children:
            directory = Directory(name)
            self.children[name] = directory
        else:
            print(f"Directory '{name}' already exists.")


class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def ls(self, path):
        node = self.root
        if path != "/":
            node = self.root.find(path)
        if node is None:
            return "Path not found."
        if isinstance(node, File):
            return str(node)
        return "\n".join(node.list_content())

    def cat(self, path):
        node = self.root.find(path)
        if node is None or not isinstance(node, File):
            return "File not found."
        return node.content

    def mkdir(self, path):
        parts = path.split("/")
        node = self.root
        for part in parts:
            if part:
                if not isinstance(node, Directory):
                    return "Invalid path."
                node.create_directory(part)
                node = node.find(part)

    def touch(self, path):
        parts = path.split("/")
        filename = parts[-1]
        directory = self.root.find("/".join(parts[:-1]))
        if directory is not None and isinstance(directory, Directory):
            directory.create_file(filename)

    def write(self, path, content):
        node = self.root.find(path)
        if node is None or not isinstance(node, File):
            return "File not found."
        node.content = content

# Exemplo de uso do sistema de arquivos
fs = FileSystem()

fs.mkdir("/home/user/documents")
fs.mkdir("/home/user/photos")
fs.touch("/home/user/documents/file1.txt")
fs.touch("/home/user/documents/file2.txt")
fs.touch("/home/user/photos/photo1.jpg")

fs.write("/home/user/documents/file1.txt", "Conteúdo do arquivo 1")
fs.write("/home/user/photos/photo1.jpg", "Conteúdo da foto 1")

print(fs.ls("/home/user"))
print(fs.ls("/home/user/documents"))
print(fs.cat("/home/user/documents/file1.txt"))
