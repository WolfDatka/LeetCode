def isAnagram(s, t):
    s_list = []
    t_list = []

    for char in s:
        s_list.append(char)

    for char in t:
        t_list.append(char)

    s_list.sort()
    t_list.sort()

    return s_list == t_list

if __name__ == "__main__":
    s = "art"
    t = "cat"

    print(isAnagram(s, t))
