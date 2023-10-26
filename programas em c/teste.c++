#include <iostream>
using namespace std;

// Definindo a estrutura do nó da árvore
struct Node {
    //aqui a data vai ser a struct com os atributos dos itens
    // pensei na lógica de se o item tiver mais defesa ele vai pra esquerda se estiver mais ataque ele vai pra direita
    int data;
    Node* left;
    Node* right;
};

// Função para criar um novo nó
Node* newNode(int data) {
    Node* node = new Node;
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Função para inserir um novo nó na árvore
Node* insert(Node* root, int data) {
    if (root == NULL) {
        return newNode(data);
    }
    if (data < root->data) {
        root->left = insert(root->left, data);
    }
    else if (data > root->data) {
        root->right = insert(root->right, data);
    }
    return root;
}

// Função para imprimir a árvore em ordem
void inorder(Node* root) {
    if (root != NULL) {
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right);
    }
}

// Função principal
int main() {
    Node* root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
    inorder(root);
    return 0;
}
