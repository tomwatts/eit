#include <iostream>


int reverse_digits(int i) {
    int result = 0;
    while (i != 0) {
        result = result * 10 + i % 10;
        i = i / 10;
    }

    return result;
}


int main() {
    for(int i = 0; i < 12; i++) {
        printf("Input: %i, Result: %i\n", i, reverse_digits(i));
    }

    return EXIT_SUCCESS;
}
