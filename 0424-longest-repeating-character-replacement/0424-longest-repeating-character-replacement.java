// class Solution {
//     public int characterReplacement(String s, int k) {
//         Map<Character, Integer> count = new HashMap<>();
//         int l = 0;
//         int res = 0;
//         for (int r = 0; r < s.length(); r ++){
//             char c = s.charAt(r);
//             count.put(c, count.getOrDefault(c, 0)+1);
//             while ((r - l + 1) - Collections.max(count.values()) > k){
//                 char left = s.charAt(l);
//                 count.put(left, count.getOrDefault(left, 0)-1);
//                 l ++;
//             }
//             res = Math.max(res, r - l + 1);
//         }
//         return res;
//     }
// }

// optimization
class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> count = new HashMap<>();
        int l = 0;
        int res = 0;
        int MaxCount = 0;

        for (int r =0; r < s.length(); r++){
            char c = s.charAt(r);
            count.put(c, count.getOrDefault(c, 0)+1);
            MaxCount = Math.max(MaxCount, count.get(c));
            while( (r-l+1) - MaxCount > k){
                char left = s.charAt(l);
                count.put(left, count.getOrDefault(left, 0)-1);
                l ++;
            }
            res = Math.max(res, r-l+1);
        }
        return res;
    }
}