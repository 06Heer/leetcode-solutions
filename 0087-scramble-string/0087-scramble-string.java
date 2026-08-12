class Solution {

    private Boolean[][][] memo;
    private String s1, s2;

    public boolean isScramble(String s1, String s2) {

        if (s1.length() != s2.length()) {
            return false;
        }

        this.s1 = s1;
        this.s2 = s2;

        int n = s1.length();

        memo = new Boolean[n][n][n + 1];

        return solve(0, 0, n);
    }

    private boolean solve(int i, int j, int len) {

        // Already calculated
        if (memo[i][j][len] != null) {
            return memo[i][j][len];
        }

        // Base case
        if (len == 1) {
            return memo[i][j][len] = 
                s1.charAt(i) == s2.charAt(j);
        }

        // Character frequency pruning
        int[] count = new int[26];

        for (int k = 0; k < len; k++) {
            count[s1.charAt(i + k) - 'a']++;
            count[s2.charAt(j + k) - 'a']--;
        }

        for (int x : count) {
            if (x != 0) {
                return memo[i][j][len] = false;
            }
        }

        // Try every possible split
        for (int k = 1; k < len; k++) {

            // Case 1: No swap
            if (solve(i, j, k) &&
                solve(i + k, j + k, len - k)) {

                return memo[i][j][len] = true;
            }

            // Case 2: Swap
            if (solve(i, j + len - k, k) &&
                solve(i + k, j, len - k)) {

                return memo[i][j][len] = true;
            }
        }

        return memo[i][j][len] = false;
    }
}