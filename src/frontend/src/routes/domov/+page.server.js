import { redirect } from "@sveltejs/kit";

export function load({ cookies }) {
    const email = cookies.get("termini_email");

    if (!email) {
        throw redirect(303, "/prijava")
    }
};
