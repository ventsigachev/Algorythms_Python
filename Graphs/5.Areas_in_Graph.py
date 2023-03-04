"""
    A Matrix could be represented as a Graph also.
    With Depth-First Search one could find the different areas in the Graph.
    We are given a matrix of letters of size N * M. Two cells are neighbors if they share a common wall.
    Let us find the connected areas of neighbor cells, holding the same letter.
"""


def dfs(letter, row, col, matrix, visited):
    if row < 0 or col < 0 or row == len(matrix) or col == len(matrix[0]):
        return

    if visited[row][col]:
        return

    if not matrix[row][col] == letter:
        return

    visited[row][col] = True

    dfs(letter, row + 1, col, matrix, visited)
    dfs(letter, row - 1, col, matrix, visited)
    dfs(letter, row, col + 1, matrix, visited)
    dfs(letter, row, col - 1, matrix, visited)


def create_letters_dict(letter, number_of_letters):
    if letter not in number_of_letters:
        number_of_letters[letter] = 1
    else:
        number_of_letters[letter] += 1


def create_areas_dict(letter, number_of_areas):
    if letter not in number_of_areas:
        number_of_areas[letter] = 1
    else:
        number_of_areas[letter] += 1

    return 1


def printing_results(n_l, n_a, t_a):
    print(f"Total Areas: {t_a}\n")

    for area, counter in sorted(n_a.items()):
        if counter > 1:
            print(f"Areas with '{area}' found {counter} times")
        else:
            print(f"Area with '{area}' found 1 time")
    print()

    for letter, counter in sorted(n_l.items(), key=lambda x: x[1], reverse=True):
        print(f"Found {counter} of letter '{letter}'")


def main():
    rows = int(input())
    cols = int(input())

    matrix = []
    visited = []

    number_of_letters = {}
    number_of_areas_by_letter = {}
    total_areas = 0

    for _ in range(rows):
        matrix.append(list(input()))
        visited.append([False] * cols)

    for row in range(rows):
        for col in range(cols):
            letter = matrix[row][col]

            create_letters_dict(letter, number_of_letters)

            if visited[row][col]:
                continue

            dfs(letter, row, col, matrix, visited)

            total_areas += create_areas_dict(letter, number_of_areas_by_letter)

    printing_results(number_of_letters, number_of_areas_by_letter, total_areas)


if __name__ == "__main__":
    main()


"""
Possible Inputs:

6
8
aacccaac
baaaaccc
baabaccc
bbdaaccc
ccdccccc
ccdccccc

3
3
aaa
aaa
aaa

5
9
asssaadas
adsdasdad
sdsdadsas
sdasdsdsa
ssssasddd

"""