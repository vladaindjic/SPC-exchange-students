from pygments.lexers import PythonLexer


def show_tokens(text, lexer):
    # The "lexer" does lexical analysis of "text" and shows the recognized tokens.
    for token_type, token_str in lexer.get_tokens(text):
        print("The token: \"%s\" of type: \"%s\"\n" % (token_str, token_type))
        pass


if __name__ == '__main__':
    show_tokens(open('test.py', 'r').read(), PythonLexer())
