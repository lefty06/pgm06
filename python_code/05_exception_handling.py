#!/usr/bin/python

'''
    #OK https://www.programiz.com/python-programming/exception-handling
    
    try:
        <body>
    except <ExceptionType1>:
        <handler1>
    except <ExceptionTypeN>:
        <handlerN>
    except:
        <handlerExcept>
    else:
        <process_else>
    finally:
        <process_finally>

    except  clause is similar to elif . When exception occurs, it is checked to match the exception type in except  clause. 
    If match is found then handler for the matching case is executed. Also note that in last except  clause ExceptionType  is omitted. 
    If exception does not match any exception type before the last except  clause, then the handler for last except  clause is executed.

    Note: Statements under the else  clause run only when no exception is raised.
    Note: Statements in finally  block will run every time no matter exception occurs or not.
'''


def test01(num1, num2):
    print("Function name: {}\n".format(test01.__name__))

    try:
        # Note: The eval()  function lets a python program run python code within itself, eval()  expects a string argument.
        # num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
        result = num1 / num2
        print("Result is {}".format(result))

    except ZeroDivisionError:
        print("Division by zero is error !!")

    except SyntaxError:
        print("Comma is missing. Enter numbers separated by comma like this 1, 2")

    except:
        print("Wrong input")

    else:
        print("No exceptions")

    finally:
        print("This will execute no matter what")


def test02(num1, num2):
    print("Function name: {}\n".format(test02.__name__))

    try:
        result = num1 / num2
        print("Result is {}".format(result))

    except (TypeError, ValueError):
        # handle multiple exceptions
        # TypeError and ZeroDivisionError
        pass

    except ZeroDivisionError as ex:
        print("Exception:\n{}".format(ex))


def main():
    test02(22222, 0)


if __name__ == '__main__':
    main()
