def compute_lcs_len(text1, text2):

    n = len(text1)
    m = len(text2)

    lcs = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif text1[i - 1] == text2[j - 1]:
                lcs[i][j] = 1 + lcs[i - 1][j - 1]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    return lcs


def diff(text1, text2):
    lcs = compute_lcs_len(text1, text2)

    i = len(text1)
    j = len(text2)

    result = []
    counter = 0

    while i != 0 or j != 0:
        if i == 0:
            result.append("+ " + text2[j - 1])
            j -= 1
        elif j == 0:
            result.append("- " + text1[i - 1])
            i -= 1
        elif text1[i - 1] == text2[j - 1]:
            result.append("= " + text1[i - 1])
            counter += 1
            i -= 1
            j -= 1
        elif lcs[i - 1][j] <= lcs[i][j - 1]:
            result.append("+ " + text2[j - 1])
            j -= 1
        else:
            result.append("- " + text1[i - 1])
            i -= 1

    return list(reversed(result)), counter


def print_diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        line1 = f1.readlines()
        line2 = f2.readlines()

    result, length = diff(line1, line2)

    print("Result:")
    for line in result:
        print(line.rstrip())
    print("\nLCS:", length)


file_1 = "file_1.txt"
file_2 = "file_2.txt"
print_diff(file_1, file_2)
