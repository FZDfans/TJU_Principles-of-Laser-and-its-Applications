$ErrorActionPreference = "Stop"
$wiki = Join-Path (Get-Location) "wiki"
$files = Get-ChildItem -Path $wiki -Recurse -Filter *.md
"Wiki markdown files: $($files.Count)"
"Draft pages:"
$files | Where-Object { (Get-Content $_.FullName -Raw -Encoding UTF8) -match "status:\s*draft" } | ForEach-Object { "- " + $_.FullName.Substring((Get-Location).Path.Length + 1) }
