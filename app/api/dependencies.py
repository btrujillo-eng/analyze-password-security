from app.services import PasswordAnalyzer, PasswordSecurityService, VulnerabilityDetector
from app.schemas import PasswordVulnerabilities, SecurityStatus

def get_password_analyzer() -> PasswordAnalyzer:
    return PasswordAnalyzer()

def get_vulnerability_detector() -> VulnerabilityDetector:
    return VulnerabilityDetector()

def get_password_security_service() -> PasswordSecurityService:
    return PasswordSecurityService(get_password_analyzer(), get_vulnerability_detector())

def get_default_vulnerabilty_value() -> PasswordVulnerabilities:
    return PasswordVulnerabilities.WITHOUT_VULNERABILITIES

def get_default_security_status() -> SecurityStatus:
    return SecurityStatus.UNSAFE