class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.workspace = "/tmp/test_workspace"
        self.file_manager = FileSystemManager(self.workspace)
        self.agent = LlamaCodeAgent()
    
    def test_full_workflow(self):
        """Test complete workflow from request to code change"""
        # Create test file
        test_code = "def greet():\n    print('hello')\n"
        self.file_manager.write_file("test.py", test_code)
        
        # Test editing workflow
        request = "Change the greeting to say 'Hello, World!'"
        # Implementation of full workflow test
        
        # Verify changes
        modified_code = self.file_manager.read_file("test.py")
        self.assertIn("Hello, World!", modified_code)
