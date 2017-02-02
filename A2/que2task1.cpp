#include<iostream>
#include<stdlib.h>
#include<cmath>
#include<time.h>
using namespace std;
int heuristic(int matrix[],int n)
{
	int i,j,count=0;
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(matrix[i]==matrix[j])
				count++;
			if(abs(matrix[i]-matrix[j])==abs(i-j))
				count++;
		}
	}
	return count;
}
int main()
{
	srand(time(NULL));
	int n;
	int innerloop=0;
	int number=0;
    cout<<"8 or 16 queens?"<<'\t';
    cin>>n;
    cout<<"for First 10 iterations \n";
	for(int y=0;y<100;y++)
        {
        if(y<11)
        {
            cout<<y<<"\titeration\n";
        }
        int i,j,row=0,col=0,val=0,globalactualcount=0;
        int count=0,actualcount=0,temp=0,flag=0;
        int a[n],copy[n],newcopy[n];
		for(int g=0;g<n;g++)
		{
			a[g]=rand()%n;
        }
        if(innerloop<11)
        {
            cout<<"Initial State \t";
            for(int i=0;i<n;i++)
                cout<<a[i]<<"\t";
            cout<<"\n";
        }
		actualcount=heuristic(a,n);
		val=actualcount;
		for(i=0;i<n;i++)
		{
			copy[i]=a[i];
		}
		do{
			actualcount=heuristic(copy,n);
			globalactualcount=actualcount;
			for(i=0;i<n;i++)
			{
				temp=copy[i];
				for(j=0;j<n;j++)
				{
					copy[i]=j;
					count=heuristic(copy,n);
					if(count<actualcount)
					{
						actualcount=count;
						col=i;
						row=j;
						for(int k=0;k<n;k++)
						{
							newcopy[k]=copy[k];
						}
					}
				}
				copy[i]=temp;
							}
			//cout<<actualcount<<'\t'<<col<<'\t'<<row;
            for(i=0;i<n;i++)
            {
                copy[i]=newcopy[i];
            }

			if(actualcount==0)
			{

				//cout<<"yes h is 0";
				break;
			}

			if(globalactualcount==actualcount)
			{
				flag=1;
				//cout<<flag<<endl;
				break;
			}
		}while(actualcount!=0);
		if(flag==0){
        //if solution is found number is incremented
			number=number+1;
		}
		if(innerloop<11)
        {
            cout<<"final State \t";
            for(int i=0;i<n;i++)
                cout<<a[i]<<"\t";
            innerloop++;
            cout<<"\n";
        }
	}
	cout<<"Total number of solutions for 100 iteration :"<<number;
	return 0;
}
