DECLARATIVE_THREE_SHOT = '''
Q: Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?

Peano solution:


Let a be the number of apples Mary started with [[var a]]. We have [[eq a = 5]]. 
Let b be how many apples she had in the morning after eating 2 apples [[var b]]. We have [[eq b = a - 2]]. 
Let c be the apples she bought in the afternoon [[var c]]. 
Since she bought as many as she had after eating, we have [[eq c = b]]. 
Let d be how many apples she ended up with [[var d]]. We have [[eq d = b + c]]. 
The answer is the value of d [[answer d]]. 





Q: Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?

Peano solution:


Let a be the number of years Mario had [[var a]]. 
Let b be the number of years Luigi had [[var b]]. We have [[eq a + b = 10]]. We also have [[eq b = a + 3]]. 
The answer is the value of a [[answer a]].





Q: The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?

Peano solution:


Let a be the number of hours in a week [[var a]]. We have [[eq a = 168]]. 
Let b be the number of hours in a revolution [[var b]]. We have [[eq b = a * 2]]. 
Let c be the number of hours in half a revolution [[var c]]. We have [[eq c = b / 2]]. 
The answer is the value of c [[answer c]].





Q: {question}

Peano solution:
'''.strip() + '\n\n\n'



DECLARATIVE_THREE_SHOT_AND_PRINCIPLES = '''
Let's solve mathematical word problems in a careful, formal manner. The solution will follow the Peano format: 
1- Each sentence in the solution either introduces a new variable or states a new equation. 
2- The last sentence gives the goal: which variable will contain the answer to the problem. 
3- Each equation only uses previously introduced variables. 
4- Each quantity is only named by one variable.
5- Use all the numbers in the question.

Q: Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?

Peano solution:


Let a be the number of apples Mary started with [[var a]]. We have [[eq a = 5]]. 
Let b be how many apples she had in the morning after eating 2 apples [[var b]]. We have [[eq b = a - 2]]. 
Let c be the apples she bought in the afternoon [[var c]]. 
Since she bought as many as she had after eating, we have [[eq c = b]]. 
Let d be how many apples she ended up with [[var d]]. We have [[eq d = b + c]]. 
The answer is the value of d [[answer d]]. 





Q: Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?

Peano solution:


Let a be the number of years Mario had [[var a]]. 
Let b be the number of years Luigi had [[var b]]. We have [[eq a + b = 10]]. We also have [[eq b = a + 3]]. 
The answer is the value of a [[answer a]].





Q: The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?

Peano solution:


Let a be the number of hours in a week [[var a]]. We have [[eq a = 168]]. 
Let b be the number of hours in a revolution [[var b]]. We have [[eq b = a * 2]]. 
Let c be the number of hours in half a revolution [[var c]]. We have [[eq c = b / 2]]. 
The answer is the value of c [[answer c]].





Q: {question}

Peano solution:
'''.strip() + '\n\n\n'



DECLARATIVE_THREE_SHOT_AND_PRINCIPLES_CODEX_SOLVE = '''
Let's solve mathematical word problems in a careful, formal manner. The solution will follow the Peano format: 
1- Each sentence in the solution either introduces a new variable or states a new equation. 
2- The last sentence gives the goal: which variable will contain the answer to the problem. 
3- Each equation only uses previously introduced variables. 
4- Each quantity is only named by one variable.
5- Use all the numbers in the question.

Q: Mary had 5 apples. The next morning, she ate 2 apples. Then, in the afternoon, she bought as many apples as she had after eating those apples in the morning. How many apples did she end up with?

Peano solution:


Let a be the number of apples Mary started with [[var a]]. We have [[eq a = 5]]. 
Let b be how many apples she had in the morning after eating 2 apples [[var b]]. We have [[eq b = a - 2]]. 
Let c be the apples she bought in the afternoon [[var c]]. 
Since she bought as many as she had after eating, we have [[eq c = b]]. 
Let d be how many apples she ended up with [[var d]]. We have [[eq d = b + c]]. 
The answer is the value of d [[answer d = 6]]. 





Q: Mario and Luigi together had 10 years of experience in soccer. Luigi had 3 more than Mario. How many did Mario have?

Peano solution:


Let a be the number of years Mario had [[var a]]. 
Let b be the number of years Luigi had [[var b]]. We have [[eq a + b = 10]]. We also have [[eq b = a + 3]]. 
The answer is the value of a [[answer a = 3.5]].





Q: The planet Goob completes one revolution after every 2 weeks. How many hours will it take for it to complete half a revolution?

Peano solution:


Let a be the number of hours in a week [[var a]]. We have [[eq a = 168]]. 
Let b be the number of hours in a revolution [[var b]]. We have [[eq b = a * 2]]. 
Let c be the number of hours in half a revolution [[var c]]. We have [[eq c = b / 2]]. 
The answer is the value of c [[answer c = 168]].





Q: {question}

Peano solution:
'''.strip() + '\n\n\n'