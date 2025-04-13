import { redirect } from "@sveltejs/kit";

import { createReminder, getReminders } from "$lib/api";


const filterKeys = ["exam_type", "cat", "location_district", "location", "calendar_date"];


export async function load({ params, cookies, url }) {
    const reminderId = url.searchParams.get("reminder_id");

    if (reminderId) {
        const email = cookies.get("termini_email");
        const reminders = await getReminders(email);
        const reminder = reminders.find((u) => u.reminder_id == reminderId);
        console.log(reminder);

        return {
            updating: true,
            reminder: reminder,
        };
        }
}


export const actions = {
    default: async ({ cookies, request }) => {
        const data = await request.formData();
        const dataJson = {};
        for (const [key, value] of data.entries()) {
            if (dataJson[key]) {
                // Convert to array if multiple values exist
                dataJson[key] = [].concat(dataJson[key], value);
            } else {
                dataJson[key] = value;
            }
        }
        
        const filters = {};
        for (const [key, value] of Object.entries(dataJson)) {
            if (filterKeys.includes(key)) {
                // Add values to filters dict and remove them from dataJson
                filters[key] = value;
                delete dataJson[key];
            }
        }
        dataJson.filters = filters;

        const dateRaw = dataJson.current_date;
        const timeRaw = dataJson.time;
        const [month, day, year] = dateRaw.split("/");
        const [hour, minute] = timeRaw.split(":");
        const date = new Date(`${year}-${month}-${day}T${hour}:${minute}:00`);
        const isoString = date.toISOString(); // gives UTC time like "2025-04-16T13:30:00.000Z"
        const final = isoString.replace("Z", "+01:00");
        dataJson.current_date = final;
        delete dataJson.time;

        const email = cookies.get("termini_email");
        dataJson.email = email;

        dataJson.frequency = "mid";

        const response = await createReminder(dataJson);

        throw redirect(303, "/domov");
    },
};
