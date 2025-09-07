# 🚀 AutoSecFlow  
> One-click security pipeline for GitHub Actions, REST API & Chrome Extension

![demo](https://github.com/Trytonottry/AutoSecFlow/raw/main/docs/demo.gif)

[![GitHub release](https://img.shields.io/github/v/release/Trytonottry/AutoSecFlow)](https://github.com/Trytonottry/AutoSecFlow/releases)
[![Awesome](https://awesome.re/badge.svg)](https://github.com/awesome-selfhosted/awesome-selfhosted)
[![Build & Lint](https://img.shields.io/badge/build-pending-lightgrey)](https://github.com/<you>/AutoSecFlow/actions)
[![Coverage](https://img.shields.io/badge/coverage-unknown-lightgrey)](https://github.com/<you>/AutoSecFlow)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
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
- uses: Trytonottry/AutoSecFlow@v1
  with:
    scanners: "trivy,semgrep"
```
### API
```bash
curl -X POST https://api.autosecflow.dev/scan \
  -H "Content-Type: application/json" \
  -d '{"repo_url":"https://github.com/Trytonottry/repo","scanners":["trivy"]}'
```

### Docker
```bash
git clone https://github.com/Trytonottry/AutoSecFlow && cd AutoSecFlow
docker-compose up
```

## 📄 License
MIT © TryToNotTry
