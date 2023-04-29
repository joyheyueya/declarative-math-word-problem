from utils import *
from prompts.declarative_three_shot import DECLARATIVE_THREE_SHOT_AND_PRINCIPLES

question = 'Bob says to Alice: if you give me 3 apples and then take half of my apples away, then I will be left with 13 apples. How many apples do I have now?'
eq_list = get_declarative_equations(model='code-davinci-002', question=question, prompt=DECLARATIVE_THREE_SHOT_AND_PRINCIPLES, max_tokens=600, stop_token='\n\n\n', temperature=0)
answer = get_final_using_sympy(eq_list)
print(answer)