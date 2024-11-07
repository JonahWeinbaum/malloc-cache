#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main(void) {
  unsigned long long t1 = __builtin_ia32_rdtsc();
  void *p = malloc(10);
  unsigned long long t2 = __builtin_ia32_rdtsc();
  free(p);

  unsigned long long t3 = __builtin_ia32_rdtsc();
  void *p2 = malloc(40);
  unsigned long long t4 = __builtin_ia32_rdtsc();
  
  printf("First malloc %f\n", (float)(t2 - t1) / CLOCKS_PER_SEC);
  printf("Second malloc %f\n", (float)(t4 - t3) / CLOCKS_PER_SEC);
}
