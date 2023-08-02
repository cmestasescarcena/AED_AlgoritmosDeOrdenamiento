//program to solve the n queen problem 
//grid[][] is represent the 2-d array with value(0 and 1) for grid[i][j]=1 means queen i are placed at j column.
//we can take any number of queen , for this time we take the atmost 10 queen (grid[10][10]).
#include<iostream>
#include<math.h>
#include <sys/time.h>
#include "nqueens.hpp"

using namespace std;
long obtenerTiempo();

int main()
{
  ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cout << "N queens times: " << endl;
    cout<<"Result: [ ";
    for(int n=4; n<16; n++){

    long inicio = obtenerTiempo();
    double tiempoEnSegundos;
    long tiempoEnMicrosegundos;

              for (int i = 0;i < n;i++) {
            for (int j = 0;j < n;j++) {
                grid[i][j] = 0;
            }
        }
        bool res = solve(n, 0);

    long final = obtenerTiempo();
    tiempoEnMicrosegundos = final - inicio;
    tiempoEnSegundos = tiempoEnMicrosegundos * pow(10, -6);
    cout<<tiempoEnSegundos<<" ";

    }
    cout<<"]"<<endl;

  return 0;
}

long obtenerTiempo(){
  struct timeval inicio;
  gettimeofday(&inicio, NULL);
  return inicio.tv_sec*1000000+inicio.tv_usec;
}