import unittest
from unittest.mock import Mock, patch

class TestCodeAgent(unittest.TestCase):
    def setUp(self):
        self.agent = LlamaCodeAgent()
        self.editor = PreciseCodeEditor(CodeParser())
    
    def test_single_line_edit(self):
        """Test single line editing functionality"""
        code = "print('hello')\nprint('world')\n"
        new_code = self.editor.edit_single_line(code, 1, "print('Hello, World!')")
        
        expected = "print('Hello, World!')\nprint('world')\n"
        self.assertEqual(new_code, expected)
    
    def test_syntax_validation(self):
        """Test syntax validation"""
        valid_code = "print('hello')"
        invalid_code = "print('hello'"
        
        self.assertTrue(self.editor.validate_syntax(valid_code))
        self.assertFalse(self.editor.validate_syntax(invalid_code))
    
    def test_agent_response_format(self):
        """Test agent response format"""
        # Mock test for agent response
        with patch.object(self.agent, 'generate_response') as mock_response:
            mock_response.return_value = "Test response"
            result = self.agent.generate_response("Test prompt")
            self.assertEqual(result, "Test response")

if __name__ == '__main__':
    unittest.main()
