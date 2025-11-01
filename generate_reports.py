import os

def read_file(filepath):
    """Lee el contenido de un archivo, o devuelve un error si no existe."""
    if not os.path.exists(filepath):
        return f"Error: Report file not found at {filepath}"
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

coverage_report = read_file("coverage_report.txt")
pylint_report = read_file("pylint_report.txt")

# Define el contenido del archivo final
reports_content = f"""# Automated Reports
## Coverage Report
```text
{coverage_report}
```
## Pylint Report
```text
{pylint_report}
```
"""

# Escribe el contenido en REPORTS.md
with open("REPORTS.md", "w", encoding="utf-8") as f:
    f.write(reports_content)



