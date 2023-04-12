DECLARATIVE_EIGHT_SHOT = '''
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?

Peano solution:


Let a be the amount of money Olivia started with [[var a]]. We're given [[eq a = 23]]. 
Let b be the number of bagels she bought [[var b]]. We're given [[eq b = 5]].
Let c be how much each bagel costs [[var c]]. We're given [[eq c = 3]].
Let d be the total amount of money she spent on bagels [[var d]]. We have [[eq d = b * c]].
Let e be the amount of money she has left [[var e]]. We have [[eq e = a - d]].
The answer is the value of e [[answer e]].





Q: Michael had 58 golf balls. On tuesday, he lost 23 golf balls. On wednesday, he lost 2 more. How many golf balls did he have at the end of wednesday?

Peano solution:


Let a be the number of golf balls Michael started with [[var a]]. We're given [[eq a = 58]]. 
Let b be the number of golf balls he lost on tuesday [[var b]]. We're given [[eq b = 23]].
Let c be the number of golf balls he lost on wednesday [[var c]]. We're given [[eq c = 2]].
Let d be the number of golf balls he had left [[var d]]. We have [[eq d = a - b - c]].
The answer is the value of d [[answer d]].





Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

Peano solution:


Let a be the number of computers in the room [[var a]]. We're given [[eq a = 9]]. 
Let b be the number of computers installed each day [[var b]]. We're given [[eq b = 5]].
Let c be the number of days computers were installed [[var c]]. Since computers were installed from monday to thursday, we know that [[eq c = 4]].
Let d be the number of computers installed [[var d]]. We have [[eq d = b*c]].
Let e be the total number of computers in the room now [[var e]]. We have [[eq e = a + d]].
The answer is the value of e [[answer e]].





Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

Peano solution:


Let a be the number of toys Shawn started [[var a]]. We're given [[eq a = 5]]. 
Let b be the number of toys Shawn got for Christmas [[var b]]. We're given [[eq b = 2]].
Let c be the number of toys Shawn has now [[var c]]. We have [[eq c = a + b]].
The answer is the value of c [[answer c]].





Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

Peano solution:


Let a be the number of lollipops Jason had [[var a]]. We're given [[eq a = 20]]. 
Let b be the number of lollipops Jason gave Denny [[var b]].
Let c be the number of lollipops Jason has now [[var c]]. We have [[eq c = a - b]]. We're given that [[eq c = 12]].
The answer is the value of b [[answer b]].





Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?

Peano solution:


Let a be the number of chocolates Leah had [[var a]]. We're given [[eq a = 32]]. 
Let b be the number of chocolates her sister had [[var b]]. We're given [[eq b = 42]]. 
Let c be the number of chocolates Leah and her sister had in total [[var c]]. We have [[eq c = a + b]]. 
Let d be the number of chocolates they ate [[var d]]. We're given [[eq d = 35]]. 
Let e be the number of chocolates Leah and her sister have left [[var e]]. We have [[eq e = c - d]]. 
The answer is the value of e [[answer e]].





Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?

Peano solution:


Let a be the number of cars in the parking lot [[var a]]. We're given [[eq a = 3]]. 
Let b be the number of cars arrived [[var b]]. We're given [[eq b = 2]]. 
Let c be the number of cars in the parking lot now [[var c]]. We have [[eq c = a + b]]. 
The answer is the value of c [[answer c]].





Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees did the grove workers plant today?

Peano solution:


Let a be the number of trees in the grove [[var a]]. We're given [[eq a = 15]]. 
Let b be the number of trees Grove workers will plant [[var b]].
Let c be the number of trees in the grove after the workers are done [[var c]]. We have [[eq c = a + b]]. We're given [[eq c = 21]].
The answer is the value of b [[answer b]].





Q: {question}

Peano solution:
'''.strip() + '\n\n\n'