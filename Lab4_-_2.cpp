#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double determinant(double matrix[3][3]) {
    return matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
           matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
           matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
}

void cramer_method(double A[3][3], double B[3], double solution[3]) {
    double detA = determinant(A);
    if (fabs(detA) < 1e-10) {
        cout << "Determinant is too close to zero, the system might not have a unique solution." << endl;
        return;
    }

    double matrix[3][3];
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            matrix[j][i] = A[j][i];
        }
        for (int j = 0; j < 3; ++j) {
            matrix[j][i] = B[j];
        }
        solution[i] = determinant(matrix) / detA;
        for (int j = 0; j < 3; ++j) {
            matrix[j][i] = A[j][i];
        }
    }
}

void jacobi_method(double A[3][3], double B[3], double solution[3], int max_iterations = 1000, double tolerance = 1e-10) {
    double x[3] = {0.0, 0.0, 0.0};
    double x_new[3] = {0.0, 0.0, 0.0};
    
    for (int iter = 0; iter < max_iterations; ++iter) {
        for (int i = 0; i < 3; ++i) {
            double sum = B[i];
            for (int j = 0; j < 3; ++j) {
                if (i != j) {
                    sum -= A[i][j] * x[j];
                }
            }
            x_new[i] = sum / A[i][i];
        }

        double error = 0.0;
        for (int i = 0; i < 3; ++i) {
            error += fabs(x_new[i] - x[i]);
        }

        if (error < tolerance) {
            for (int i = 0; i < 3; ++i) {
                solution[i] = x_new[i];
            }
            return;
        }

        for (int i = 0; i < 3; ++i) {
            x[i] = x_new[i];
        }
    }

    for (int i = 0; i < 3; ++i) {
        solution[i] = x_new[i];
    }
}

int main() {
    double A[3][3] = {
        {5, 2, -2},
        {3, -3, -1},
        {2, 3, -1}
    };
    double B[3] = {0, 1, -1};
    double cramer_solution[3];
    double jacobi_solution[3];

    cramer_method(A, B, cramer_solution);
    cout << "Solution using Cramer's Method:" << endl;
    cout << fixed << setprecision(10);
    for (int i = 0; i < 3; ++i) {
        cout << cramer_solution[i] << " ";
    }
    cout << endl;

    jacobi_method(A, B, jacobi_solution);
    cout << "Solution using Jacobi Method:" << endl;
    for (int i = 0; i < 3; ++i) {
        cout << jacobi_solution[i] << " ";
    }
    cout << endl;

    return 0;
}
