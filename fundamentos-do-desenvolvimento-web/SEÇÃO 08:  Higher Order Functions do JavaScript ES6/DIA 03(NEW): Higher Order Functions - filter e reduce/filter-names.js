const dados = ['Luca', 91234567, 'Ana', 92345678, 'Marlete', 93456789];


function rof(element, index, array){
  // array[index + 1] = toString(array[index + 1]);
  console.log(array[index]);
  array[index + 1] = typeof array[index + 1];
  console.log(array[index + 1])
}

dados.filter(rof)