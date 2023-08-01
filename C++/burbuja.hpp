#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

// Extracción de datos
vector<int> datos(string name)
{
  ifstream archivo(name);
  vector<int> vect;
  string linea;
  int dato;
  char delimitador = ',';

  while (getline(archivo, linea))
  {
    stringstream stream(linea);
    string tempInt;
    getline(stream, tempInt, delimitador);
    dato = stoi(tempInt);
    vect.push_back(dato);
  }
return (vect);
}// Fin extracción

//Burbuja
vector<int> burbuja(vector<int> v)
{
  int i, j, aux;
  for (i=0; i<v.size(); i++)
  {
    for (j=0; j<v.size()-1; j++)
    {
      if (v[j] > v[j+1])
      {
        aux = v[j];
        v[j] = v[j+1];
        v[j+1] = aux;
      }
    }
  }
  return(v);
}// Fin burbuja
