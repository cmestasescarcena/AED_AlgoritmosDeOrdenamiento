#include <iostream>
#include <math.h>
#include <sys/time.h>
#include <vector>
#include"burbuja.hpp"
#include"treeSort.hpp"
#include"mergeSort.hpp"
#include"data.hpp"

using namespace std;

long obtenerTiempo();

int main()
{


  int intentos = 15;
  string docName[] = { "..//Data//100.csv",
                    "..//Data//1000.csv",
                    "..//Data//2000.csv",
                    "..//Data//3000.csv",
                    "..//Data//4000.csv",
                    "..//Data//5000.csv",
                    "..//Data//6000.csv",
                    "..//Data//7000.csv",
                    "..//Data//8000.csv",
                    "..//Data//9000.csv",
                    "..//Data//10000.csv",
                    "..//Data//20000.csv",
                    "..//Data//30000.csv",
                    "..//Data//40000.csv",
                    "..//Data//50000.csv" };


  // TREE SORT
  for (int k = 0; k < 15; k++)
  {
    int i = 0;

    cout << "Tree Sort 15 times size "<<docName[k]<<endl;
    cout << "Result: [";

    while (i < 15)
    {
      vector<int> A = datos(docName[k]);
      int arr[A.size()];
      for (int i = 0; i < A.size(); i++)
      {
        arr[i] = A[i];
      }
      int size = sizeof(arr) / sizeof(arr[0]);

      long inicio = obtenerTiempo();
      double tiempoEnSegundos;
      long tiempoEnMicrosegundos;

      TreeSort(arr,size);

      long final = obtenerTiempo();
      tiempoEnMicrosegundos = final - inicio;
      tiempoEnSegundos = tiempoEnMicrosegundos * pow(10, -6);
      cout << tiempoEnSegundos << ", ";

      i++;
    }
    cout << "]" << endl;
    cout << endl;
  }
//**********************************************


/*
// MERGE SORT
  for (int k = 0; k < 15; k++)
  {
    int i = 0;

    cout << "Merge Sort 15 times size "<<docName[k]<<endl;
    cout << "Result: [";

    while (i < 15)
    {
      vector<int> A = datos(docName[k]);
      int arr[A.size()];
      for (int i = 0; i < A.size(); i++)
      {
        arr[i] = A[i];
      }
      int size = sizeof(arr) / sizeof(arr[0]);

      long inicio = obtenerTiempo();
      double tiempoEnSegundos;
      long tiempoEnMicrosegundos;

      mergeSort(arr, 0, size - 1);

      long final = obtenerTiempo();
      tiempoEnMicrosegundos = final - inicio;
      tiempoEnSegundos = tiempoEnMicrosegundos * pow(10, -6);
      cout << tiempoEnSegundos << ", ";

      i++;
    }
    cout << "]" << endl;
    cout << endl;
  }
//**********************************************
*/

/*
// BURBUJA
  for (int k = 0; k < 15; k++)
  {
    int i = 0;

    cout << "Bubble Sort 15 times size "<<docName[k]<<endl;
    cout << "Result: [";

    while (i < 15)
    {
      vector<int> A = datos(docName[k]);
      int arr[A.size()];
      for (int i = 0; i < A.size(); i++)
      {
        arr[i] = A[i];
      }
      int n = sizeof(arr) / sizeof(arr[0]);
   
      long inicio = obtenerTiempo();
      double tiempoEnSegundos;
      long tiempoEnMicrosegundos;

      bubbleSort(arr, n);

      long final = obtenerTiempo();
      tiempoEnMicrosegundos = final - inicio;
      tiempoEnSegundos = tiempoEnMicrosegundos * pow(10, -6);
      cout << tiempoEnSegundos << ", ";

      i++;
    }
    cout << "]" << endl;
    cout << endl;
  }
//**********************************************
*/

  return 0;
}

long obtenerTiempo(){
  struct timeval inicio;
  gettimeofday(&inicio, NULL);
  return inicio.tv_sec*1000000+inicio.tv_usec;
}

