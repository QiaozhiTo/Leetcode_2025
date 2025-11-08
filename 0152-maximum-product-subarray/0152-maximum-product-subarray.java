class Solution {
    public int maxProduct(int[] nums) {
        int cur_min = nums[0];
        int cur_max = nums[0];
        int res = nums[0];

        for (int i=1; i < nums.length; i++){
            int tmp_min = Math.min(nums[i], Math.min(cur_min * nums[i],cur_max * nums[i]));
            int tmp_max = Math.max(nums[i], Math.max(cur_min * nums[i],cur_max * nums[i]));
            cur_min = tmp_min;
            cur_max = tmp_max;
            res = Math.max(res, cur_max);

        }
        return res;

        
    }
}