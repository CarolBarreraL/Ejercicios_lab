#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*Funciones*/
void condicionInicial(double dx, int nX, double *u, double *saveUinicial);
//void primeraIteracion(double a, int nX, double *uAntes, double *uPresent);
void accion(double a, int nX, double *uAntes, double *uFut);
void actualizar(int nX, double *uAntes, double *uFut);
void guardarDatos(int nX, double dx, double *u, double *uInicial);


int main(void)
{
	double xFinal = 2.0;
	int puntosX = 100;
	double tFinal = 0.3;
	int puntosT = 300;
	double c = 1.0;
	int i;

	double dt = 0.001;
	double alpha = 0.05;
	double dX = c*dt/alpha;
	
	double *uAnterior = malloc(puntosX*sizeof(double));
	double *uPresente = malloc(puntosX*sizeof(double));
	double *uInicial = malloc(puntosX*sizeof(double));
	double *uFutura = malloc(puntosX*sizeof(double));
	
	condicionInicial(dX, puntosX, uAnterior, uInicial);
	//primeraIteracion(alpha, puntosX, uAnterior, uPresente);
	actualizar(puntosX, uPresente ,uAnterior);
	for(i=0;i<puntosT;i++)
	{	
		actualizar(puntosX,uAnterior, uPresente);
		accion(alpha, puntosX, uAnterior, uPresente);
	}
	guardarDatos(puntosX, dX, uPresente, uInicial);

	return 0;

}

void condicionInicial(double dx, int nX, double *u, double *saveUinicial)
{
	int i;
	for(i=0;i<nX;i++)
	{
		double x = i*dx;
		if(x<0.7){u[i]=0;}
		else if(x>0.7 && x<1.2){u[i]=2;}
		else if(x>1.2){u[i]=0;}
		saveUinicial[i]=u[i];
	}
}


void accion(double a, int nX, double *uAntes, double *uFut)
{
	int i;
	for(i=1;i<nX-1;i++)
	{
		uFut[i] = uAntes[i] + a*(uAntes[i-1] - uAntes[i]);
	}
}

void actualizar(int nX, double *uAntes, double *uFut)
{
	int i;
	for(i=0;i<nX;i++)
	{
		uAntes[i]=uFut[i];
	}
}

void guardarDatos(int nX, double dx, double *u, double *uInicial)
{
	int i;
	for(i=0;i<nX;i++)
	{
		printf("%e,%e,%e\n", i*dx, u[i], uInicial[i]);
	}
}






