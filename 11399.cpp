#include <stdio.h>
#include <algorithm>
using namespace std;
int a, s[100002], d = 0;
int main() {
    scanf("%d", &a);
    for (int g = 0; g < a; g++)
        scanf("%d", &s[g]);
    sort(s, s + a);
    for (int g = 0; g < a; g++)
        d += s[g] * (a - g);
    printf("%d", d);
}
