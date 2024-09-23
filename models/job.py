import json
from dataclasses import asdict, dataclass

from models.boss import Boss
from models.job_summary import JobSummary


@dataclass(init=False)
class Job:
    id: str = ""
    summary: JobSummary = None
    boss: Boss = None
    detail: str = ""
    posted_date: str = ""

    def to_jon(self):
        return json.dumps(self.to_dict(), default=str)

    def to_dict(self):
        return asdict(self)
