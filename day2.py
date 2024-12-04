def check_increase(line):
        for i in range(len(line)-1):
            n1 = int(line[i])
            n2 = int(line[i+1])
            diff = abs(n1-n2)
            if n1 > n2:
                return False
            if diff<1 or diff >=4:
                return False
        return True
    
def check_decrease(line):
    for i in range(len(line)-1):
        n1 = int(line[i])
        n2 = int(line[i+1])
        diff = abs(n1-n2)
        if n1 < n2:
            return False
        if diff<1 or diff >=4:
            return False
    return True

def check_safe(line):
    return check_increase(line) or check_decrease(line)

def safe_reports():
    count = 0
    with open("day2.txt","r") as file:
        while True:
            line = file.readline().split()
            if not line:
                break
            if check_safe(line):
                count+=1
            
    return count

def check_again(line):
    for i in range(len(line)):
        copy = line[:]
        copy.pop(i)
        if check_safe(copy):
            return True
    return False

def new_safe_reports():
    count = 0
    with open("day2.txt","r") as file:
        while True:
            line = file.readline().split()
            if not line:
                break
            if check_safe(line):
                count+=1
            else:
                if check_again(line):
                    count+=1
            
    return count
print(new_safe_reports())
