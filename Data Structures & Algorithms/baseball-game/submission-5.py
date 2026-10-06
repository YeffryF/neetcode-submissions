class Solution:
    def calPoints(self, operations: List[str]) -> int:
        values = [5, -2]
        for i in range(len(operations)):
            if operations[i].isdigit():
                values.append(int(operations[i]))
            elif operations[i] == "+":
                values.append(int(values[-1]) + int(values[-2]))
            elif operations[i] == "C":
                values.pop()
            elif operations[i] == "D":
                values.append(int(values[-1]) * 2)
        return sum(values)

        