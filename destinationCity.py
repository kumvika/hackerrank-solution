# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        for i in range(len(paths)):
            count = 0
            for j in range(len(paths)):
                if (i != j) and (paths[i][1] != paths[j][0]):
                    count += 1
            if (count == len(paths)-1):
                return paths[i][1]

#paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
#paths = [["B","C"],["D","B"],["C","A"]]
paths = [["A","Z"]]
s = Solution()
print(s.destCity(paths))