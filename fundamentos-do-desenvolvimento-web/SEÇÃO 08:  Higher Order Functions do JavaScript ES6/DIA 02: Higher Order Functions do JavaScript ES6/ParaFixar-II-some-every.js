const people = [
    { name: 'Mateus', age: 19 },
    { name: 'José', age: 18 },
    { name: 'Ana', age: 23 },
    { name: 'Cláudia', age: 20 },
    { name: 'Bruna', age: 19 },
  ];
  
  const verifyAges = (arr, minimumAge) => arr.every((obj)=>(obj.age >= minimumAge));
  
  console.log(verifyAges(people, 18));