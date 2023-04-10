function convertToRoman(num) {
    // Make sure the number is smaller than 3999
    if (num > 3999) { return }
    // Convert the number to a string
    var digits = num.toString(10);
    // Make an array for storing the roman digits
    var roman = [];
    // Do for each digit from the right
    for (let i = digits.length - 1; i >= 0; i--) {
        // Attach the digit to a variable
        var digit = digits[i];
        // Make an arr for storing the range digits
        var range = [];
        // Identify the numerical place (ones, tens, hundreds, thousands)
        switch (digits.length - 1 - i) {
            // Ones
            case 0:
                range.push('I','V','X');
                break;
            // Tens
            case 1:
                range.push('X','L','C');
                break;
            // Hundreds
            case 2:
                range.push('C','D','M');
                break;
            // Thousands
            case 3:
                range.push('M');
                break;
        }
        // See if the digit is greater than five
        if (digit > 5) {
            // See how many ones are left in the digit
            var ones = digit % 5;
            // If more than three
            if (ones > 3) {
                // Subtract from the greatest number in the range
                roman.unshift(range[0] + range[2]);
            } else {
                roman.unshift(range[1] + range[0].repeat(ones));
            }
        // If the digit is smaller than five
        } else if (digit < 5) {
            // See how many ones are there in the digit 
            var ones = digit;
            // If more than three
            if (ones > 3) {
                // Subtract from the middle number in the range
                roman.unshift(range[0] + range[1]);
            } else {
                roman.unshift(range[0].repeat(ones));
            }
        // If the digit is five
        } else {
            roman.unshift(range[1]);
        }
    }
    return roman.join('');
}
   
console.log(convertToRoman(399));