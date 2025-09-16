# cpp_sphinx_test

Guide to document **C++** or **Python** projects using **Sphinx** (and **Doxygen + Breathe** for C++), styled with the **Read the Docs (RTD) theme**, and published via **GitHub Pages**.  
Example: https://ahsanyusob.github.io/cpp_sphinx_test/

(I wont maintain this repo. Only for reference.)

---

## Project layout

```text
my_project/
├─ include/      # C++ headers
│  └─ Car.h
├─ src/          # C++ sources
│  └─ Car.cpp
├─ py_module/    # Python module (optional)
│  └─ car.py
└─ docs/
```

Code references:
- [`my_project/include/Car.h`](my_project/include/Car.h)
- [`my_project/src/Car.cpp`](my_project/src/Car.cpp)
- [`my_project/py_module/car.py`](my_project/py_module/car.py)

---

## 1) Generate Doxygen XML (C++)

1. Add **Doxygen-style comments** in headers and source files. Reference: https://www.doxygen.nl/manual/docblocks.html

2. In `docs/`, create a default Doxygen config:

```bash
doxygen -g Doxyfile
```

This generates `docs/Doxyfile`.

3. Edit `docs/Doxyfile` (minimal setup for XML):

```text
PROJECT_NAME     = "MyProject"
OUTPUT_DIRECTORY = build
EXTRACT_ALL      = YES
INPUT            = ../include ../src
RECURSIVE        = YES
GENERATE_XML     = YES
HAVE_DOT         = YES
CLASS_DIAGRAMS   = YES
CALL_GRAPH       = NO
CALLER_GRAPH     = NO
```

4. Run Doxygen to generate XML:

```bash
doxygen Doxyfile
```

- XML output will be at `docs/build/xml/`
- Diagram images at `docs/build/html/` (if `HAVE_DOT=YES`)

Refs:
- Doxygen config: https://www.doxygen.nl/manual/config.html

---

## 2) Connect Doxygen → Sphinx with Breathe (C++)

1. Install dependencies:

```bash
pip install sphinx breathe sphinx_rtd_theme
```

2. Generate Sphinx skeleton inside `docs/`:

```bash
sphinx-quickstart source
```

This creates `docs/source/conf.py` and `docs/source/index.rst`.

3. Edit `docs/source/conf.py`:

```python
extensions = ["breathe"]

breathe_projects = {"MyProject": "../build/xml"}
breathe_default_project = "MyProject"

# RTD theme
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
```

4. Edit `docs/source/index.rst`:

```rst
Welcome to MyProject
====================

.. toctree::
   :maxdepth: 2

API Reference
-------------
.. doxygenclass:: Car
   :project: MyProject
```

5. Build and preview:

```bash
make -C docs clean
doxygen Doxyfile  #build again since it got cleaned
make -C docs html
xdg-open docs/build/html/index.html
```

Refs:
- Sphinx Skeleton: https://sphinx-tutorial.readthedocs.io/step-1/
- Breathe: https://breathe.readthedocs.io/en/latest/

---

## 3) Generate docs for Python

- Python Sphinx uses **docstrings** directly.

- In `docs/source/conf.py`:

```python
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]
html_theme = "sphinx_rtd_theme"
```

- In `docs/source/index.rst`:

```rst
Welcome to My Python Project
============================

.. automodule:: car
   :members:
```

- Build and preview:

```bash
make -C docs clean
doxygen Doxyfile  #build again since it got cleaned
make -C docs html
xdg-open docs/build/html/index.html
```

Refs:
- Sphinx: https://www.sphinx-doc.org/en/master/
- RTD theme: https://sphinx-rtd-theme.readthedocs.io/en/stable/

---

## 4) Deploy to GitHub Pages 

(Example: Creating orphaned, single commit gh-pages branch)

1. Switch/create `gh-pages` branch:

```bash
git checkout --orphan gh-pages
```

2. Remove old files and copy HTML:

```bash
#following 3 steps will copy built HTML to repo /root and delete everything else
# cp -r <path/to/repo/docs/build/html/*> <path/to/tmp>
# rm -rf <path/to/repo/*>
# mv <path/to/tmp> <path/to/repo>
touch .nojekyll   # critical: jekyll (default) ignores folders starting with _
git add .
git commit -m "Deploy docs"
git push origin gh-pages --force
```

3. In GitHub Settings → Pages:
- Source: `gh-pages` branch
- Folder: `/ (root)`
- Save and wait ~1–2 minutes

Access the docs:

```
https://username.github.io/reponame/
```

Confirm:
- `.nojekyll` exists in branch root
- `_static/` and `_sources/` are present
