#include <stdio.h>

int jordan_nonzeros(int n, const int gms[], int k) {
    int B = 0;
    for (int i = 0; i < k; ++i) B += gms[i];  
    int r = n - B;                            
    if (r < 0 || r > B) return -1;
    return B + 2 * r;                         
}

int num_two_by_two_blocks(int n, const int gms[], int k) {
    int B = 0;
    for (int i = 0; i < k; ++i) B += gms[i];
    int r = n - B;
    return (r < 0 || r > B) ? -1 : r;
}

int num_one_by_one_blocks(int n, const int gms[], int k) {
    int B = 0;
    for (int i = 0; i < k; ++i) B += gms[i];
    int r = n - B;
    return (r < 0 || r > B) ? -1 : (B - r);
}

