from pathlib import Path


def instructions():
    return (Path(__file__).resolve().parent.parent / 'skills/job_requirements_agent.md').read_text(encoding='utf8')
