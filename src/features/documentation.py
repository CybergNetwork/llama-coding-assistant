class DocumentationGenerator:
    def __init__(self, llama_agent):
        self.agent = llama_agent
    
    def generate_docstring(self, function_code):
        """Generate comprehensive docstring for a function"""
        prompt = f"""
        Generate a comprehensive docstring for the following function:
        
        ```python
        {function_code}
        ```
        
        Include:
        1. Brief description
        2. Parameters with types and descriptions
        3. Return value with type and description
        4. Raises section if applicable
        5. Example usage
        
        Use Google-style docstring format.
        """
        
        return self.agent.generate_response(prompt)
    
    def generate_readme(self, project_structure, main_files):
        """Generate project README"""
        prompt = f"""
        Generate a comprehensive README.md for a project with the following structure:
        
        Project structure:
        {project_structure}
        
        Main files:
        {main_files}
        
        Include:
        1. Project description
        2. Installation instructions
        3. Usage examples
        4. API documentation
        5. Contributing guidelines
        6. License information
        """
        
        return self.agent.generate_response(prompt)
