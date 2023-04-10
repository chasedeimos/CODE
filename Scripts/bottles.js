// THIS PROGRAM PRINTS ALL SOLUTIONS TO THE THREE BOTTLES PUZZLE

class Bottle {
    constructor(capacity, contents) {
      if (capacity < contents) {
        contents = capacity;
      }
      this.capacity = capacity;
      this.contents = contents;
      this.updateState();
    }
    pourInto = (container) => {
      // Check if the bottle has room
      var room = container.capacity - container.contents;
      while (room > 0 && this.contents > 0) {
        container.contents++; 
        this.contents--;
        room--;
      }
      this.updateState();
      container.updateState();
    }
    updateState = () => {
      if (this.contents == 0) {
        this.state = 'empty';
      } else if (this.contents < this.capacity) {
      this.state = 'filled';
      } else {
      this.state = 'full';
      }
    }
  }

class Context {
  constructor(bottleArr) {
    // Identify the type of the current set
    var bottleStates = bottleArr.map(b => {return b.state}).sort();
    var contextTypes = [
      ['empty', 'filled', 'full'].toString(),
      ['empty', 'full', 'full'].toString(), 
      ['filled', 'filled', 'filled'].toString(),
      ['empty', 'filled', 'filled'].toString(),
      ['filled', 'filled', 'full'].toString()
    ]
    this.type = contextTypes.indexOf(bottleStates.toString());
    // Find which specific bottles are in which states and add them to the corresponding array
    var empty = [];
    var filled = [];
    var full = [];
    for (let i = 0; i < bottleArr.length; i++) {
      switch (bottleArr[i].state) {
        case 'empty':
          empty.push(bottleArr[i]);
          break;
        case 'filled':
          filled.push(bottleArr[i]);
          break;
        case 'full':
          full.push(bottleArr[i]);
          break;
      }
    }
    // Identify possible moves for the bottles in the current set
    switch (this.type) {
      // One possible move is an array where the first item can pour water into the second
      case 0:
        this.possibleMoves = [
          [full[0], filled[0]], 
          [full[0], empty[0]], 
          [filled[0], empty[0]]
        ];
        break;
      case 1:
        this.possibleMoves = [
          [full[0], empty[0]], 
          [full[1], empty[0]]
        ];
        break;
      case 2:
        this.possibleMoves = [
          [filled[0], filled[1]], 
          [filled[1], filled[0]],
          [filled[0], filled[2]], 
          [filled[2], filled[0]],
          [filled[1], filled[2]], 
          [filled[2], filled[1]]
        ];
        break;
      case 3:
        this.possibleMoves = [
          [filled[0], filled[1]],
          [filled[1], filled[0]], 
          [filled[0], empty[0]],
          [filled[1], empty[0]]
        ];
        break;
      case 4:
        this.possibleMoves = [
          [full[0], filled[0]],
          [full[0], filled[1]],
          [filled[0], filled[1]],
          [filled[1], filled[0]]
        ];
        break;
    }
  }
}
  
function makeTree(bottleArray, tree = {}) {
  // Fixate the bottle capacity order
  const CAPACITY_ORDER = [];
  bottleArray.forEach((bottle) => { CAPACITY_ORDER.push(bottle.capacity); });
  // Log current contents in an array
  var fork = [];
  bottleArray.forEach((bottle) => { fork.push(bottle.contents); });
  // Create an empty array for the new fork
  tree[fork] = [];
  // Identify possible moves for the current context
  var context = new Context(bottleArray);
  var options = context.possibleMoves;
  // Create a branch for every possible move from the options and link it to the current fork
  for (let moveIndex in options) {
    // Create a copy of the bottle set to leave the original one untouched for the other moves
    bottleArrayCopy = [];
    bottleArray.forEach((bottle) => { 
      let bottleCopy = new Bottle(bottle.capacity, bottle.contents);
      bottleArrayCopy.push(bottleCopy);
    });
    // Identify which copied bottles to perform the move on
    for (let copy of bottleArrayCopy) {
      if (copy.capacity == options[moveIndex][0].capacity && copy.contents == options[moveIndex][0].contents) {
        var pourer = copy;
      } else if (copy.capacity == options[moveIndex][1].capacity && copy.contents == options[moveIndex][1].contents) {
        var receiver = copy;
      }
    }
    // Perform the move on the copy of the set and create a new branch from it
    pourer.pourInto(receiver);
    var branch = [];
    bottleArrayCopy.forEach((bottleCopy) => { branch.push(bottleCopy.contents); });
    // If the set has been repeated anywhere in the tree, don't add it
    let repeated = false;
    for (let eachFork in tree) {
      for (let j = 0; j < tree[eachFork].length; j++) {
        if (branch.toString() == tree[eachFork][j].toString()) {
          repeated = true;
        }
      }
      if (branch.toString() == eachFork.toString()) {
        repeated = true;
      }
    }
    // It's okay for a fork with an 8 to repeat though
    for (let waterContained of branch) { if (waterContained == 8) { repeated = false; }}
    if (!repeated) {
      tree[fork].push(branch);
    }
  } 
  // Repeat the function for every branch of every fork in the tree
  for (let eachFork in tree) {
    for (let eachBranch of tree[eachFork]) {
      // Make sure the funciton doesn't execute on the same branch twice
      if (tree.hasOwnProperty(eachBranch)) { 
        continue;
      }
      // Create new bottles from the current branch using capacity order
      newBottleArray = []
      for (let i in eachBranch) {
        var newBottle = new Bottle(CAPACITY_ORDER[i], eachBranch[i]);
        newBottleArray.push(newBottle);
      }
      return makeTree(newBottleArray, tree);
    }
  }
  return tree;
}

function traceBranches(tree, solutions = []) {
  // If the function is running for the first time, look for the eights
  if (solutions.length == 0) {
    // Collect all the forks that contain a branch with an eight
    for (let fork in tree) {
      for (let branch of tree[fork]) {
        // Add it to the endings array if the branch contains 8 and the fork doesn't
        if (branch.includes(8) && !fork.includes(8)) {
          // Convert all items of the fork to integers
          fork = fork.split(',');
          for (i in fork) {
            fork[i] = parseInt(fork[i]);
          }
          solutions.push([fork, branch]);
        }
      }
    }
  }
  // Find the first item of each solution in the tree branches and add their forks to the solutions
  for (let solution of solutions) {
    // Search every fork for the same branch as the first item
    for (let fork in tree) {
      // Check every branch for matches 
      for (let branch of tree[fork]) {
        // When a match found add the fork to the beginning of the current solution
        if (branch.toString() == solution[0].toString()) {
          // Convert all items of the fork to integers
          fork = fork.split(',');
          for (i in fork) {
            fork[i] = parseInt(fork[i]);
          }
          solution.unshift(fork);

          // If the last (the first fork of the tree) step has been added to all solutions
          // Exit the current loop
          // Check if it's the last item in the solutions array
          if (solution === solutions[solutions.length-1] && fork.toString() == Object.keys(tree)[0].toString()) {
            return solutions;
          }
        }
      }
    }
  }
  // Repeat the function recursively
  return traceBranches(tree, solutions)
}

function getSolutions(...args) {
  bottles = Array.from(args);
  tree = makeTree(bottles);
  solutions = traceBranches(tree);
  // Add bottle capacities to the beginning of each solution
  capacities = [];
  for (let bottle of bottles) { capacities.push(bottle.capacity); }
  for (let solution of solutions) {
    solution.unshift(capacities, ['-','-','-'])
  }
  // Print out all the solutions
  for (let i = 0; i < solutions.length; i++) {
    console.log(`\nSolution #${i+1}\n`);
    for (let step of solutions[i]) {
      console.log(step);
    }
  }
  return solutions;
}

var b1 = new Bottle(10, 10);
var b2 = new Bottle(5, 1); 
var b3 = new Bottle(6, 0); 

var solutions = getSolutions(b1, b2, b3);