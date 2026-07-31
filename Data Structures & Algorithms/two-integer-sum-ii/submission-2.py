class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        c = len(numbers)
        i=0
        while i < c :
            j=0
            a = target - numbers[i]
            if(a in numbers):
                while j < c:
                    if((numbers[j]==a) & (j!=i)):
                        if(j<i):
                            l=[j+1,i+1]
                            return l
                        else:
                            l=[i+1,j+1]
                            return l
                    j=j+1
            i=i+1



        