from utilities.logger_creator import logger_creator

def add_int(x: int, y: int) -> int:
    #add type hints to variables for clairity

    '''
    Add two integers
    :param x: an integer
    :param y: an integer
    :return: the sum of the two integers
    '''
    #use doc str for documentation, help()

    assert type(x) == int
    assert type(y) == int
    #use assertion to ensure input data meet requirements

    int_x = int(x)
    int_y = int(y)
    result = int_x + int_y

    return result

if __name__ == '__main__':
    from pathlib import Path
    from datetime import datetime
    save_dir = Path('logs')
    logger, warnings_logger = logger_creator(save_dir.joinpath(f'add_two_int_main_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'))
    x = 1
    y = 2
    result = add_int(x=x, y=y)
    #use debug to find out how does the function work step by step or if there was an error.
    logger.info(f'The result of adding {x} and {y} is: {result}')
    #use pythong logging instead of printing to save important messages into files.