import ply.lex as lex
import sys

tkns = (
    'IDENTIFIERS','LITERALS','PLUS','MINUS','DVIDE','LP','RP','MULTIPLY','ASSINMENT','TERMINATOR'    
)

t_plus = r'\+'
t_minus = r'-'
t_mul = r'\*'
t_div = r'/'
t_as = r'='
t_lp = r'\('
t_rp = r'\)'

print(r'[a-zA-Z_][a-zA-Z0-9_]*')

def t_id(t):
