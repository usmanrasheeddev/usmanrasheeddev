from pathlib import Path

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="900" height="300" viewBox="0 0 900 300">
  <rect width="100%" height="100%" fill="#0d1117"/>
  <rect x="20" y="20" width="860" height="260" rx="12" fill="#161b22" stroke="#30363d"/>
  <text x="50" y="65" fill="#58a6ff" font-family="Consolas, monospace" font-size="22">usmanrasheeddev@github</text>
  <text x="50" y="110" fill="#c9d1d9" font-family="Consolas, monospace" font-size="16">Now   : Building web projects</text>
  <text x="50" y="145" fill="#c9d1d9" font-family="Consolas, monospace" font-size="16">Prev  : Learning automation & scripting</text>
  <text x="50" y="180" fill="#c9d1d9" font-family="Consolas, monospace" font-size="16">Stack : HTML, CSS, JS, Java, Python, SQL</text>
  <text x="50" y="215" fill="#c9d1d9" font-family="Consolas, monospace" font-size="16">Focus : Clean code, performance, maintainability</text>
</svg>
"""
Path("info-card.svg").write_text(svg, encoding="utf-8")
print("wrote info-card.svg")