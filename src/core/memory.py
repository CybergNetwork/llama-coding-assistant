class AgentMemory:
    def __init__(self, max_context_length=4000):
        self.conversation_history = []
        self.code_context = {}
        self.max_context_length = max_context_length
    
    def add_interaction(self, user_input, agent_response, code_changes=None):
        """Add interaction to memory"""
        interaction = {
            'timestamp': time.time(),
            'user_input': user_input,
            'agent_response': agent_response,
            'code_changes': code_changes or []
        }
        self.conversation_history.append(interaction)
        
        # Trim history if too long
        self.trim_history()
    
    def get_relevant_context(self, query, max_interactions=5):
        """Get relevant context for current query"""
        recent_interactions = self.conversation_history[-max_interactions:]
        context = []
        
        for interaction in recent_interactions:
            context.append(f"User: {interaction['user_input']}")
            context.append(f"Assistant: {interaction['agent_response']}")
        
        return '\n'.join(context)
    
    def trim_history(self):
        """Keep memory within context length limits"""
        while len(self.conversation_history) > 20:
            self.conversation_history.pop(0)
