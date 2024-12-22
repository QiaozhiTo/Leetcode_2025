/**
 * Encodes a list of strings to a single string.
 *
 * @param {string[]} strs
 * @return {string}
 */
var encode = function(strs) {
    let res = "";
    for (let s of strs){
        res += s.length + "#" + s;
    }
    return res;
    
};

/**
 * Decodes a single string to a list of strings.
 *
 * @param {string} s
 * @return {string[]}
 */
var decode = function(s) {
    let i = 0;
    let res = [];
    while (i < s.length){
        j = i;
        while(s[j] !== "#"){
            j ++; 
        }
        
        let len = parseInt(s.substring(i, j));
        res.push(s.substring(j+1, j+len + 1));
        i = j + len + 1; 
    }    
    return res;
    
    
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */