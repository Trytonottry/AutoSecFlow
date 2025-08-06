document.getElementById("scan").onclick = () => {
  chrome.tabs.query({active:true, currentWindow:true}, tabs => {
    const url = tabs[0].url;
    fetch("https://api.autosecflow.dev/scan", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({repo_url: url, scanners:["trivy","semgrep"]})
    }).then(r => r.json()).then(d => alert("Report ready!"));
  });
};