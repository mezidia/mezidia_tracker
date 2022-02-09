const date = new Date()
const currentTimeZoneOffsetInHours = date.getTimezoneOffset() / 60;
const utc_time = `${date.getHours() + currentTimeZoneOffsetInHours}:${date.getMinutes()}`;

console.log(utc_time)