#include <iostream>
#include <list>
#include <stack>
#define NIL -1
using namespace std;

// A class that represents
// an directed graph
class Graph {
    // No. of vertices
    int V;

    // A dynamic array of adjacency lists
    list<int>* adj;

    // A Recursive DFS based function
    // used by SCC()
    void SCCUtil(int u, int disc[],
                 int low[], stack<int>* st,
                 bool stackMember[]);

public:
    // Member functions
    Graph(int V);
    void addEdge(int v, int w);
    void SCC();
};

// Constructor
Graph::Graph(int V) {
    this->V = V;
    adj = new list<int>[V];
}

// Function to add an edge to the graph
void Graph::addEdge(int v, int w) {
    adj[v].push_back(w);
}

// Recursive function to finds the SCC
// using DFS traversal
void Graph::SCCUtil(int u, int disc[],
                    int low[], stack<int>* st,
                    bool stackMember[]) {
    static int time = 0;

    // Initialize discovery time
    // and low value
    disc[u] = low[u] = ++time;
    st->push(u);
    stackMember[u] = true;

    // Go through all vertices
    // adjacent to this
    list<int>::iterator i;

    for (i = adj[u].begin();
         i != adj[u].end(); ++i) {
        // v is current adjacent of 'u'
        int v = *i;

        // If v is not visited yet,
        // then recur for it
        if (disc[v] == -1) {
            SCCUtil(v, disc, low,
                    st, stackMember);

            // Check if the subtree rooted
            // with 'v' has connection to
            // one of the ancestors of 'u'
            low[u] = min(low[u], low[v]);
        }

        // Update low value of 'u' only of
        // 'v' is still in stack
        else if (stackMember[v] == true)
            low[u] = min(low[u], disc[v]);
    }

    // head node found, pop the stack
    // and print an SCC

    // Store stack extracted vertices
    int w = 0;

    // If low[u] and disc[u]
    if (low[u] == disc[u]) {
        // Until stack st is empty
        while (st->top() != u) {
            w = (int)st->top();

            // Print the node
            cout << w << " ";
            stackMember[w] = false;
            st->pop();
        }
        w = (int)st->top();
        cout << w << "\n";
        stackMember[w] = false;
        st->pop();
    }
}

// Function to find the SCC in the graph
void Graph::SCC() {
    // Stores the discovery times of
    // the nodes
    int* disc = new int[V];

    // Stores the nodes with least
    // discovery time
    int* low = new int[V];

    // Checks whether a node is in
    // the stack or not
    bool* stackMember = new bool[V];

    // Stores all the connected ancestors
    stack<int>* st = new stack<int>();

    // Initialize disc and low,
    // and stackMember arrays
    for (int i = 0; i < V; i++) {
        disc[i] = NIL;
        low[i] = NIL;
        stackMember[i] = false;
    }

    // Recursive helper function to
    // find the SCC in DFS tree with
    // vertex 'i'
    for (int i = 0; i < V; i++) {

        // If current node is not
        // yet visited
        if (disc[i] == NIL) {
            SCCUtil(i, disc, low,
                    st, stackMember);
        }
    }
}

// Driver Code
int main() {
    // Given a graph
    Graph g1(15);
    g1.addEdge(11, 10);
    g1.addEdge(10, 9);
    g1.addEdge(5, 7);
    g1.addEdge(7, 14);
    g1.addEdge(1, 5);
    g1.addEdge(1, 7);
    g1.addEdge(1, 14);
    g1.addEdge(2, 1);
    g1.addEdge(2, 10);
    g1.addEdge(12, 2);
    g1.addEdge(14, 0);
    g1.addEdge(0, 11);
    g1.addEdge(6, 5);
    g1.addEdge(6, 9);
    g1.addEdge(7, 12);
    g1.addEdge(8, 1);
    g1.addEdge(8, 10);
    g1.addEdge(8, 14);
    g1.addEdge(9, 13);
    g1.addEdge(9, 5);
    g1.addEdge(9, 10);
    g1.addEdge(9, 2);
    g1.addEdge(9, 11);
    g1.addEdge(3, 12);
    g1.addEdge(11, 6);
    g1.addEdge(11, 3);
    g1.addEdge(11, 12);
    g1.addEdge(12, 2);
    g1.addEdge(12, 4);
    g1.addEdge(12, 5);
    g1.addEdge(13, 6);
    g1.addEdge(13, 14);
    g1.addEdge(13, 2);
    g1.addEdge(14, 0);
    g1.addEdge(4, 2);
    

    // Function Call to find SCC using
    // Tarjan's Algorithm
    g1.SCC();

    return 0;
}
