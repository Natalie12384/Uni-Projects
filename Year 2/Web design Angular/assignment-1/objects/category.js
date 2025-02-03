/**
 * Represents a category object
 * @author Yizhou Huang <yhua0183@student.monash.edu>
 */
class Category {
	/**
     * @constructor
     * @param {String} name 
     * @param {String} description 
     * @param {String} image 
     */
	constructor(name, description, imagePath) {
		this.id = "C" +
			String.fromCharCode(Math.round(Math.random() * (90 - 65) + 65)) + //using the ASCII code to generate a random alphbet
			String.fromCharCode(Math.round(Math.random() * (90 - 65) + 65)) + //using the ASCII code to generate a random alphbet
			"-" +
			//generate a random integer between 1-9999, and if the number isn't 4 digits, it will fill the blank with 0
			//for example, 89 will be 0089
			(Math.floor(Math.random() * 9999) + 1).toString().padStart(4, '0'); 
		this.name = name;
		this.description = description;
		this.imagePath = imagePath;
		this.createdAt = new Date();
	}
}

module.exports = Category;
