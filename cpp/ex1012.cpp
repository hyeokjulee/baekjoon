#include <iostream>

void freeArray(int** arr, int rows) {
    for (int i = 0; i < rows; i++) {
        delete[] arr[i];
    }
    delete[] arr;
}

void count(int** arr, int x, int y, int rows, int cols) {
    arr[y][x] = 0;
    if(x < cols - 1 && arr[y][x + 1] == 1) {
        count(arr, x + 1, y, rows, cols);
    }
    if(y < rows - 1 && arr[y + 1][x] == 1) {
        count(arr, x, y + 1, rows, cols);
    }
    if(0 < x && arr[y][x - 1] == 1) {
        count(arr, x - 1, y, rows, cols);
    }
    if(0 < y && arr[y - 1][x] == 1) {
        count(arr, x, y - 1, rows, cols);
    }
}

int main() {
    int T, M, N, n, a, b, cnt;
    std::cin >> T;

    for(int i = 0; i < T; i++) {
        cnt = 0;
        std::cin >> M >> N >> n;

        int** array = new int*[N];
        for (int j = 0; j < N; j++) {
            array[j] = new int[M];
        }

        for (int j = 0; j < N; j++) {
            for (int k = 0; k < M; k++) {
                array[j][k] = 0;
            }
        }

        for(int j = 0; j < n; j++) {
            std::cin >> a >> b;
            array[b][a] = 1;
        }

        for(int j = 0; j < N; j++) {
            for(int k = 0; k < M; k++) {
                if(array[j][k] == 1) {
                    cnt++;
                    count(array, k, j, N, M);
                }
            }
        }

        freeArray(array, N);

        std::cout << cnt << "\n";
    }
}