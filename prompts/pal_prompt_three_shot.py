PAL_PROMPT_THREE_SHOT = '''
Q: Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?

# solution in Python:


def solution():
    """Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?"""
    apple_initial = 5
    apple_eaten = 2
    apple_left = apple_initial - apple_eaten
    apple_bought = apple_left
    result = apple_left + apple_bought
    return result





Q: Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?

# solution in Python:


def solution():
    """Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?"""
    mario_experience = (10 - 3)/2
    result = mario_experience
    return result





Q: The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?

# solution in Python:


def solution():
    """The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?"""
    one_revolution_week = 2
    half_revolution_week = one_revolution_week/2
    half_revolution_hour = half_revolution_week * 7 * 24
    result = half_revolution_hour
    return result





Q: {question}

# solution in Python:
'''.strip() + '\n\n\n'