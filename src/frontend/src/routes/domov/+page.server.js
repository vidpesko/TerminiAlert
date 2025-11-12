import { redirect } from "@sveltejs/kit";

import { toasts } from "$lib/stores/toast";
import { getReminders } from "$lib/api";

export async function load({ cookies }) {
    const email = cookies.get("termini_email");

    if (!email) {
        throw redirect(303, "/prijava")
    }

    let reminders = [];
    let errors = null;
    try {
        reminders = await getReminders(email);
    } catch (error) {
        errors = [error.message, ]
    }


    return {
        reminders,
        errors,
    }
};
