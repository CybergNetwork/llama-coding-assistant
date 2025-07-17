class PreciseCodeEditor:
    def __init__(self, code_parser):
        self.parser = code_parser
        self.edit_history = []
    
    def edit_single_line(self, file_content, line_number, new_line, validation=True):
        """Edit a single line in the code"""
        lines = file_content.split('\n')
        
        if line_number < 1 or line_number > len(lines):
            raise ValueError(f"Line number {line_number} out of range")
        
        # Store original state
        original_line = lines[line_number - 1]
        self.edit_history.append({
            'type': 'line_edit',
            'line_number': line_number,
            'original': original_line,
            'new': new_line,
            'timestamp': time.time()
        })
        
        # Apply edit
        lines[line_number - 1] = new_line
        new_content = '\n'.join(lines)
        
        # Validate syntax if requested
        if validation:
            if not self.validate_syntax(new_content):
                # Rollback on syntax error
                self.rollback_last_edit()
                raise SyntaxError("Edit would result in syntax error")
        
        return new_content
    
    def edit_multiple_lines(self, file_content, edits):
        """Apply multiple line edits atomically"""
        # edits: [(line_number, new_content), ...]
        lines = file_content.split('\n')
        
        # Sort edits by line number (descending to avoid index shifts)
        edits.sort(key=lambda x: x[0], reverse=True)
        
        for line_number, new_content in edits:
            if line_number < 1 or line_number > len(lines):
                continue
            lines[line_number - 1] = new_content
        
        return '\n'.join(lines)
    
    def validate_syntax(self, code, language='python'):
        """Validate code syntax"""
        try:
            if language == 'python':
                ast.parse(code)
            return True
        except SyntaxError:
            return False
    
    def rollback_last_edit(self):
        """Rollback the last edit"""
        if not self.edit_history:
            return None
        
        last_edit = self.edit_history.pop()
        # Implementation for rollback
        return last_edit
        
class CodeContextAnalyzer:
    def __init__(self, llama_agent, code_parser):
        self.agent = llama_agent
        self.parser = code_parser
    
    def analyze_code_intent(self, code_snippet, context=""):
        """Analyze what the code is trying to do"""
        prompt = f"""
        Analyze the following code and explain its purpose, identify potential issues, and suggest improvements:
        
        Context: {context}
        
        Code:
        ```
        {code_snippet}
        ```
        
        Please provide:
        1. Purpose and functionality
        2. Potential issues or bugs
        3. Suggestions for improvement
        4. Dependencies and imports needed
        """
        
        return self.agent.generate_response(prompt)
    
    def suggest_line_edit(self, file_content, line_number, desired_change):
        """Suggest specific line edit based on desired change"""
        lines = file_content.split('\n')
        current_line = lines[line_number - 1]
        
        # Get surrounding context
        context_lines, start_idx = self.parser.get_line_context(
            file_content, line_number - 1, context_size=10
        )
        
        context_code = '\n'.join(context_lines)
        
        prompt = f"""
        You are a precise code editor. Given the following code context and a specific line that needs to be changed, provide ONLY the new line content.
        
        Current line {line_number}: {current_line}
        Desired change: {desired_change}
        
        Context:
        ```
        {context_code}
        ```
        
        Provide only the replacement line, maintaining proper indentation and syntax.
        """
        
        return self.agent.generate_response(prompt)
