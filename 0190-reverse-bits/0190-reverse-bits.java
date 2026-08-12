class Solution {
    public int reverseBits(int n) {

        int result = 0;

        for (int i = 0; i < 32; i++) {

            // Extract last bit
            int bit = n & 1;

            // Shift result left and add extracted bit
            result = (result << 1) | bit;

            // Remove last bit from n
            n >>>= 1;
        }

        return result;
    }
}