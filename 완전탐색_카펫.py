def getMyDivisor(n):
    divisorsList = []
    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append([i, int(n/i)])
    return divisorsList
        
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    div_dict = getMyDivisor(total)
    
    for divs in div_dict:
        row = divs[0]
        column = divs[1]
        if(row > 2 and column > 2):
            if((row-2) * (column-2) == yellow):
                if(row > column):
                    answer = [row, column]
                else:
                    answer = [column, row]
    
    return answer