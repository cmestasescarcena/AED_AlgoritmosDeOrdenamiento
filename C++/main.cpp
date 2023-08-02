#include <iostream>
#include <math.h>
#include <sys/time.h>
#include <vector>
#include"burbuja.hpp"
#include"treeSort.hpp"
#include"mergeSort.hpp"

using namespace std;

long obtenerTiempo();

int main()
{
  int intentos = 15;
  vector<int> A = datos("..//Data//4000.csv");
  int Asize = A.size();


// BURBUJA
  cout << "Bubble Sort 15 times size 70000" << endl;
  cout<<"Result: [ ";
  for (int i = 0; i < intentos; i++)
  {
    long inicio = obtenerTiempo();
    double tiempoEnSegundos;
    long tiempoEnMicrosegundos;
    burbuja(A);
    long final = obtenerTiempo();
    tiempoEnMicrosegundos = final - inicio;
    tiempoEnSegundos = tiempoEnMicrosegundos * pow(10, -6);
    cout<<tiempoEnSegundos<<" ";
  }
  cout<<"]"<<endl;
  cout<<endl;

// TREE SORT
  cout << "Tree Sort 15 times size 30000" << endl;
  cout<<"Result: [ ";
  for (int i = 0; i < intentos; i++)
  {
    long inicio = obtenerTiempo();
    double tiempoEnSegundos;
    long tiempoEnMicrosegundos;
    TreeSort(A);
    long final = obtenerTiempo();
    tiempoEnMicrosegundos = final - inicio;
    tiempoEnSegundos = tiempoEnMicrosegundos * pow(10, -6);
    cout<<tiempoEnSegundos<<" ";
  }
  cout<<"]"<<endl;
  cout<<endl;

//MERGE SORT
  cout << "Merge Sort 15 times size 30000" << endl;
  cout<<"Result: [ ";
  for (int i = 0; i < intentos; i++)
  {
    long inicio = obtenerTiempo();
    double tiempoEnSegundos;
    long tiempoEnMicrosegundos;
    mergeSort(A, 0, Asize-1);
    long final = obtenerTiempo();
    tiempoEnMicrosegundos = final - inicio;
    tiempoEnSegundos = tiempoEnMicrosegundos * pow(10, -6);
    cout<<tiempoEnSegundos<<" ";
  }
  cout<<"]"<<endl;
  cout<<endl;


  return 0;
}

long obtenerTiempo(){
  struct timeval inicio;
  gettimeofday(&inicio, NULL);
  return inicio.tv_sec*1000000+inicio.tv_usec;
}

