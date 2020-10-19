#include <cmath>
#include <iostream>
#include <string>


int char_to_int(char c) {
    if (c >= '0' && c <= '9') {
        return c - '0';
    }

    return c - '7';
}


char int_to_char(int i) {
    if (i >= 0 && i <= 9) {
        return i + '0';
    }

    return i + '7';
}


std::string base_convert(std::string i, int in_base, int out_base) {
    if (i == "0") {
        return "0";
    }

    std::string result = "";
    int counter = 0;
    int base_10 = 0;

    do {
        base_10 += char_to_int(i.back()) * std::pow(in_base, counter++);
        i.pop_back();
    } while (i != "");

    do {
        result.push_back(int_to_char(base_10 % out_base));
        base_10 /= out_base;
    } while (base_10 > 0);

    return {rbegin(result), rend(result)};
}


int main() {

    printf("Input: %s, Result: %s\n", "0", base_convert("0", 10, 10).c_str());
    printf("Input: %s, Result: %s\n", "2", base_convert("1", 10, 2).c_str());
    printf("Input: %s, Result: %s\n", "A", base_convert("A", 16, 10).c_str());
    printf("Input: %s, Result: %s\n", "15", base_convert("15", 10, 16).c_str());
    printf("Input: %s, Result: %s\n", "16", base_convert("16", 10, 16).c_str());
    printf("Input: %s, Result: %s\n", "615", base_convert("615", 7, 13).c_str());

    return EXIT_SUCCESS;
}
