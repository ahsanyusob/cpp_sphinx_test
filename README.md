# cpp_sphinx_test

Minimal guide to document a C++ project using **Doxygen + Sphinx + Breathe**, styled with the **Read the Docs (RTD) theme**, and published via **GitHub Pages** (example link: https://ahsanyusob.github.io/cpp_sphinx_test/).

---

## 0) Example project layout

```text
my_project/
├─ include/
│  └─ Car.h
├─ src/
│  └─ Car.cpp
└─ docs/
```

---

## 1) Generate Doxygen XML

- Add Doxygen comments in your headers/sources (ref: https://www.doxygen.nl/manual/docblocks.html)
- In `docs/`:

```bash
doxygen -g Doxyfile
```

- Edit `docs/Doxyfile` (minimal):

```text
PROJECT_NAME           = "MyProject"
OUTPUT_DIRECTORY       = build
EXTRACT_ALL            = YES
INPUT                  = ../include ../src
RECURSIVE              = YES
GENERATE_XML           = YES
HAVE_DOT               = YES
CLASS_DIAGRAMS         = YES
CALL_GRAPH             = NO
CALLER_GRAPH           = NO
```

- Run Doxygen:

```bash
doxygen Doxyfile
```

This creates `docs/build/xml/`.

Refs:
- Doxygen config: https://www.doxygen.nl/manual/config.html

---

## 2) Connect Doxygen → Sphinx with Breathe

- Install:

```bash
pip install sphinx breathe
```

- Create Sphinx skeleton (inside `docs/`):

```bash
sphinx-quickstart source
```

This creates `docs/source/conf.py` and `docs/source/index.rst`.

- Edit `docs/source/conf.py`:

```python
extensions = ["breathe"]

breathe_projects = {"MyProject": "../build/xml"}
breathe_default_project = "MyProject"

# Theme added in step 3, keep default here for now
```

- Edit sphinx skeleton in `docs/source/index.rst`:

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

- Build & preview:

```bash
make -C docs clean
make -C docs html
xdg-open docs/build/html/index.html
```

Refs:
- Sphinx Skeleton: https://sphinx-tutorial.readthedocs.io/step-1/
- Breathe: https://breathe.readthedocs.io/en/latest/

---

## 3) Apply Read the Docs theme

- Install:

```bash
pip install sphinx_rtd_theme
```

- Update `docs/source/conf.py`:

```python
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']  # leave as default; folder is optional
# Do NOT set html_baseurl/canonical_url for Pages; not required
```

- Rebuild:

```bash
make -C docs clean
make -C docs html
xdg-open docs/build/html/index.html
```

Refs:
- RTD theme: https://sphinx-rtd-theme.readthedocs.io/en/stable/

---

## 4) Deploy to GitHub Pages (project page)

- Create the `gh-pages` branch and publish the built HTML at branch root:

```bash
git checkout --orphan gh-pages
rm -rf ./*
cp -r docs/build/html/* .
touch .nojekyll   # critical: serve _static/_sources on GitHub Pages
git add .
git commit -m "Deploy docs"
git push origin gh-pages --force
```

- In GitHub: **Settings → Pages**
  - Source: `gh-pages` branch
  - Folder: `/ (root)`
  - Save and wait a minute

Your docs will be at:

```
https://username.github.io/reponame/
```

If the page looks unstyled, confirm `.nojekyll` exists at the root of `gh-pages` and that `_static/` is present in the branch.

Refs:
- GitHub Pages: https://docs.github.com/en/pages

---

## Appendix: Minimal example code


`include/Car.h`
```cpp
/**
 * @file Car.h
 * @brief Defines the Car class.
 */

#ifndef CAR_H
#define CAR_H

#include <string>

/**
 * @class Car
 * @brief A simple Car class.
 *
 * Demonstrates how to generate docs with
 * Doxygen + Sphinx + Breathe.
 */
class Car {
public:
    /**
     * @brief Construct a new Car object.
     * @param brand Car brand name.
     * @param year Year of manufacture.
     */
    Car(const std::string& brand, int year);

    /**
     * @brief Start the engine.
     * @return true if started successfully, false otherwise.
     */
    bool startEngine();

    /// Stop the engine.
    void stopEngine();

    /// Get the car brand.
    std::string getBrand() const;

private:
    std::string brand_; ///< Brand of the car.
    int year_;          ///< Year of manufacture.
    bool running_;      ///< Engine status.
};

#endif // CAR_H
```


`src/Car.cpp`
```cpp
#include "Car.h"
#include <iostream>

/**
 * @brief Construct a new Car object.
 * @param brand Car brand name.
 * @param year Year of manufacture.
 */
Car::Car(const std::string& brand, int year)
    : brand_(brand), year_(year), running_(false) {}

/**
 * @brief Start the engine.
 * @return true if started successfully, false otherwise.
 */
bool Car::startEngine() {
    if (!running_) {
        running_ = true;
        std::cout << brand_ << " engine started." << std::endl;
        return true;
    }
    return false; // already running
}

/**
 * @brief Stop the engine.
 */
void Car::stopEngine() {
    if (running_) {
        running_ = false;
        std::cout << brand_ << " engine stopped." << std::endl;
    }
}

/**
 * @brief Get the car brand.
 * @return std::string Car brand.
 */
std::string Car::getBrand() const {
    return brand_;
}
```
