const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');
// const https = require('https');
const client = require("@mailchimp/mailchimp_marketing");

const app = express();

app.use(express.static("public"));
app.use(bodyParser.urlencoded({
  extended: true
}));


app.get("/", function(req, res) {

  res.sendFile(__dirname + "/signup.html");
});

client.setConfig({
  apiKey: "f413b8e259d3119ba4c4c5711b86efc3-us21",
  server: "us21",
});

// for checking api is working or not
// async function run() {
//   const response = await client.ping.get();
//   console.log(response);
// }
// run();



// async function run() {
//   const listId = "a139a128c0";
//     try {
//         const response = await client.lists.addListMember(listId, {
//           email_address: "1214w15@gmail.com",
//           status: "subscribed",
//           merge_fields: {
//             FNAME: "Ayush",
//             LNAME: "Kumar"
//           }
//         });
//
//         console.log("Successfully added contact as an audience member. The contact's id is "+response.id);
//
//         // res.sendFile(__dirname + "/success.html");
//     } catch (e) {
//         // res.sendFile(__dirname + "/failure.html");
//         console.log("failed :" + e);
//     }
// }

app.post("/", function(req, res) {

  const fName = req.body.firstName;
  const lName = req.body.lastName;
  const email = req.body.email;

  async function run() {
    const listId = "a139a128c0";
    try {
      const response = await client.lists.addListMember(listId, {
        email_address: email,
        // status: "subscribed",
        status: "pending",
        merge_fields: {
          FNAME: fName,
          LNAME: lName
        }
      });

      console.log("Successfully added contact as an audience member. The contact's id is " + response.id);

      res.sendFile(__dirname + "/success.html");
    } catch (e) {
      res.sendFile(__dirname + "/failure.html");
      console.log("failed :" + e);
    }
  }
  run();
});

app.post("/failure", function(req,res){
  res.redirect("/");
});

app.listen(process.env.PORT || 3000, function() {

  console.log("Srver is started at port 3000");

});


// api key
// f413b8e259d3119ba4c4c5711b86efc3-us21


// app.post("/", function(req, res) {
//
//   const fName = req.body.firstName;
//   const lName = req.body.lastName;
//   const email = req.body.email;
//
// const data = {
//   members: [
//     {
//       email_address: email,
//       status: "subscribed",
//       merge_fields: {
//         FNAME: fName,
//         LNAME: lName
//       }
//     }
//   ]
// };
//
// const jsonData = JSON.stringify(data);
//
// const url = "https://us21.mailchimp.com/3.0/list/a139a128c0";
//
// const option = {
//   method: "POST",
//   auth: "aka-ayush: f413b8e259d3119ba4c4c5711b86efc3-us21"
// };
//
// var request = https.request(url, option, function(response){

// response.on("data", function(data){
//   console.log(JSON.parse(data));
// });

// });
//
// request.write(jsonData);
// request.end();
// });
