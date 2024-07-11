#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double lagrange_interpolation(double x_eval, double x[], double y[], int n) {
    double result = 0.0;
    for (int i = 0; i <= n; ++i) {
        double term = y[i];
        for (int j = 0; j <= n; ++j) {
            if (j != i) {
                term *= (x_eval - x[j]) / (x[i] - x[j]);
            }
        }
        result += term;
    }
    return result;
}

int main() {
    const int n = 3;
    double x[n+1] = {0.1 * M_PI, 0.2 * M_PI, 0.3 * M_PI, 0.4 * M_PI};
    double y[n+1];
    for (int i = 0; i <= n; ++i) {
        y[i] = sin(x[i]);
    }

    double x_eval = 0.25 * M_PI;
    double interpolation = lagrange_interpolation(x_eval, x, y, n);

    double exact_value = sin(x_eval);

    double error = abs(exact_value - interpolation);

    cout << "Значение sin(" << x_eval << "): " << exact_value << endl;
    cout << "Значение интерполяции в точке " << x_eval << ": " << interpolation << endl;
    cout << "Погрешность: " << error << endl;

    return 0;
}
