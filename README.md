# Solving Math Word Problems by Combining Language Models With Symbolic Solvers

This is the repo for the paper: [Solving Math Word Problems by Combining Language Models With Symbolic Solvers](https://arxiv.org/pdf/2304.09102.pdf).

## Usage
To solve a math word problem, we first formalize the word problem as a set of variables and equations and then use `SymPy` to solve the equations.

Set the OpenAI key before running the script:
```export OPENAI_API_KEY='sk-...'```

```
from utils import *
from prompts.declarative_three_shot import DECLARATIVE_THREE_SHOT_AND_PRINCIPLES

question = 'xxx'
eq_list = get_declarative_equations(model='code-davinci-002', question=question, prompt=DECLARATIVE_THREE_SHOT_AND_PRINCIPLES, max_tokens=600, stop_token='\n\n\n', temperature=0)
answer = get_final_using_sympy(eq_list)
```

The `get_declarative_equations` method calls the OpenAI API to generate the equations, and the `get_final_using_sympy` method solves the equations to get the final answer (see an example in `run.py`).