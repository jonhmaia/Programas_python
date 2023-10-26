#include <iostream>
using namespace std;
// Definindo a estrutura do nó da A
struct Node
{
    int data;
    Node *left;
    Node *right;
};

// Função para criar um novo nó
Node *newNode(int data)
{
    Node *node = new Node;
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Função para inserir um novo nó na A
Node *insert(Node *root, int data)
{
    if (root == NULL)
    {
        return newNode(data);
    }
    if (data < root->data)
    {
        root->left = insert(root->left, data);
    }
    else if (data > root->data)
    {
        root->right = insert(root->right, data);
    }
    return root;
}

// Função para remover um nó da A
Node *removeNode(Node *root, int data)
{
    if (root == NULL)
    {
        return root;
    }
    // Se o dado a ser removido for menor que o dado da raiz, então ele está na subárvore esquerda
    if (data < root->data)
    {
        root->left = removeNode(root->left, data);
    }
    // Se o dado a ser removido for maior que o dado da raiz, então ele está na subárvore direita
    else if (data > root->data)
    {
        root->right = removeNode(root->right, data);
    }
    // Se o dado a ser removido for igual ao dado da raiz, então ele é o nó a ser removido
    else
    {
        // Se o nó não tiver filhos, então ele é removido
        if (root->left == NULL)
        {
            Node *temp = root->right;
            delete root;
            return temp;
        }
        // Se o nó tiver apenas um filho, então ele é removido e o filho toma seu lugar
        else if (root->right == NULL)
        {
            Node *temp = root->left;
            delete root;
            return temp;
        }
        Node *temp = root->right;
        // Encontrando o menor nó da subárvore direita
        while (temp->left != NULL)
        {
            temp = temp->left;
        }
        root->data = temp->data;
        // Removendo o nó
        root->right = removeNode(root->right, temp->data);
    }
    return root;
}

// Função para imprimir a A em notação prefixada
// a notação prefixada é feita para remover a raiz primeiro como se fosse uma lista
void preorder(Node *root)
{
    if (root != NULL)
    {
        cout << root->data << " ";
        preorder(root->left);
        preorder(root->right);
    }
}

// Função para imprimir a A em notação infixa
// a notação infixada é feita para remover a raiz no meio folha- filho- raiz- filho- folha
void inorder(Node *root)
{
    if (root != NULL)
    {
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right);
    }
}

// Função para imprimir a A em notação posfixada
// a notação posfixada é feita para remover a raiz por último como se fosse uma pilha
void postorder(Node *root)
{
    if (root != NULL)
    {
        postorder(root->left);
        postorder(root->right);
        cout << root->data << " ";
    }
}

// Função principal
int main()
{
    Node *root = NULL;
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 20);
    insert(root, 40);
    insert(root, 70);
    insert(root, 60);
    insert(root, 80);
    cout << "A em notacao prefixada: ";
    preorder(root);
    cout << endl;
    cout << "A em notacao infixa: ";
    inorder(root);
    cout << endl;
    cout << "A em notacao posfixada: ";
    postorder(root);
    cout << endl;
    removeNode(root, 20);
    cout << "Arvore em notacao infixa apos remocao do no 20: ";
    inorder(root);
    cout << endl;
    return 0;
}
