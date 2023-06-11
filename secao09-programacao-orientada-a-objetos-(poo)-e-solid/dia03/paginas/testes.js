const db = [1, 2, 3, 433, 5, 65];
const func = () => {
  console.log(db)
  const a = db.splice(1,1);
  console.log(a)
};

func();
console.log(db)