#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int T, x1, y1, x2, y2, n, cx, cy, r, cnt;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cnt = 0;
        cin >> x1 >>  y1 >>  x2 >>  y2;
        cin >> n;
        for (int j = 0; j < n; j++) {
            cin >> cx >>  cy >>  r;
            if (pow(x1 - cx, 2) + pow(y1 - cy, 2) < pow(r, 2) && pow(x2 - cx, 2) + pow(y2 - cy, 2) > pow(r, 2)) {
                cnt++;
            }
            if (pow(x2 - cx, 2) + pow(y2 - cy, 2) < pow(r, 2) && pow(x1 - cx, 2) + pow(y1 - cy, 2) > pow(r, 2)) {
                cnt++;
            }
        }
        cout << cnt;
    }
    cin >> n;
}