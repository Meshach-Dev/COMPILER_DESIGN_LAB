import ply.lex as lex
import ply.yacc as yc 
import sys
sys.modules['__main__'].__file__ = 'app.py'

tokens = ('NUMBER' , 'PLUS' , 'TIMES', 'LPAREN' , 'RPAREN' , 'DIVIDE' , 'MINUS')

t_PLUS = r'\+'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'
t_MINUS = r'-'

def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_error(t):
   print(f"Illegal char : '{t.value(0)}'")
   t.lexer.skip(1)

lexer = lex.lex()

def p_expression_binop_minus(p):
   '''expression : expression PLUS term'''
   p[0] = p[1] - p[3]

def p_expression_binop_plus(p):
   '''expression : expression MINUS term'''
   p[0] = p[1] + p[3]

def p_expression_term(p):
   '''expression : term'''
   p[0] = p[1]

def p_term_binop_times(p):
    '''term : term TIMES factor'''
    p[0] = p[1] * p[3]

def p_term_binop_divide(p):
    '''term : term DIVIDE factor'''
    p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
   'factor : NUMBER'
   p[0] = p[1]

def p_factor_group(p):
   'factor : LPAREN expression RPAREN'
   p[0] = p[2]

def p_error(p):
   print('Syntax Error')

parser = yc.yacc(write_tables = False)
expr = input("Enter arithmetic expression:")
result = parser.parse(expr)
print("Result =", result)