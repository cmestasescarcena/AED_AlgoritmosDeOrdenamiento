#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>&arreglo, int inicio, int mitad, int final)
{
  int i, j, k;
  int elementosIzq = mitad - inicio + 1;
  int elementosDer = final - mitad;

  vector<int>izquierda(elementosIzq);
  vector<int>derecha(elementosDer);

  for(int i=0; i<elementosIzq; i++)
  {
    izquierda[i] = arreglo[inicio+i];
  }

    for(int j=0; j<elementosDer; j++)
  {
    derecha[j] = arreglo[mitad + 1 + j];
  }

  i = 0;
  j = 0;
  k = inicio;

  while(i < elementosIzq && j < elementosDer)
  {
    if(izquierda[i] <= derecha[j])
    {
      arreglo[k] = izquierda[i];
      i++;
    }
    else
    {
      arreglo[k] = derecha[j];
      j++;
    }
    k++;
  }

  while (j < elementosDer)
  {
    arreglo[k] = derecha[j];
    j++;
    k++;
  }

  while (i < elementosDer)
  {
    arreglo[k] = izquierda[i];
    i++;
    k++;
  }

}

vector<int> mergeSort(vector<int>&arreglo, int inicio, int final)
{
  if(inicio < final)
  {
    int mitad = inicio + (final-inicio)/2;
    mergeSort(arreglo, inicio, mitad); //divide parte izquierda
    mergeSort(arreglo, mitad+1, final); //divide parte derecha
    merge(arreglo, inicio, mitad, final);
  }
  return(arreglo);
}