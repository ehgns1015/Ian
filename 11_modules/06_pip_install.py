"""
Installing Third-Party Packages with pip

pip is Python's package installer.
It allows you to install packages from PyPI (Python Package Index).

Source: Modules and Packages.docx - pip and Third-Party Packages
"""

print("=== WHAT IS PIP? ===\n")

print("pip is the package installer for Python.")
print("It downloads and installs packages from PyPI (pypi.org)")
print("PyPI hosts over 400,000 packages!")

# Basic pip commands
print("\n=== BASIC PIP COMMANDS ===\n")

commands = """
# Install a package
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Install latest version
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name

# List installed packages
pip list

# Show package information
pip show package_name

# Search for packages
pip search keyword

# Install from requirements file
pip install -r requirements.txt

# Create requirements file
pip freeze > requirements.txt
"""

print(commands)

# Popular packages
print("=== POPULAR PYTHON PACKAGES ===\n")

print("Data Science & ML:")
print("  - numpy: Numerical computing")
print("  - pandas: Data analysis")
print("  - matplotlib: Data visualization")
print("  - scikit-learn: Machine learning")
print("  - tensorflow/pytorch: Deep learning")

print("\nWeb Development:")
print("  - django: Full-featured web framework")
print("  - flask: Lightweight web framework")
print("  - fastapi: Modern API framework")
print("  - requests: HTTP library")
print("  - beautifulsoup4: Web scraping")

print("\nUtilities:")
print("  - pillow: Image processing")
print("  - pytest: Testing framework")
print("  - black: Code formatter")
print("  - flake8: Code linter")

# Requirements file
print("\n=== REQUIREMENTS.TXT ===\n")

print("A requirements.txt file lists project dependencies:")

requirements_example = """
# requirements.txt
requests==2.28.0
numpy>=1.21.0
pandas>=1.3.0
flask==2.1.0
pytest>=7.0.0
"""

print(requirements_example)

print("Install all requirements:")
print("  pip install -r requirements.txt")

# Virtual environments
print("\n=== VIRTUAL ENVIRONMENTS ===\n")

print("Virtual environments isolate project dependencies.")

print("\nCreate virtual environment:")
venv_commands = """
# Using venv (built-in)
python -m venv myenv

# Activate (Windows)
myenv\\Scripts\\activate

# Activate (Mac/Linux)
source myenv/bin/activate

# Deactivate
deactivate

# Install packages in venv
(myenv) pip install requests
"""

print(venv_commands)

print("\nWhy use virtual environments?")
print("  - Isolate project dependencies")
print("  - Avoid version conflicts")
print("  - Easy to reproduce environment")
print("  - Clean project dependencies")

# Example workflow
print("\n=== TYPICAL WORKFLOW ===\n")

workflow = """
1. Create project directory
   mkdir my_project && cd my_project

2. Create virtual environment
   python -m venv venv

3. Activate virtual environment
   venv\\Scripts\\activate  (Windows)
   source venv/bin/activate  (Mac/Linux)

4. Install packages
   pip install requests pandas flask

5. Create requirements file
   pip freeze > requirements.txt

6. Work on project
   # Your code here

7. Deactivate when done
   deactivate

8. Share project
   # Others can recreate environment:
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
"""

print(workflow)

# Package versions
print("\n=== MANAGING VERSIONS ===\n")

print("Version specifiers:")
versions = """
package==1.2.3      # Exact version
package>=1.2.0      # Minimum version
package<=1.5.0      # Maximum version
package>=1.2,<2.0   # Range
package~=1.2.0      # Compatible version (>=1.2.0, <1.3.0)
"""
print(versions)

# Upgrading packages
print("\n=== UPGRADING PACKAGES ===\n")

upgrade_commands = """
# Upgrade single package
pip install --upgrade package_name

# Upgrade all packages (in requirements.txt)
pip install --upgrade -r requirements.txt

# List outdated packages
pip list --outdated

# Show what would be upgraded
pip install --upgrade --dry-run package_name
"""

print(upgrade_commands)

# Common issues and solutions
print("\n=== COMMON ISSUES ===\n")

print("1. Permission denied:")
print("   Solution: Use --user flag")
print("   pip install --user package_name")

print("\n2. pip not found:")
print("   Solution: Use python -m pip")
print("   python -m pip install package_name")

print("\n3. Package conflicts:")
print("   Solution: Use virtual environment")

print("\n4. Slow download:")
print("   Solution: Use --no-cache-dir")
print("   pip install --no-cache-dir package_name")

# Example: Using third-party package
print("\n=== EXAMPLE: USING REQUESTS ===\n")

example_code = """
# First install: pip install requests

import requests

# Make HTTP GET request
response = requests.get('https://api.github.com')

# Check status
if response.status_code == 200:
    data = response.json()
    print(f"Response: {data}")

# POST request
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', json=data)
print(f"Status: {response.status_code}")
"""

print(example_code)

# Best practices
print("\n=== PIP BEST PRACTICES ===\n")

print("1. Always use virtual environments")
print("2. Keep requirements.txt updated")
print("3. Pin versions in requirements.txt")
print("4. Regularly update packages (test first!)")
print("5. Use pip freeze to capture exact versions")
print("6. Separate dev and production requirements")
print("7. Check package security (pip-audit)")

# Project setup checklist
print("\n=== PROJECT SETUP CHECKLIST ===\n")

checklist = """
□ Create project directory
□ Initialize git repository
□ Create virtual environment
□ Activate virtual environment
□ Install required packages
□ Create requirements.txt
□ Create .gitignore (include venv/)
□ Write README.md
□ Start coding!
"""

print(checklist)

# Additional resources
print("\n=== RESOURCES ===\n")

print("PyPI: https://pypi.org")
print("pip documentation: https://pip.pypa.io")
print("Virtual environments: https://docs.python.org/3/library/venv.html")
print("requirements.txt: https://pip.pypa.io/en/stable/reference/requirements-file-format/")
