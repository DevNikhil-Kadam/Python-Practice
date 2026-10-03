class Solution:
    # Returns matrix elements in clockwise spiral order.
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # An empty matrix has no cells to traverse.
        if not matrix or not matrix[0]:
            return []

        order: list[int] = []
        top: int = 0
        bottom: int = len(matrix) - 1
        left: int = 0
        right: int = len(matrix[0]) - 1

        # Process one remaining rectangular layer at a time.
        while top <= bottom and left <= right:
            # Collect the current top row from left to right.
            for col in range(left, right + 1):
                order.append(matrix[top][col])
            top += 1

            # Collect the current right column from top to bottom.
            for row in range(top, bottom + 1):
                order.append(matrix[row][right])
            right -= 1

            # A bottom row remains only if the top boundary has not crossed it.
            if top <= bottom:
                # Collect the current bottom row from right to left.
                for col in range(right, left - 1, -1):
                    order.append(matrix[bottom][col])
                bottom -= 1

            # A left column remains only if the right boundary has not crossed it.
            if left <= right:
                # Collect the current left column from bottom to top.
                for row in range(bottom, top - 1, -1):
                    order.append(matrix[row][left])
                left += 1

        return order


# Prints a one-dimensional integer list.
def print_values(values: list[int]) -> None:
    print(values)


# Driver code
def main() -> None:
    matrix: list[list[int]] = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]

    # instance for class Solution
    sol: Solution = Solution()

    result: list[int] = sol.spiralOrder(matrix)
    print_values(result)


if __name__ == "__main__":
    main()