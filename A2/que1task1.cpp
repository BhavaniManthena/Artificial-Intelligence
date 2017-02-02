#include<iostream>
#include<fstream>
#include<stdlib.h>//rand,srand
#include<time.h> //time
#include<ctime>
#include<math.h>
#define _USE_MATH_DEFINES
#define M_PI1
using namespace std;
//float PI=3.14;
float RandomFloat(float a,float b)
{
	float random=((float)rand())/(float)RAND_MAX;
	float diff=b-a;
	float r=random*diff;
	return a+r;
}
double ackely(float x,float y)
{
	double f;
	f=((-20)*exp((-0.2)*sqrt(0.5*(pow(x,2)+pow(y,2))))) - exp((0.5)*(cos(2*M_PI*x)+cos(2*M_PI*y)));
	return f;
}

int main()
{
    ofstream myfile;
    myfile.open("file11.txt");
	srand(time(NULL));
	float x,y,x1,y1;
	int i=0;
	double result,result1;
	for(int k=1;k<=100;k++)
	{
		x=RandomFloat(-4.99,4.99);
		y=RandomFloat(-4.99,4.99);
		result=ackely(x,y);
		for(int j=1;j<=100;j++)
		{
			x1=((RandomFloat(0.0,0.9)-0.5)*0.1)+x;
			y1=((RandomFloat(0.0,0.9)-0.5)*0.1)+y;
			result1=ackely(x1,y1);
			if(result1>result)
			{
				//cout<<j;
				break;
			}
			x=x1;
			y=y1;
			result=result1;
		}
		//cout<<k<<endl;
		myfile<<result<<endl;
		cout<<result<<endl; //prints the least value result
	}
	myfile.close();
}
