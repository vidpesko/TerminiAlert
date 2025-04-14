import { redirect } from "@sveltejs/kit";


export function load({ cookies }) {
    cookies.delete("termini_email", { path: "/" });
    redirect(303, "/prijava")
}
