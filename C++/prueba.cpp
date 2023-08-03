#include <iostream>
#include <math.h>
#include <sys/time.h>
#include <vector>
#include"burbuja.hpp"
#include"treeSort.hpp"
#include"mergeSort.hpp"
#include"data.hpp"

int main()
{
    //create input array
    vector<int> A = datos("..//Data//50000.csv");
    int arr[A.size()];
     for(int i=0; i<A.size(); i++)
     {
        arr[i] = A[i];
     }

    int size = sizeof(arr)/sizeof(arr[0]);
    cout << sizeof(arr) << " Numero n "<<endl;
    cout << sizeof(arr[0]) << " Numero 0 "<<endl;


    mergeSort(arr, 0, size - 1);
  
        for (int i=0; i<100; i++)
       cout << arr[i] << " ";
  
    return 0;
}