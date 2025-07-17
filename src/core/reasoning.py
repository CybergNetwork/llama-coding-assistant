class ReasoningEngine:
    def __init__(self, llama_agent):
        self.agent = llama_agent
    
    def plan_code_changes(self, request, codebase_context):
        """Plan multi-step code changes"""
        planning_prompt = f"""
        You are a senior software engineer planning code changes. Break down the following request into specific, actionable steps:
        
        Request: {request}
        Codebase context: {codebase_context}
        
        Provide a step-by-step plan with:
        1. Files to modify
        2. Specific changes needed
        3. Dependencies to consider
        4. Testing requirements
        5. Risk assessment
        
        Format as JSON:
        {{
            "steps": [
                {{
                    "step": 1,
                    "description": "...",
                    "files": ["file1.py", "file2.py"],
                    "changes": ["specific change description"],
                    "risks": ["potential issues"]
                }}
            ]
        }}
        """
        
        return self.agent.generate_response(planning_prompt)
    
    def execute_plan(self, plan, file_manager, code_editor):
        """Execute the planned changes"""
        results = []
        
        for step in plan.get('steps', []):
            step_result = {
                'step': step['step'],
                'description': step['description'],
                'status': 'pending',
                'changes': []
            }
            
            try:
                # Execute each change in the step
                for file_path in step['files']:
                    content = file_manager.read_file(file_path)
                    if content:
                        # Process changes for this file
                        for change in step['changes']:
                            modified_content = self.apply_change(
                                content, change, code_editor
                            )
                            file_manager.write_file(file_path, modified_content)
                            step_result['changes'].append({
                                'file': file_path,
                                'change': change,
                                'status': 'success'
                            })
                
                step_result['status'] = 'completed'
                
            except Exception as e:
                step_result['status'] = 'failed'
                step_result['error'] = str(e)
            
            results.append(step_result)
        
        return results
