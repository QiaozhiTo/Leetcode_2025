class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int minBuy = prices[0];
        for (int p:prices){
            maxP = Math.max(maxP, p-minBuy);
            minBuy = Math.min(p, minBuy);
        }
        return maxP;
        
    }
}