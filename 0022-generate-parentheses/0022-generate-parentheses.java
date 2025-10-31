class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        StringBuilder stack = new StringBuilder();
        backtrack(0, 0, n, res, stack);
        return res;
    }

    private void backtrack(int openN, int closeN, int n, List<String> res, StringBuilder stack){
        if(openN == n && closeN == n){
            res.add(stack.toString());
            return;
        }
        if(openN < n){
            stack.append('(');
            backtrack(openN+1, closeN, n, res, stack);
            stack.deleteCharAt(stack.length() - 1);
        }
        if(closeN < openN){
            stack.append(')');
            backtrack(openN, closeN+1, n, res, stack);
            stack.deleteCharAt(stack.length() - 1);
        }

    }
}
