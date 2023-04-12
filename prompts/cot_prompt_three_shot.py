COT_PROMPT_THREE_SHOT = '''
Q: Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?

A:


Mary had 5 apples and ate 2 apples, so she had 5 - 2 = 3 apples left. She bought 3 apples, so she ended up with 3 + 3 = 6 apples. The answer is 6.





Q: Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?

A:


Luigi had 3 more years of experience than Mario, and they have 10 years of experience in total. So Mario had (10 - 3)/2 = 3.5 years of expereinces. The answer is 3.5.





Q: The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?

A: 


One revolution takes 2 weeks, so half a revolution takes 2 / 2 = 1 week. One week is 1 * 7 * 24 = 168 hours. So half a revolution takes 168 hours. The answer is 168.





Q: {question}

A:
'''.strip() + '\n\n\n'