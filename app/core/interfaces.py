from app.schemas import PasswordData, PasswordAnalyzed, PasswordVulnerabilities, PasswordResponse

from abc import ABC, abstractmethod
from typing import List
class IPasswordAnalyzer(ABC):
    
    @abstractmethod
    async def analyze(self, password: PasswordData) -> PasswordAnalyzed: ...
    
class IVulnerabilityDetector(ABC):
    
    @abstractmethod
    async def detect(self, raw_data: PasswordAnalyzed, default_vulnerabilty_value: PasswordVulnerabilities) -> List[PasswordVulnerabilities]:...

class IPasswordSecurityService(ABC):
    
    @abstractmethod
    async def password_analyze(self, password: str) -> PasswordResponse: ...