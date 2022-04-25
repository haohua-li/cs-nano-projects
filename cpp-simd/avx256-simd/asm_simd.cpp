#include <cstdio>

// extern "C" 
// int64_t maxofthree(int64_t, int64_t, int64_t);

extern "C"
void avx256Add(double* C, double* A, double* B); 


int main(){
    double A[] = {1.0, 2.0, 3.0, 4.0}; 
    double B[] = {8.0, 7.0, 6.0, 5.0}; 
    double C[] = {0.0, 0.0, 0.0, 0.0}; 

    // printf("%lld\n", maxofthree(1, -4, -7));
    avx256Add(C, A, B); 
    printf("[%lf, ", C[0]); 
    printf("%lf, ", C[1]); 
    printf("%lf, ", C[2]); 
    printf("%lf]\n", C[3]); 
    
    return 0; 
}