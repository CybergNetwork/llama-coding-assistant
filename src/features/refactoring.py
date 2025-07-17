class RefactoringAgent:
    def __init__(self, llama_agent, code_parser):
        self.agent = llama_agent
        self.parser = code_parser
    
    def suggest_refactoring(self, code, refactoring_type="general"):
        """Suggest code refactoring improvements"""
        prompt = f"""
        Analyze the following code and suggest {refactoring_type} refactoring improvements:
        
        Code:
        ```
        {code}
        ```
        
        Provide specific refactoring suggestions with:
        1. What to change
        2. Why it should be changed
        3. The exact replacement code
        4. Benefits of the change
        
        Focus on: code clarity, performance, maintainability, and best practices.
        """
        
        return self.agent.generate_response(prompt)
    
    def extract_function(self, code, start_line, end_line, function_name):
        """Extract code block into a new function"""
        lines = code.split('\n')
        extracted_lines = lines[start_line-1:end_line]
        
        # Analyze variables and dependencies
        analysis_prompt = f"""
        Analyze the following code block and determine:
        1. Input parameters needed
        2. Return value
        3. Local variables that shouldn't be parameters
        
        Code block:
        ```
        {''.join(extracted_lines)}
        ```
        
        Provide the function signature and any necessary modifications.
        """
        
        analysis = self.agent.generate_response(analysis_prompt)
        
        # Generate the extracted function
        function_prompt = f"""
        Create a function named '{function_name}' from the analyzed code block:
        
        Analysis: {analysis}
        
        Original code:
        ```
        {''.join(extracted_lines)}
        ```
        
        Provide:
        1. The complete function definition
        2. The function call to replace the original code
        """
        
        return self.agent.generate_response(function_prompt)
