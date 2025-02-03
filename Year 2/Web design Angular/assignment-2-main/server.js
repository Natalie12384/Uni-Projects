const mongoose = require("mongoose");
const express = require("express");

const catRouter = require("./route/category-route");

const app = express();
app.listen(8081);

app.use(express.json());

const url = "mongodb://localhost:27017/";

async function connect(url) {
	await mongoose.connect(url);
	return "Connected Successfully";
}

//tempory for testing
app.use("/category", catRouter);

connect(url)
	.then(console.log)
	.catch((err) => console.log(err));