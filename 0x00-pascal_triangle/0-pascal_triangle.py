def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # Initialize the triangle with the first row
    
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])  # Calculate the inner elements
        row.append(1)  # End each row with a 1
        triangle.append(row)
    
    return triangle

# Function to print the triangle
def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
