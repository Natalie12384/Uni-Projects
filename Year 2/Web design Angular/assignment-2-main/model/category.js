const mongoose = require("mongoose");

const categorySchema = mongoose.Schema({
	_id: {
		type: String, 
		default: function() {
			const randomAlphabet1 = String.fromCharCode(Math.round(Math.random() * (90 - 65) + 65));
			const randomAlphabet2 = String.fromCharCode(Math.round(Math.random() * (90 - 65) + 65));
			const randomInteger = (Math.floor(Math.random() * 9999) + 1).toString().padStart(4, '0');
			return `C${randomAlphabet1}${randomAlphabet2}-${randomInteger}`;
		},
	},
	name: {
		type: String,
		required: true,
	},
    description: {
        type: String,
    },
    imagePath: {
        type: String
    },
    eventsList: [{
		type: mongoose.Schema.Types.ObjectId,
	    ref: "Event",
	}],
	createdAt: {
		type: Date,
		default: Date.now
	}
});

module.exports = mongoose.model("Category", categorySchema);
