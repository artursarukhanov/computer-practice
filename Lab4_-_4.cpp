#include <iostream>
#include <iomanip>

using namespace std;

void thomas_algorithm(int n, double a[], double b[], double c[], double d[], double x[]) {
    double *c_star = new double[n];
    double *d_star = new double[n];

    c_star[0] = c[0] / b[0];
    d_star[0] = d[0] / b[0];

    for (int i = 1; i < n; i++) {
        double m = b[i] - a[i] * c_star[i - 1];
        c_star[i] = c[i] / m;
        d_star[i] = (d[i] - a[i] * d_star[i - 1]) / m;
    }

    x[n - 1] = d_star[n - 1];
    for (int i = n - 2; i >= 0; i--) {
        x[i] = d_star[i] - c_star[i] * x[i + 1];
    }

    delete[] c_star;
    delete[] d_star;
}

int main() {
    const int n = 5;
    double a[n] = {0, -3, -2, -4, 4};
    double b[n] = {12, -18, -16, 18, -9};
    double c[n] = {-5, -8, -9, -7, 0};
    double d[n] = {148, 45, -155, 11, 3};
    double x[n];

    thomas_algorithm(n, a, b, c, d, x);

    cout << "Solution using Thomas Algorithm:" << endl;
    cout << fixed << setprecision(10);
    for (int i = 0; i < n; i++) {
        cout << "x[" << i + 1 << "] = " << x[i] << endl;
    }

    return 0;
}
