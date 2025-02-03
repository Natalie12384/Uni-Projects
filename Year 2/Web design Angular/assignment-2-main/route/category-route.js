const express = require("express");
const catCont = require("../controller/category-controller");

const router = express.Router();

router.post("/", catCont.newCategory);

module.exports = router;