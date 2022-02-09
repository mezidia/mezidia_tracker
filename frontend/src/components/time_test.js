function addZeroToMinutes(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}


const date = new Date()
const currentTimeZoneOffsetInHours = date.getTimezoneOffset() / 60;
const utc_time = `${date.getHours() + currentTimeZoneOffsetInHours}:${addZeroToMinutes(date.getMinutes())}`;

const user_timezone = date.getTimezoneOffset() / 60 * (-1);

function determineTime(time, timezone) {
    return ((+time.substr(0, 2) + timezone) + time.substr(2)).toString()
}

console.log(utc_time, user_timezone)
console.log(determineTime(utc_time, user_timezone))