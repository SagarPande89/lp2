class NQueens:
    def __init__(self, n):
        self.n = n
        self.queens = [-1] * n

    def solve(self, method):
        self.method = method
        self.num_solutions = 0  # Reset solution count for each method
        self.solve_helper(0)

    def solve_helper(self, row):
        if row == self.n:
            self.num_solutions += 1
            if self.num_solutions <= 2:  # Limiting to print only 2 solutions
                self.print_solution()
        else:
            for col in range(self.n):
                if self.is_valid(row, col):
                    self.queens[row] = col
                    self.solve_helper(row + 1)
                    self.queens[row] = -1

    def is_valid(self, row, col):
        for i in range(row):
            if self.queens[i] == col or abs(row - i) == abs(col - self.queens[i]):
                return False
        return True

    def print_solution(self):
        method_name = "Backtracking" if self.method == "backtracking" else "Branch and Bound"
        print(f"{method_name} Solution {self.num_solutions}: ")
        for row in range(self.n):
            line = "".join("Q " if col == self.queens[row] else "- " for col in range(self.n))
            print(line)
        print()


if __name__ == "__main__":
    n = int(input("Enter N Queens Problem: "))
    n_queens = NQueens(n)

    # Backtracking
    print("Solving using Backtracking:")
    n_queens.solve("backtracking")

    # Branch and Bound
    print("\nSolving using Branch and Bound:")
    n_queens.solve("branch_and_bound")