#!/usr/bin/python
def getMaxAverage(marks):
    max_avg = 0
    score_dict = [0, 0]
    for i in range(0,len(marks),4):
        avg_score = (int(marks[i+1]) + int(marks[i+2]) + int(marks[i+3]))/3
        #print("Average Score = " + str(avg_score))
        if max_avg < avg_score:
            max_avg = avg_score
            score_dict = [marks[i], avg_score]
            #print(marks[i], avg_score)
    return score_dict

marks = ["Shrikanth", "100", "90", "80","Ram", "100", "100", "100","Aman", "67","89","94"]
#print(getMaxAverage(marks))
print(getMaxAverage(marks))


