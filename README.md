# 🚀 AutoSecFlow  
> One-click security pipeline for GitHub Actions, REST API & Chrome Extension

![demo](https://github.com/вашлогин/AutoSecFlow/raw/main/docs/demo.gif)

[![GitHub release](https://img.shields.io/github/v/release/вашлогин/AutoSecFlow)](https://github.com/вашлогин/AutoSecFlow/releases)
[![Awesome](https://awesome.re/badge.svg)](https://github.com/awesome-selfhosted/awesome-selfhosted)

---

## 🪄 Features
- Composite GitHub Action – zero-setup, OIDC-auth, 3-second start
- REST API – POST repo URL → get SARIF+Markdown report
- Chrome Extension – 1-click scan of any repo
- Docker-Compose – self-hosted «SecDevOps in a box»
- 20+ built-in scanners (Trivy, Semgrep, TruffleHog, Checkov, ZAP…)

---

## 🚀 Quick Start
### GitHub Action
```yaml
- uses: вашлогин/AutoSecFlow@v1
  with:
    scanners: "trivy,semgrep"

### API
curl -X POST https://api.autosecflow.dev/scan \
  -H "Content-Type: application/json" \
  -d '{"repo_url":"https://github.com/owner/repo","scanners":["trivy"]}'

### Docker
git clone https://github.com/вашлогин/AutoSecFlow && cd AutoSecFlow
docker-compose up

## 📄 License
MIT © TryToNotTry
