#include <iostream>
#include <math.h>
#include <sys/time.h>
#include <vector>
#include"data.hpp"
#include"treeSort.hpp"

int main()
{
    //create input array
    vector<int> A = datos("..//Data//4000v2.csv");
    int arr[A.size()];
     for(int i=0; i<A.size(); i++)
     {
        arr[i] = A[i];
     }
     
     int n = sizeof(arr) / sizeof(arr[0]);

    TreeSort(arr,n);
    
    cout<<"The sorted array is :\n";
    //Printing the sorted array
    for(size_t i=0;i<n;i++)
    {
      cout<<arr[i]<<" ";
    }
    return 0;
}