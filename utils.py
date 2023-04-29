import openai
import re
import numpy as np
from sympy import solve, sympify, Symbol
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor


def reformat_incre_equations(x):
    result = ''
    if len(x) >= 1:
        for eq in x:
            if len(result) == 0:
                result += eq[2 : -2]
            else:
                result += ', ' + eq[2 : -2]
    return result


def reformat_equations_from_peano(eq_list):
    result = ''
    for eq in eq_list.split(','):
        if 'eq' in eq:
            if len(result) == 0:
                result += eq[eq.index('eq') + 2:]
            else:
                result += ', ' + eq[eq.index('eq') + 2:]
        elif 'answer' in eq:
            if len(result) == 0:
                result += eq[eq.index('answer') + 6:].strip() + ' = ?'
            else:
                result += ', ' + eq[eq.index('answer') + 6:].strip() + ' = ?'     
    return result


def get_declarative_equations(model, question, prompt, max_tokens, stop_token, temperature):
    prompt = prompt.format(question=question)
    
    response = openai.Completion.create(
        model = model,
        prompt = prompt,
        max_tokens = max_tokens,
        stop = stop_token,
        temperature = temperature,
        top_p = 1
    )           

    result = response['choices'][0]['text']
    eq_list = re.findall(r'\[\[.*?\]\]', result)
    if len(eq_list) > 0:            
        return reformat_equations_from_peano(reformat_incre_equations(eq_list))
    else:
        print()
        print(response['choices'][0]['text'])
        return response['choices'][0]['text']


def get_final_using_sympy(equations):
    try:
        transformations = (standard_transformations + (implicit_multiplication_application,) + (convert_xor,))
        if str(equations) == 'nan':
            return np.nan
        equation_list = equations.split(',')
        for eq in equation_list:
            for c in range(len(eq)):
                if c < len(eq) - 2:
                    if eq[c].isalpha() and eq[c+1].isalpha() and eq[c+2].isalpha():
                        return 'invalid equations'

        goal_var = None
        goal_expression_list = []
            
        if equation_list[-1].split('=')[0].strip().isalpha() or len(equation_list[-1].split('=')[0].strip()) == 2:
            goal_var = equation_list[-1].split('=')[0].strip()
        elif '=' in equation_list[-1]:
            for l in list(string.ascii_lowercase) + list(string.ascii_uppercase):
                if l not in equation_list[-1]:
                    goal_var = l
                    break
            if goal_var is not None:
                goal_expression = goal_var + ' - (' + equation_list[-1].split('=')[0].strip() + ')'
                goal_expression = parse_expr(goal_expression, transformations=transformations)
                goal_expression = sympify(goal_expression)
                try:
                    return float(solve(goal_expression)[0])
                except Exception as e:
                    pass
                goal_expression_list.append(goal_expression)
            else:
                return 'invalid equations'

        if len(equation_list) == 1:
            try:
                goal_expression = parse_expr(equation_list[0].split('=')[0], transformations=transformations)
                return float(sympify(goal_expression))
            except Exception as e:
                return 'invalid equations'

        if goal_var == None:
            return 'no goal found'

        for i in range(len(equation_list) - 1):
            sub_eqs = equation_list[i]  
            if '?' not in sub_eqs:
                try:    
                    sub_eqs_split = sub_eqs.split('=')
                    sub_eqs = sub_eqs_split[0].strip() + ' - (' + sub_eqs_split[1].strip() + ')'
                    sub_eqs = parse_expr(sub_eqs, transformations=transformations)
                    sub_eqs = sympify(sub_eqs)
                except Exception as e:
                    return 'invalid equations'
                goal_expression_list.append(sub_eqs)

                try:
                    try:
                        return float(solve(goal_expression_list)[Symbol(goal_var)])
                    except Exception as e:
                        return float(solve(goal_expression_list)[0][Symbol(goal_var)])
                except Exception as e:
                    pass

        return 'no solution'
    except Exception as e:
        print(e)
        return 'bug'
  