def add_inputs(input_1: float, input_2: float, *extra) -> float:
    """
    adds 2 or more numbers together

        :param input_1: first number
        :type input_1: float
        :param input_2: second number
        :type input_2: float
        :return: all the inputs added together
        :rtype: float
    """
    total = input_1 + input_2

    for curr_num in extra:
        total += curr_num

    return total
