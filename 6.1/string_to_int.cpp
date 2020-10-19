#include <cmath>
#include <iostream>
#include <string>


int string_to_int(std::string str) {
    int result = 0;
    for (int i = str.length() - 1; i >= 0; --i) {
        if (str[i] == '-') {
            return result * -1;
        }
        result += (str[i] - '0') * std::pow(10, str.length() - i - 1);
    }

    return result;
}


std::string int_to_string(int i) {
    if (!i) {
        return "0";
    }

    std::string result = "";

    // Dealing with negative numbers
    if (i < 0) {
        result.push_back('-');
        i *= -1;
    }

    int n_digits = 0;
    while (std::pow(10, n_digits) <= i) {
        ++n_digits;
    }

    while (i) {
        int rename_me = std::pow(10, --n_digits);
        result.push_back((i / rename_me) + '0');
        i %= rename_me;
    }

    return result;
}


int main() {

    printf("Input: %s, Result: %i\n", "0", string_to_int("0"));
    printf("Input: %s, Result: %i\n", "-0", string_to_int("-0"));
    printf("Input: %s, Result: %i\n", "1", string_to_int("1"));
    printf("Input: %s, Result: %i\n", "314", string_to_int("314"));
    printf("Input: %s, Result: %i\n", "-314", string_to_int("-314"));
    printf("Input: %i, Result: %s\n", 0, int_to_string(0).c_str());
    printf("Input: %i, Result: %s\n", 1, int_to_string(1).c_str());
    printf("Input: %i, Result: %s\n", 314, int_to_string(314).c_str());
    printf("Input: %i, Result: %s\n", -314, int_to_string(-314).c_str());

    return EXIT_SUCCESS;
}
