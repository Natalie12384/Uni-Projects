/**
 * Represents a event object
 * @author Natalie Chan <ncha0086@student.monash.edu>
 */
class Event{
    /**
     * @constructor
     * @param {String} name 
     * @param {String} desc 
     * @param {Date} startDate 
     * @param {boolean} isActive 
     * @param {Number} capacity 
     * @param {Number} ticketsAvailable 
     * @param {Number} duration 
     * @param {String} image 
     * @param {String} catId 
     */
    constructor(name,desc, startDate,isActive, capacity, ticketsAvailable, duration,image, catId ){
        this.name= name;
        this.desc = desc;
        this.startDate= startDate;
        this.isActive= isActive;
        this.capacity=capacity;
        this.ticketsAvailable=ticketsAvailable;
        this.duration= duration;
        this.image = image;
        this.catId= catId;
        this.id=this.makeRandomId();
        this.endDate = this.calculateEndDate(duration, startDate);
    }

    /**
     * Randomly assigns numbers and letters for a event ID
     * @returns {String} formatted string of event id
     */
    makeRandomId(){
        let retStr = "E"
        const list = "ABCDEFGHIJKLMNPQRSTUVWXYZ";
        let str = "";
        for(let i = 0; i < 3; i++) {
            str = str + list.charAt(Math.floor(Math.random() * list.length));            
        }
        retStr = retStr+str.substring(0,2)+"-"+Math.floor(Math.random()*10000).toString().padStart(4, '0');;
        return retStr;
    }

    /**
     * Creates the formatted end date of an event based on starting DateTime object date and duration of the event.
     * @param {Number} minutes - duration of event in minutes
     * @param {Date} startDate - starting time and date of event
     * @returns {String} formatted return string of 
     */
    calculateEndDate(minutes, startDate){
        const date = new Date(startDate);
        const newDate = new Date(date.setMinutes(date.getMinutes()+minutes));
        return `${newDate.getDate()}/${newDate.getMonth()}/${newDate.getYear()+1900}, ${newDate.getHours()>12?newDate.getHours()-12:newDate.getHours()}:${newDate.getMinutes()}:00 ${newDate.getHours()>12?"PM":"AM"}`;  
    }
}

module.exports = Event;