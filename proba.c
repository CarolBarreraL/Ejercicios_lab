#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

void condicionInicial(double *u, int nt, double dt, double *tiempo );
void Proceso(float lm, double dt, double t, int puntos, double *up, double *tim);

int main(void)
{
	double tFinal = 10.0;
	int nT = 1000;
	double dt = tFinal/nT;
	double *u = malloc(nT*sizeof(double));
	double *uProceso = malloc(nT*sizeof(double));
	double *tiempo = malloc(nT*sizeof(double));
	double *utemp = malloc(nT*sizeof(double));
	double *uUnaVez = malloc(nT*sizeof(double));
	
	condicionInicial(u, nT, dt, tiempo);

	srand48(1);

	Proceso(0.5, dt, tFinal, nT, uUnaVez, tiempo);
	
	Proceso(0.5, dt, tFinal, nT, uProceso, tiempo);
	int i,j;
	float pasos = 200;

	for(j=0;j<pasos;j++)
	{
		Proceso(0.5, dt, tFinal, nT, utemp, tiempo);
		for(i=0; i<nT;i++)
		{
			uProceso[i]+= utemp[i];
		}
	}

	for(j=0;j<nT;j++)
	{
		uProceso[j] = (uProceso[j]/pasos);
		printf("%e,%e,%e,%e\n", tiempo[j], uProceso[j], uUnaVez[j], u[j]);
	}

	return 0;
}

void condicionInicial(double *u, int nt, double dt, double *tiempo )
{
	int i;
	double gam = 0.5;
	double t=0.0;
	u[0] =10;
	for(i=1;i<nt;i++)
	{
		t+=dt;
		u[i]= 10*exp(-gam*t);
	}
}



void Proceso(float lm, double dt, double N0 , int puntos, double *up, double *tim)
{
	int i;
	double time=0.0;
	double n = N0;
	double numAle;
	up[0]=n;
	tim[0]=0.0;
	for(i=1;i<puntos;i++)
	{
		numAle = drand48();
		time+=dt;
		tim[i]=time;
		if(numAle< dt*lm*n)
		{
			n= n- 1;
			up[i]=n;
		}
		else{n = n; up[i]=n;}
		
		//printf("%e,%e\n", tim[i], up[i]);
		
	}
}





