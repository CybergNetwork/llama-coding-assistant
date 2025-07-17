import os
import git
from pathlib import Path

class FileSystemManager:
    def __init__(self, workspace_path):
        self.workspace_path = Path(workspace_path)
        self.git_repo = None
        self.init_git_if_needed()
    
    def init_git_if_needed(self):
        """Initialize git repo if not exists"""
        try:
            self.git_repo = git.Repo(self.workspace_path)
        except git.InvalidGitRepositoryError:
            self.git_repo = git.Repo.init(self.workspace_path)
    
    def read_file(self, file_path):
        """Read file content"""
        full_path = self.workspace_path / file_path
        if full_path.exists():
            return full_path.read_text()
        return None
    
    def write_file(self, file_path, content, create_backup=True):
        """Write file content with optional backup"""
        full_path = self.workspace_path / file_path
        
        if create_backup and full_path.exists():
            backup_path = full_path.with_suffix(f".bak.{int(time.time())}")
            full_path.rename(backup_path)
        
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content)
    
    def commit_changes(self, message="AI agent code changes"):
        """Commit changes to git"""
        if self.git_repo:
            self.git_repo.git.add(A=True)
            self.git_repo.index.commit(message)
