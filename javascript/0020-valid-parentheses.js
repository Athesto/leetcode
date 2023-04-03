/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const validator = [];
    for (key of s){
        validator.push(key)
        if (validator.length == 1)
            continue
        if (
            validator.slice(-2).join("") == "()" ||
            validator.slice(-2).join("") == "[]" ||
            validator.slice(-2).join("") == "{}"
        ){
            validator.pop()
            validator.pop()
        }
    }
    return (!validator.length)
};
