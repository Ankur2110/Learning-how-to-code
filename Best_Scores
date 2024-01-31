#Given a list, write a function to get first, second best scores from the list. List may contain duplicates.

def best_score(scores_list):
    max1, max2 =  float('-inf'), float('-inf')
    for num in scores_list:
        if num> max1:
            max2= max1
            max1 = num
        elif num>max2 and num != max1:
            max2= num
    return max1, max2




# def best_score(list_of_scores):
#     list_of_scores.sort(reverse=True)
#     set1=set()
#     for i in range(len(list_of_scores)):
#         set1.add(list_of_scores[i])
#     score_list =list(set1)
    
#     return score_list[0], score_list[1]



print(best_score([1,9,9,9,8,7,10,12,14,14,55,66,23,12412,9]))


