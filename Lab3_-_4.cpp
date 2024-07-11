#include <iostream>
#include <cmath>

int main() {
    const double epsilon = 1e-6;
    double sum = 0.0;
    double term;
    int k = 1;
    double x;

    std::cout << "Enter the value of x: ";
    std::cin >> x;

    do {
        term = pow(-1, k) / (sin(k * x) + 1 + k * k);
        sum += term;
        k++;
    } while (fabs(term) > epsilon);

    std::cout.precision(10);
    std::cout << "Sum of series: " << sum << std::endl;
    return 0;
}
