//jshint esversion:6
const express = require('express');
const bodyParser = require('body-parser');
const ejs = require('ejs');
const mongoose = require('mongoose');
const encrypt = require('mongoose-encryption');


const app = express();

app.use(express.static('public'));
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));



mongoose.set('strictQuery', false);
mongoose.connect("mongodb://127.0.0.1:27017/userDB", { useNewUrlParser: true });

const userSchema = new mongoose.Schema ({
  email : String,
  password: String
});

const secret = "Thisisourlittlesecret.";
userSchema.plugin(encrypt, { secret: secret, encryptedFeilds: ["password"], excludeFromEncryption:  ["email"]  });
const User = mongoose.model("User", userSchema);

app.get("/", (req, res)=>{
  res.render("home");
});

app.get("/login", (req, res)=>{
  res.render("login");
});

app.get("/register", (req, res)=>{
  res.render("register");
});

app.post("/register", (req, res)=>{
  const newUser = new User ({
    email : req.body.username,
    password : req.body.password
  });

  newUser.save((err)=>{
    if (!err) {
      res.render("secrets");
    }
  });
});

app.post("/login", (req, res)=>{
  User.findOne({email: req.body.username}, (err, foundUser)=>{
    if (!err) {
      console.log(foundUser);
      if (foundUser.password === req.body.password) {
        res.render("secrets");
      }
    }
  })
});


app.listen(3000, ()=>{
  console.log("server is started at port 3000");
})
