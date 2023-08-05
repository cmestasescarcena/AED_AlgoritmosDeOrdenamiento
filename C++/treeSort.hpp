//Tree Sort implemented using C++
// Part of Cosmos by OpenGenus Foundation
#include <iostream>
using namespace std;
struct Node{
  int data;
  Node *left;
  Node *right;
};

//Function to create new Node
struct Node *newnode(int key)
{
  struct Node *temp=new Node;
  temp->data=key;
  temp->left=NULL;
  temp->right=NULL;
  return temp;
}

Node* insert(Node *node,int key)
{
  if(node==NULL) return newnode(key);//If tree is empty return new node
  if(key < node->data)
    node->left=insert(node->left,key);
  else
    node->right=insert(node->right,key);
  return node;
}
void store(Node *root,int a[],int &i)
{
  if(root!=NULL)
  {
    store(root->left,a,i);
    a[i++]=root->data;
    store(root->right,a,i);
  }
}
void TreeSort(int a[], int n)
{
    struct Node *root = NULL;
    //Construct binary search tree
    root = insert(root, a[0]);
    for (size_t i=1; i<n; i++)
        insert(root, a[i]);
    //Sorting the array using inorder traversal on BST
    int i = 0;
    store(root, a , i);
}