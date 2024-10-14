if __name__ == '__main__':
    studentDetails = []
    Scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Scores.append(score)
        studentDetails.append([name, score])
        
    uniqueScore = sorted(set(i[1] for i in studentDetails))
    secondHighestScore = uniqueScore[1]
    Names = []
    
    for i in studentDetails:
        if i[1] == secondHighestScore:
            Names.append(i[0])
    
    for name in sorted(Names):
        print(name)
