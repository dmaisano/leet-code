// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findStartingIndex(vector<int>& a, int x) {
        int index = -1;
        int start = 0, end = a.size() - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (a[mid] >= x) {
                end = mid - 1;
            } else { // a[mid] < x
                start = mid + 1;
            }

            if (a[mid] == x) {
                index = mid;
            }
        }

        return index;
    }

    int findEndingIndex(vector<int>& a, int x) {
        int index = -1;
        int start = 0, end = a.size() - 1;

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (a[mid] <= x) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }

            if (a[mid] == x) {
                index = mid;
            }
        }

        return index;
    }

    vector<int> searchRange(vector<int>& a, int x) {
        int startingIndex = findStartingIndex(a, x);
        int endingIndex = findEndingIndex(a, x);

        return { startingIndex, endingIndex };
    }
};

int main(int argc, char const* argv[])
{
    vector<int> nums { 5, 7, 7, 8, 8, 10 };
    vector<int> nums2 { 1 };

    auto sln = new Solution();
    auto res = sln->searchRange(nums, 8);
    auto res2 = sln->searchRange(nums2, 1);

    cout << "first pos: " << res[0] << "\nsecond pos: " << res[1] << endl;
    cout << "first pos: " << res2[0] << "\nsecond pos: " << res2[1] << endl;

    return 0;
}
