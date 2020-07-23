

#include<bits/stdc++.h>

using namespace std;

class Node
{
public:
int data;
Node* left,*right;
	
};

Node* newnode(int data)
{
	Node* new_node=new Node();
	new_node->data=data;
	new_node->left=NULL;
	new_node->right=NULL;

	return new_node;

}


Node* sorted_To_bst(int* arr, int start,int end)
{
	if(start>end)
		return NULL;
	int middle=(start+end)/2;

	Node* root=newnode(arr[middle]);
	root->left=sorted_To_bst(arr,start,middle-1);
	root->right=sorted_To_bst(arr,middle+1,end);

	return root;
}

void preorder(Node* root)
{
	if(root==NULL)
		return;
	else 
	{
		cout<<root->data<<" ";
		preorder(root->left);
		preorder(root->right);
	}
}

int main()
{ int t;

	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int arr[n];
		for(int i=0;i<n;i++)
		{
			cin>>arr[i];
		}
		Node* root=NULL;
		root=sorted_To_bst(arr,0,n-1);
		preorder(root);
		cout<<endl;
	}


}