import logging
from datetime import datetime

class AgentMonitor:
    def __init__(self):
        self.setup_logging()
        self.metrics = {
            'requests_processed': 0,
            'errors': 0,
            'avg_response_time': 0,
            'code_edits_made': 0
        }
    
    def setup_logging(self):
        """Setup comprehensive logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('agent.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger('CodeAgent')
    
    def log_interaction(self, user_input, agent_response, execution_time):
        """Log user interactions"""
        self.logger.info(f"User Input: {user_input[:100]}...")
        self.logger.info(f"Agent Response: {agent_response[:100]}...")
        self.logger.info(f"Execution Time: {execution_time:.2f}s")
        
        # Update metrics
        self.metrics['requests_processed'] += 1
        self.metrics['avg_response_time'] = (
            (self.metrics['avg_response_time'] * (self.metrics['requests_processed'] - 1) + execution_time) 
            / self.metrics['requests_processed']
        )
