class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        for i in range(len(operations)):
            if operations[i].isdigit():
                values.append(int(operations[i]))
            if operations[i] == "+":
                values.append(int(values[-1]) + int(values[-2]))
            if operations[i] == "C":
                values.pop()
            if operations[i] == "D":
                values.append(int(values[-1]) * 2)
        return sum(values)

        