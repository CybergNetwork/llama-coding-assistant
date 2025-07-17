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
