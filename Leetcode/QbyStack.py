class MyQueue:

    def __init__(self):
        self.input = []
        self.output = []

    def shifter(self):
        for i in range(len(self.input) - 1, -1, -1):
            self.output.append(self.input[i])
            self.input.pop()

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if not self.output and self.input:
            self.shifter()

        return self.output.pop() if len(self.output) > 0 else -1

    def peek(self) -> int:
        if not self.output and self.input:
            self.shifter()
        return self.output[-1] if len(self.output) > 0 else -1

    def empty(self) -> bool:
        print(self.input)
        return True if (len(self.input) == 0 and len(self.output) == 0) else False
