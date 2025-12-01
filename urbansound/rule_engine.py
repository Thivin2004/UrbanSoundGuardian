# urbansound/rule_engine.py

from typing import Tuple

def noise_score_for_label(label: str) -> int:
    """
    Assign a rough noise score (0-100) based on sound type.
    These values are inspired by typical urban noise levels.
    """
    base_scores = {
        "traffic": 82,
        "horn": 95,
        "construction": 88,
        "dogs": 45,
        "crowd": 72
    }
    return base_scores.get(label, 50)

def severity_from_score(score: int) -> str:
    """
    Convert numeric noise score to severity category.
    """
    if score < 50:
        return "LOW"
    elif score < 70:
        return "MEDIUM"
    elif score < 90:
        return "HIGH"
    else:
        return "CRITICAL"
def recommended_actions(label: str, severity: str) -> Tuple[str, str]:
    authority_actions = {
        "LOW": "No immediate action required. Continue monitoring.",
        "MEDIUM": "Log incident and monitor this area at peak hours.",
        "HIGH": "Send city inspection team to check compliance with noise rules.",
        "CRITICAL": "Trigger urgent enforcement: restrict source and notify authorities immediately."
    }

    citizen_tips = {
        "traffic": "Avoid unnecessary honking and follow lane discipline.",
        "horn": "Use horn only in emergency situations.",
        "construction": "Ensure construction follows permitted timings and uses noise barriers.",
        "dogs": "Avoid provoking stray animals and use ear protection if sensitive.",
        "crowd": "Avoid very crowded places during peak times to reduce noise exposure."
    }

    authority = authority_actions.get(severity, "Monitor the situation.")
    citizen = citizen_tips.get(label, "Reduce exposure to loud sounds where possible.")
    return authority, citizen
