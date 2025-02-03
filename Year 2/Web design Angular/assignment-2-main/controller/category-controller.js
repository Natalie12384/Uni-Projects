const Category = require("../model/category");

module.exports = {
	newCategory: async function (req, res) {
		let aCategory = new Category({ name: req.body.name,description: req.body.description,imagePath:req.body.imagePath });
		await aCategory.save();
		res.json(aCategory);
	},
};