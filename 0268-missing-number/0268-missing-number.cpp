class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();

        long long expected = 1LL * n * (n + 1) / 2;
        long long actual = 0;

        for (int num : nums)
            actual += num;

        return expected - actual;
    }
};