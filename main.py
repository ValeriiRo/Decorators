import time
import os


def save_decor(calculation_function):

    def save(*args, **kwargs):
        text_file = open("logger.txt", "w")
        Creation_time = time.ctime()
        arguments = ''
        for argument in args:
            arguments += str(argument) + ' '
        result = calculation_function(*args, **kwargs)
        path_to_logs = os.path.join(os.getcwd(), 'text_file.txt')
        text_file.write(f'date of function call: {Creation_time}\nfunction name: {calculation_function.__name__}\nattribute name: {arguments}\nreturn value: {result}\npath to logs:{path_to_logs}')
        print(f"Файл сохранён: {path_to_logs}")
        return result
    return save

@save_decor
def function_operation(variable_1, variable_2):
    return variable_1 + variable_2

function_operation(3, 9)