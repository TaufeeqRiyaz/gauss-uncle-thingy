def print_matrix(matrix):
    for row in matrix:
        print(row)

def gaussian_elimination(matrix):
    n = len(matrix)
    for i in range(n):
        max_index = i
        max_value = abs(matrix[i][i])
        for k in range(i+1, n):
            if abs(matrix[k][i]) > max_value:
                max_value = abs(matrix[k][i])
                max_index = k
        matrix[i], matrix[max_index] = matrix[max_index], matrix[i]
        
        for j in range(i+1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n+1):
                matrix[j][k] -= ratio * matrix[i][k]
        
        print(f"Step {i+1}:")
        print_matrix(matrix)
        print()

    solution = [0] * n
    for i in range(n-1, -1, -1):
        solution[i] = matrix[i][n] / matrix[i][i]
        for j in range(i-1, -1, -1):
            matrix[j][n] -= matrix[j][i] * solution[i]
    
    return solution

def main():
    n = int(input("Enter the number of equations - "))
    equations = []
    print("Enter the coefficients and constant term for each equation sperated by a space -")
    for i in range(n):
        equation = list(map(float, input(f"Equation {i+1}: ").split()))
        equations.append(equation)
    
    print("\nSystem of equations -")
    print_matrix(equations)
    print()
    
    solution = gaussian_elimination(equations)
    
    print("\nSolution -")
    for i, value in enumerate(solution):
        print(f"x{i+1} =", value)

if __name__ == "__main__":
    main()
