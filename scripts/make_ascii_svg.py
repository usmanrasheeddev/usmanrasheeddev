from pathlib import Path

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="900" height="500" viewBox="0 0 900 500">
  <rect width="100%" height="100%" fill="#0d1117"/>
  <text x="40" y="70" fill="#c9d1d9" font-family="Consolas, monospace" font-size="24">ASCII Portrait</text>
  <text x="40" y="120" fill="#8b949e" font-family="Consolas, monospace" font-size="16">Step 3b placeholder generated successfully.</text>
  <text x="40" y="170" fill="#58a6ff" font-family="Consolas, monospace" font-size="14">Run full photo pipeline later on Python 3.12 for real portrait output.</text>
</svg>
"""
Path("avi-ascii.svg").write_text(svg, encoding="utf-8")
print("wrote avi-ascii.svg")