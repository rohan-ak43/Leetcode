class Solution(object):
    def countSeniors(self, details):
        count = 0
        for i in details:
            if i[11] >= "7":
                count += 1 
            elif i[11] == "6":
                if i[12] > "0":
                    count += 1  
        return count