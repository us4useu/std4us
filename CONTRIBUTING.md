# Contributing to Nson

Thanks for your interest in contributing! This document describes how to build
the library, the conventions we follow, and how to propose changes.

## Reporting issues

- Use the GitHub issue tracker to report bugs, request features, or ask
  questions about the library.
- When reporting a bug, please include:
  - a minimal reproducer (a short `.cpp` file is ideal),
  - your compiler and its version,
  - the version of Nson (`std4us`) you are using,
  - the observed behavior and what you expected instead.

## Development setup

Nson is a header-only C++20 library packaged with
[Conan 2](https://conan.io/). To hack on it locally:

1. Clone the repository:
   ```
   git clone https://github.com/us4useu/nson.git
   cd nson
   ```

2. Export the recipe into your local Conan cache so downstream projects can
   consume your working copy:
   ```
   conan export recipes/nson/all --version=0.0.1
   ```

3. In a consumer project, add `nson/0.0.1` to your `conanfile.txt` (or
   `conanfile.py`) and rebuild.

Because the library is header-only, most changes only require re-exporting the
recipe; the repository itself has nothing to build.

## Repository layout

```
include/          Public headers, all in the `nson` namespace.
  concepts.h      Concepts used across the library.
  string.h        String utilities (to_string, join, split, trim).
  internal/       Implementation details — not part of the public API.
recipes/nson/     Conan recipe used to package the library.
```

Anything under `include/internal/` is an implementation detail; do not rely on
it from consumer code, and expect it to change without notice.

## Coding conventions

- Target C++20. It is fine to use `<concepts>`, `<ranges>`, `<format>`, and
  other C++20 features.
- Public APIs live in the `nson` namespace. Implementation helpers live in
  `nson::internal::<subsystem>`.
- Header guards use the `NSON_<PATH>_H` form (e.g. `NSON_STRING_H`).
- Every source file starts with the SPDX header:
  ```
  // SPDX-FileCopyrightText: Copyright (c) <year> us4us Ltd.
  // SPDX-License-Identifier: MIT
  ```
- Document public functions and concepts with a short Doxygen-style comment
  describing parameters, return value, and any non-obvious behavior.
- Prefer constraining templates with concepts over SFINAE.
- Follow the formatting used in existing headers (4-space indentation, braces
  on the same line, `east const` is not required — match the surrounding
  code).

## Adding a new component

1. Add the public header under `include/` (e.g. `include/foo.h`).
2. If the component has non-trivial internals, put them under
   `include/internal/foo.h` and include them from the public header.
3. Expose any relevant concepts through `concepts.h` so downstream code can
   constrain templates on them.
4. Update the "Structure" section of [README.md](README.md) with a short
   description of the new component.

## Submitting changes

1. Fork the repository and create a topic branch off `master`.
2. Make your changes in small, focused commits with clear commit messages.
3. Ensure the recipe still exports cleanly:
   ```
   conan export recipes/nson/all --version=0.0.1
   ```
4. Open a pull request against `master` describing the motivation for the
   change and any user-visible impact.

## License

By contributing, you agree that your contributions will be licensed under the
MIT license, the same license that covers this project. See [LICENSE](LICENSE)
for details.