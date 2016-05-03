#include <stdio.h>
extern "C"
{
	__declspec(dllexport) int plop();
	__declspec(dllexport) int sum(int a);
}
int sum(int a){
	return a++;
}

int plop() { return 80; }