// Day 2 mini task- Find highest marks from an array

const marks = [88, 78, 68, 75, 99, 67]

let highest = marks[0];

for (let i = 1; i< marks.length; i++) {
    if (marks[i]> highest){
        highest = marks[i];
    }
}

console.log("Highest Marks:", highest)
