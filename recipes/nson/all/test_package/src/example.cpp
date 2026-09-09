// SPDX-FileCopyrightText: Copyright (c) 2024-2026 us4us Ltd.
// SPDX-License-Identifier: MIT

#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>

#include <nson/concepts.h>
#include <nson/string.h>

int main() {
    const std::vector<int> values{1, 2, 3};

    const auto joined = nson::join(values, ", ");
    const auto stringified = nson::to_string(values);
    const auto trimmed = nson::trim("  hello  ");

    std::cout << joined << '\n' << stringified << '\n' << trimmed << '\n';

    if (joined != "1, 2, 3" || stringified != "1, 2, 3" || trimmed != "hello") {
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
