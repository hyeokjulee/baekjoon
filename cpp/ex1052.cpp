#include <iostream>

using namespace std;

int main() {
    int N, K, num, tmp, multi = 1;
    cin >> N >> K;

    for (int i = 0; i < K - 1; i++) {
        while (multi <= N * 0.5) {
            multi *= 2;
        }
        N -= multi;
        if (N == 0) {
            cout << 0 << endl;
            return 0;
        }
        multi = 1;
    }

    while (multi < N) {
        multi *= 2;
    }

    cout << multi - N << endl;
    cin >> K;
    return 0;
}