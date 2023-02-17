const people = [
    { name: 'Marquinho', age: {ageReal: 19, age: 18}},
    { name: 'Mateus', age: 18 },
    { name: 'José', age: 16 },
    { name: 'Ana', age: 23 },
    { name: 'Cláudia', age: 20 },
    { name: 'Bruna', age: 19 }
  ];
  
const organizeObject = () => (orderedObject = people.sort((obj1, obj2) => (obj1.age - obj2.age)));
  
  console.log(organizeObject());