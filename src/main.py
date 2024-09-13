# TEAM 01
# González Arredondo Rafael
# González Casanova Gallegos Renato Alfonso
# Juárez Herrera Erick Adrián
# Pineda Galino Ricardo Angel
# Sánchez Durán Danae

# Import of the library "ply", module "lexer"
import ply.lex as lexer

# Dictionary for the "KEYWORDS" that the lexer will be able
# to handle.
keywords = {'printf':'KEYWORD',
            'if':'KEYWORD',
            'return' : 'KEYWORD',
            'int' : 'KEYWORD',
            'IF' : 'KEYWORD',
            'RETURN' : 'KEYWORD',
            'INT' : 'KEYWORD'
            }


# List with the token names
tokens = [
    'CONSTANT', 
    'IDENTIFIER',
    'OPERATOR', 
    'LITERAL', 
    'PUNCTUATION', 
    'KEYWORD'
 ] 

# Regular expression for the tokens (with action code)
def t_CONSTANT(t):
    r'-?\d+'  # We define the regex being able to have an optional
              # negative symbol just before the number itself.
    t.value = int(t.value) # We transform the number identified in the regex to
                           # according data type
    return t   

# Regular expressions for the tokens (without action code)
#Preference for rational operators == <= >=
t_OPERATOR = r'==|<=|>=|[=+\-*/%<>]'
t_PUNCTUATION = r'[(){}\[\],;]'
t_LITERAL = r'"[^"]*"|\'[^\']*\''

# Regular expression for the tokens (with action code)
def t_IDENTIFIER(t):
    
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    
    t.type = keywords.get(t.value,'IDENTIFIER') # Check for reserved words, if not
                                                # they're identifiers
    return t

#Function t_IDENTIFIER: This functions stablishes "t.type" in
#"KEYWORD" if the token's value is found in the dictionary "keywords", if not, it classifies 
#it as "IDENTIFIER".


# Rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# String to store the ignored characters
t_ignore = ' \t'

# Error handling rule 
def t_error(t):
    print("Caracter ilegal '%s'" %t.value[0])
    t.lexer.skip(1)

# Creation of the lexical analyzer
lexical_analyzer = lexer.lex()

# Declaration of the example code 
data = '''
int main(){
int x, a=2, b=3, c=5;
 2+-4-4

if(4<5){
    x = a+b*c;
}

if(4<=5){
    x = a+b*c;
}

if(5>4){
    x = a+b*c;
}

if(5>=4){
    x = a+b*c;
}

if(4==4){
    x = a+b*c;
}

printf("The value of x is");
printf(x);

return 0;
}
'''

# Lexer's input
lexical_analyzer.input(data)

# Counting variables
a = 0
b = 1

# Start of the tokenization process
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(b,'-->',tok.type,'-->', tok.value)
    a = a + 1
    b = b + 1

# Total amount of tokens
print("Cantidad total de tokens: ", a)