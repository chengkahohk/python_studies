while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('That\'s ValueError!')
    except KeyboardInterrupt:
        print('That\'s KeyboardInterrupt!')
    finally:
        print('\nAttempt Input\n')

print('That ok')
