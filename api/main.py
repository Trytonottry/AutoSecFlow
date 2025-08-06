from fastapi import FastAPI
from pydantic import BaseModel
import subprocess, tempfile, os
app = FastAPI()

class ScanRequest(BaseModel):
    repo_url: str
    scanners: list[str]

@app.post("/scan")
def scan(req: ScanRequest):
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(["git", "clone", "--depth", "1", req.repo_url, d])
        os.chdir(d)
        subprocess.run(["pip", "install", "-r", "src/requirements.txt"])
        cmd = f"python src/autosecflow.py --scanners {','.join(req.scanners)} --token dummy"
        subprocess.run(cmd, shell=True)
        with open("SECURITY_REPORT.md") as f:
            return {"report": f.read()}