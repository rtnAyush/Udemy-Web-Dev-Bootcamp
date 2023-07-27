// using mongoose
const mongoose = require('mongoose');

mongoose.set('strictQuery', false);

main();

async function main() {
  await mongoose.connect("mongodb://127.0.0.1:27017/fruitsDB", { useNewUrlParser: true });
  // console.log("mongoDB server is connected.");

  const fruitSchema = new mongoose.Schema({
    name: {
      type: String,
      required: [true, "Name not inserted"]
    },
    rating: {
      type: Number,
      max: 10,
      min: 1
    },
    review: String
  });

  const personSchema = new mongoose.Schema({
    name: String,
    age: Number,
    favouriteFruit : fruitSchema
  })

  const Fruit = mongoose.model("Fruit", fruitSchema);
  const Person = mongoose.model("Person", personSchema)

  const pineapple = new Fruit({
    name: "Pineapple",
    rating: 8,
    review: "This very yummy fruit."
  });

  const person = new Person({
    name: "Aney",
    age: 16,
    favouriteFruit: pineapple
  });
  // await person.save();
  // await pineapple.save();
  // mongoose.disconnect();

  Person.updateOne({name:"Jhon"},{favouriteFruit: pineapple},function(err){
    if (err) {
      console.log(err);
    } else {
      console.log("SuccessFully updated.");
    }
  });

  // Fruit.deleteOne({name: "Lichi"}, function(err){
  //   if (err) {
  //     console.log(err);
  //   } else {
  //     console.log("SuccessFully deleted.");
  //   }
  // });

  // Fruit.find(function(err, fruits) {
  //   if (err) {
  //     console.log(err);
  //   } else {
  //
  //     mongoose.disconnect();
  //
  //     fruits.forEach(function(fruit) {
  //       console.log(fruit.name);
  //     })
  //   }
  // });
}
