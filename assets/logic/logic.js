require("dotenv").config({ path: "../assets/modules/.env" });
const request = require('request');



function first(){
    request.post({url: "127.0.0.1", json: { funct: "instagram_login"}})
}


module.exports.first = first;
