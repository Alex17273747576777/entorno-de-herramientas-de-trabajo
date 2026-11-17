#!/usr/bin/env bash
# Crear incidencias por API sin temporales ni interpolación de títulos en código.
set -euo pipefail
exec python3 - "$@" <<'PY'
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request


def parse_blocks(text):
    records = []
    for number, block in enumerate(re.split(r"(?m)^---[ \t]*$", text), 1):
        if not block.strip():
            continue
        fields = {}
        body = []
        in_body = False
        for line in block.splitlines():
            if in_body:
                body.append(line[2:] if line.startswith("  ") else line)
            elif line.startswith("cuerpo: |"):
                in_body = True
            else:
                match = re.match(r"^(repo|titulo|etiquetas):[ \t]*(.*)$", line)
                if match:
                    fields[match[1]] = match[2].strip()
                elif line.strip() and not line.lstrip().startswith("#"):
                    raise ValueError(f"bloque {number}: línea no reconocida")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", fields.get("repo", "")):
            raise ValueError(f"bloque {number}: repo inválido o ausente")
        if not fields.get("titulo"):
            raise ValueError(f"bloque {number}: falta titulo")
        fields["body"] = "\n".join(body).strip()
        fields["labels"] = [x.strip() for x in fields.get("etiquetas", "").split(",") if x.strip()]
        records.append(fields)
    return records


def request(token, path, data=None):
    req = urllib.request.Request(
        "https://api.github.com/" + path,
        data=None if data is None else json.dumps(data).encode(),
        headers={"Authorization": "Bearer " + token,
                 "Accept": "application/vnd.github+json", "User-Agent": "incidencias"},
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def main():
    path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "incidencias.txt")
    records = parse_blocks(path.read_text(encoding="utf-8"))
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        token = (pathlib.Path.home() / ".gh-tokens").read_text().splitlines()[0].strip()
    if not token:
        raise ValueError("falta token de GitHub")
    opened = 0
    known = {}
    for item in records:
        repo = item["repo"]
        if repo not in known:
            titles = set()
            page = 1
            while True:
                issues = request(token, f"repos/{repo}/issues?state=open&per_page=100&page={page}")
                if not isinstance(issues, list):
                    raise ValueError("respuesta de incidencias inválida")
                titles.update(i["title"] for i in issues if "pull_request" not in i)
                if len(issues) < 100:
                    break
                page += 1
            known[repo] = titles
        if item["titulo"] in known[repo]:
            print("  = ya existe:", item["titulo"])
            continue
        payload = {"title": item["titulo"], "body": item["body"]}
        if item["labels"]:
            payload["labels"] = item["labels"]
        # Un error HTTP aborta: jamás se interpreta como lista vacía ni éxito.
        issue = request(token, f"repos/{repo}/issues", payload)
        known[repo].add(item["titulo"])
        opened += 1
        print(f"  + {repo}#{issue['number']}  {item['titulo']}")
    print(f"{opened} incidencias abiertas")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, urllib.error.URLError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
PY
