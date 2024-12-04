def find_diff_between_sorted_numbers()->int:
    list1 = []
    list2 = []
    with open("day1.txt", "r") as file:
        while True:
            line = file.readline().split()
            if not line:
                break
            list1.append(int(line[0]))
            list2.append(int(line[1]))
    list1 = iter(sorted(list1))
    list2 = iter(sorted(list2))
    ans = 0
    while list1 and list2:
        try:
            int1 = next(list1)
            int2 = next(list2)
        except StopIteration:
            break
        diff = abs(int1 - int2)
        ans+=diff
    return ans

def find_similarity()->int:
    list1 = []
    list2 = []
    with open("day1.txt", "r") as file:
        while True:
            line = file.readline().split()
            if not line:
                break
            list1.append(int(line[0]))
            list2.append(int(line[1]))
    list2 = sorted(list2)
    similarity_dict = {}
    for i in list2:
        if i in similarity_dict:
            similarity_dict[i] +=1
        else:
            similarity_dict[i] = 1
    ans = 0
    for i in list1:
        if i in similarity_dict:
            ans += i*similarity_dict[i]
    return ans
    
answer = find_similarity()
print(answer)
    