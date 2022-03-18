def length_of_longest_substring(s: str) -> int:
    m = 0
    seen = {}
    start = 0
    for i in range(len(s)):
        if s[i] in seen:
            start = max(start, seen[s[i]] + 1)
        seen[s[i]] = i
        m = max(m, i - start + 1)
    return m

if __name__ == '__main__':
    print(length_of_longest_substring("abcdbef"))
    print(length_of_longest_substring("abdefgabef"))
    print(length_of_longest_substring("abacbefghpa"))
    print(length_of_longest_substring("abcbjbzddefghlo"))