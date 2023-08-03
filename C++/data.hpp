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
