class CodeQualityAnalyzer:
    def __init__(self, llama_agent):
        self.agent = llama_agent
    
    def analyze_code_quality(self, code, file_path=""):
        """Analyze code quality and suggest improvements"""
        prompt = f"""
        Analyze the following code for quality issues and provide specific line-by-line suggestions:
        
        File: {file_path}
        Code:
        ```
        {code}
        ```
        
        Check for:
        1. Code style and formatting
        2. Performance optimizations
        3. Security vulnerabilities
        4. Best practices compliance
        5. Potential bugs
        
        Provide specific line numbers and suggested changes.
        """
        
        return self.agent.generate_response(prompt)
    
    def generate_tests(self, code, test_type="unit"):
        """Generate tests for the given code"""
        prompt = f"""
        Generate comprehensive {test_type} tests for the following code:
        
        Code:
        ```
        {code}
        ```
        
        Include:
        1. Test cases for normal operation
        2. Edge cases
        3. Error conditions
        4. Mock dependencies if needed
        
        Use appropriate testing framework (pytest for Python, Jest for JavaScript, etc.)
        """
        
        return self.agent.generate_response(prompt)
