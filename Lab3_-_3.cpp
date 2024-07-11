#include <iostream>
#include <cmath>

int main() {
    const double epsilon = 1e-6;
    double sum = 0.0;
    double term;
    int k = 1;

    do {
        term = 1.0 / pow(2, k-1) + pow(-1, k-1) / (2 * pow(3, k-1));
        sum += term;
        k++;
    } while (fabs(term) > epsilon);

    std::cout.precision(10);
    std::cout << "Sum of series: " << sum << std::endl;
    return 0;
}
