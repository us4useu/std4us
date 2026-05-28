// SPDX-FileCopyrightText: Copyright (c) 2026 us4us Ltd.
// SPDX-License-Identifier: MIT

#ifndef STD4US_CONCEPTS_H
#define STD4US_CONCEPTS_H

#include <concepts>
#include <ostream>
#include <string>

#include "internal/join.h"
#include "internal/string.h"

namespace std4us {

/**
 * Concept to check if a type supports std4us::join.
 */
template<typename T>
concept supports_join = internal::join::supports_join<T>;

/**
 * Concept to check if a type supports std4us::to_string directly (i.e. not via std4us::join).
 */
template<typename T>
concept supports_to_string_directly = internal::string::supports_to_string<T>;

/**
 * Concept to check if the type is supported by one of the specializations of std4us::to_string. 
 */
template<typename T>
concept supports_to_string = internal::string::supports_to_string<T>;

/**
 * Concept to check if a type supports ostream << operator.
 */
template<typename T>
concept streamable = internal::string::streamable<T>;

}// namespace std4us

#endif// STD4US_CONCEPTS_H