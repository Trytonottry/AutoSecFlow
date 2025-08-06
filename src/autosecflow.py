#!/usr/bin/env python3
import argparse, json, os, subprocess, jinja2, yaml, datetime

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True)

def gen_report(findings):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))
    md = env.get_template("output.md.j2").render(findings=findings, date=datetime.datetime.utcnow())
    with open("SECURITY_REPORT.md", "w") as f:
        f.write(md)
    print(md)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scanners", required=True)
    parser.add_argument("--token", required=True)
    args = parser.parse_args()

    findings = []
    for tool in args.scanners.split(","):
        if tool == "trivy":
            out = run("trivy fs --format json .")
            findings.append(json.loads(out))
        elif tool == "semgrep":
            run("semgrep --config=auto --json -o sg.json .")
            findings.append(json.load(open("sg.json")))
        elif tool == "truffleHog":
            run("truffleHog git https://$GITHUB_SERVER_URL/$GITHUB_REPOSITORY --json > th.json")
            findings.append(json.load(open("th.json")))

    gen_report(findings)

if __name__ == "__main__":
    main()