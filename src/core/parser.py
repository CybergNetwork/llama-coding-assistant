import tree_sitter
from tree_sitter import Language, Parser
import ast
import re

class CodeParser:
    def __init__(self):
        # Initialize tree-sitter parsers for different languages
        self.parsers = {}
        self.setup_parsers()
    
    def setup_parsers(self):
        # Setup for Python
        python_lang = Language('path/to/tree-sitter-python.so', 'python')
        python_parser = Parser()
        python_parser.set_language(python_lang)
        self.parsers['python'] = python_parser
        
        # Setup for JavaScript
        js_lang = Language('path/to/tree-sitter-javascript.so', 'javascript')
        js_parser = Parser()
        js_parser.set_language(js_lang)
        self.parsers['javascript'] = js_parser
    
    def parse_code(self, code, language='python'):
        """Parse code and return AST"""
        parser = self.parsers.get(language)
        if not parser:
            raise ValueError(f"Unsupported language: {language}")
        
        tree = parser.parse(bytes(code, 'utf8'))
        return tree
    
    def find_function_boundaries(self, code, function_name):
        """Find start and end lines of a specific function"""
        tree = self.parse_code(code)
        # Implementation for finding function boundaries
        # Returns (start_line, end_line)
        pass
    
    def get_line_context(self, code, line_number, context_size=5):
        """Get context around a specific line"""
        lines = code.split('\n')
        start = max(0, line_number - context_size)
        end = min(len(lines), line_number + context_size + 1)
        return lines[start:end], start
