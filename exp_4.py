import ply.lex as lex
import ply.yacc as yc 
import sys
sys.modules['__main__'].__file__ = 'app.py'

tokens = ('NUMBER' , 'PLUS' , 'TIMES')

t_PLUS = r'\+'
t_TIMES = r'\*'
t_ignore = '\t'

def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_error(t):
   print(f"Illegal char : '{t.value(0)}'")
   t.lexer.skip(1)

lexer = lex.lex()

def p_expression_plex_minus(p):
   '''expression : expression PLUS term'''
   p[0] = p[1] + p[3]


def p_expression_term(p):
   '''expression : term'''
   p[0] = p[1]

def p_term_times_divide(p):
    '''term : term TIMES factor'''
    p[0] = p[1] * p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
   'factor : NUMBER'
   p[0] = p[1]

def p_error(p):
   print('Syntax Error')

parser = yc.yacc(write_tables = False)
expr = input("Enter arithmetic expression:")
result = parser.parse(expr)
print("Result =", result)