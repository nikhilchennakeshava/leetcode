class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)

        # salary_sort = sorted(salary)
        # salary_sort.pop(0)
        # salary_sort.pop()

        # return sum(salary_sort)/len(salary_sort)
