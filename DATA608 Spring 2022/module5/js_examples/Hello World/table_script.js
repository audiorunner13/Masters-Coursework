// var num_tab = 5

var num_tab = document.getElementById('num_tab').value

let table = document.createElement('table');
// let thead = document.createElement('thead');
let tbody = document.createElement('tbody');

// table.appendChild(thead);
table.appendChild(tbody);

// Adding the entire table to the body tag
document.getElementById('body').appendChild(table);

// Creating and adding data to first row of the table
let row_1 = document.createElement('tr');
let row_1_data_1 = document.createElement('td');
row_1_data_1.innerHTML = num_tab * 1;
let row_1_data_2 = document.createElement('td');
row_1_data_2.innerHTML = num_tab * 2;
let row_1_data_3 = document.createElement('td');
row_1_data_3.innerHTML = num_tab * 3;
let row_1_data_4 = document.createElement('td');
row_1_data_4.innerHTML = num_tab * 4;

row_1.appendChild(row_1_data_1);
row_1.appendChild(row_1_data_2);
row_1.appendChild(row_1_data_3);
row_1.appendChild(row_1_data_4);
tbody.appendChild(row_1);


// Creating and adding data to second row of the table
let row_2 = document.createElement('tr');
let row_2_data_1 = document.createElement('td');
row_2_data_1.innerHTML = num_tab * 5;
let row_2_data_2 = document.createElement('td');
row_2_data_2.innerHTML = num_tab * 6;
let row_2_data_3 = document.createElement('td');
row_2_data_3.innerHTML = num_tab * 7;
let row_2_data_4 = document.createElement('td');
row_2_data_4.innerHTML = num_tab * 8;

row_2.appendChild(row_2_data_1);
row_2.appendChild(row_2_data_2);
row_2.appendChild(row_2_data_3);
row_2.appendChild(row_2_data_4);
tbody.appendChild(row_2);


// Creating and adding data to third row of the table
let row_3 = document.createElement('tr');
let row_3_data_1 = document.createElement('td');
row_3_data_1.innerHTML = num_tab * 9;
let row_3_data_2 = document.createElement('td');
row_3_data_2.innerHTML = num_tab * 10;
let row_3_data_3 = document.createElement('td');
row_3_data_3.innerHTML = num_tab * 11;
let row_3_data_4 = document.createElement('td');
row_3_data_4.innerHTML = num_tab * 12;

row_3.appendChild(row_3_data_1);
row_3.appendChild(row_3_data_2);
row_3.appendChild(row_3_data_3);
row_3.appendChild(row_3_data_4);
tbody.appendChild(row_3);


