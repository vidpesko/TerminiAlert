import { redirect } from "@sveltejs/kit";


const filterKeys = ["exam_type", "cat", "location_district", "location", "calendar_date"];


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

        const email = cookies.get("termini_email");
        dataJson.email = email;

        console.log(dataJson);

        // throw redirect(303, "/domov");
    },
};
