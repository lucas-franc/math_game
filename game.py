from models.calculate import Calculate


def main() -> None:
    points: int = 0
    gaming(points)


def gaming(points: int) -> None:
    difficulty: int = int(input('What difficulty you want? [1, 2, 3 or 4]: '))

    calc: Calculate = Calculate(difficulty)

    print('What is the result for the operation: ')
    calc.view_operation()

    result: int = int(input())

    if calc.check_result(result):
        points += 1
        print(f'You have {points} points.')

    continue_game: int = int(
        input('You want continue the game? [1 - yes, 0 - no]: '))

    if continue_game:
        gaming(points)
    else:
        print(f'You finished with {points} point(s)')


if __name__ == '__main__':
    main()
