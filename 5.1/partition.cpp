#include <iostream>
#include <vector>


std::vector<int> partition_by_pivot(std::vector<int> arr, int pivot) {
    std::vector<int> left = {};
    std::vector<int> right = {};
    std::vector<int> middle = {};

    for (std::vector<int>::iterator it = arr.begin(); it != arr.end(); ++it) {
        if (*it > arr[pivot]) {
            right.push_back(*it);
        } else if (*it < arr[pivot]) {
            left.push_back(*it);
        } else {
            middle.push_back(*it);
        }
    }

    std::vector<int> result = {};
    result.insert(result.end(), left.begin(), left.end());
    result.insert(result.end(), middle.begin(), middle.end());
    result.insert(result.end(), right.begin(), right.end());
    return result;
}


int main() {

    std::vector<int> result = partition_by_pivot({0, 1, 2, 0, 2, 1, 1}, 3);
    for (std::vector<int>::iterator it = result.begin(); it != result.end(); ++it) {
        std::cout << ' ' << *it;
    }
    std::cout << '\n';

    return EXIT_SUCCESS;
}
