from random import randint


class Calculate:
    def __init__(self: object, difficulty: int) -> None:
        self.__difficulty: int = difficulty
        self.__value1: int = self._generate_value
        self.__value2: int = self._generate_value
        # 1 = sum, 2 = subtraction, 3 = multiplication
        self.__operation: int = randint(1, 3)
        self.__result: int = self._generate_result

    @property
    def difficulty(self: object) -> int:
        return self.__difficulty

    @property
    def value1(self: object) -> int:
        return self.__value1

    @property
    def value2(self: object) -> int:
        return self.__value2

    @property
    def operation(self: object) -> int:
        return self.__operation

    @property
    def result(self: object) -> int:
        return self.__result

    def __str__(self: object) -> str:
        op: str = ''
        if self.operation == 1:
            op = 'Sum'
        elif self.operation == 2:
            op = 'Subtraction'
        elif self.operation == 3:
            op = 'Multiplicate'
        else:
            op = 'unknown operation'
        return f'Value 1: {self.value1} \nValue 2: {self.value2} \nDifficulty: {self.difficulty} \nOperation: {op}'

    @property
    def _generate_value(self: object) -> int:
        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(0, 100)
        elif self.difficulty == 3:
            return randint(0, 1000)
        elif self.difficulty == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _generate_result(self: object) -> int:
        if self.operation == 1:
            return self.value1 + self.value2
        elif self.operation == 2:
            return self.value1 - self.value2
        else:
            return self.value1 * self.value2

    @property
    def _op_symbol(self: object) -> str:
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        else:
            return '*'

    def check_result(self: object, right_result: int) -> bool:
        right: bool = False

        if self.result == right_result:
            print('Resposta correta')
            right = True
        else:
            print('Resposta erra!')
        print(f'{self.value1} {self._op_symbol} {self.value2} = {self.result}')
        return right

    def view_operation(self: object) -> None:
        print(f'{self.value1} {self._op_symbol} {self.value2} = ?')
