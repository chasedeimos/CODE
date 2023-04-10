function checkCashRegister(price, cash, cid) {
  // Map the currency values
  const MAP = {
    'PENNY': 0.01,
    'NICKEL': 0.05,
    'DIME': 0.1,
    'QUARTER': 0.25,
    'ONE': 1,
    'FIVE': 5,
    'TEN': 10,
    'TWENTY': 20,
    'ONE HUNDRED': 100
  }
  // Calculate the change needed
  var change = cash - price;
  // Create the change array 
  var changeArr = [];
  // Create an object for storing change currencies
  var changeObj = {};
  // Pick the appropriate change currency
  for (let i = cid.length - 1; i >= 0; i--) {
    let currency = cid[i][0];
    let value = MAP[currency];
    let available = cid[i][1];
    changeObj[currency] = 0;
    if (value <= change) {
      // While the currency is available and the change is not collected
      while (available > 0 && change > 0 && value <= change) {
        // Subtract from the change needed and the available cash
        available = Math.round((available - value) * 100) / 100;
        change = Math.round((change - value) * 100) / 100;
        // Add the currency and the amount changed to the array
        if (changeObj[currency]) {
          changeObj[currency] = Math
          .round((changeObj[currency] + value) * 100) / 100;
        } else {
          changeObj[currency] = value;
        }
        // Refresh the cash available in the drawer
        cid[i][1] = available;
      }
    }
  }
  // Construct the change array
  for (let currency in changeObj) {
    changeArr.push([currency, changeObj[currency]])
  }
  // Find the total cash-in-drawer amount
  var total = cid.map((arr) => { return arr[1] })
  .reduce((a, b) => a + b);
  // Identify the status
  var status = change > 0 ? 'INSUFFICIENT_FUNDS'
  : total > 0 ? 'OPEN': 'CLOSED';
  // If funds are insufficient, return an empty array as change
  if (status == 'INSUFFICIENT_FUNDS') {
    return {'status': status, 'change': [] }
  } else if (status == 'CLOSED') {
    return {'status': status, 'change': changeArr.reverse()}
  } else {
    return {'status' : status, 'change': changeArr.filter(arr => arr[1] != 0)}
  }
}

var res = checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);

console.log(res);