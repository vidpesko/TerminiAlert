import { redirect } from "@sveltejs/kit";

import { getReminders } from "$lib/api";

export async function load({ cookies }) {
    const email = cookies.get("termini_email");

    if (!email) {
        throw redirect(303, "/prijava")
    }

    const reminders = await getReminders(email);

    return {
        reminders
    }
};
