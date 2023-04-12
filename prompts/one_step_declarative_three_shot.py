ONE_STEP_DECLARATIVE_THREE_SHOT = '''
Q: Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?

Peano solution:


[[eq a = (5 - 2) + (5 - 2)]]
[[answer a]]





Q: Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?

Peano solution:


[[eq a = (10 - 3) / 2]]
[[answer a]]





Q: The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?

Peano solution:


[[eq a = 2 / 2 * 7 * 24]]
[[answer a]]





Q: {question}

Peano solution:
'''.strip() + '\n\n\n'