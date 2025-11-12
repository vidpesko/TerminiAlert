import { redirect } from "@sveltejs/kit";
import { HTTPS_ENABLED, DOMAIN } from "$env/static/private";


export function load({ cookies }) {
    let secure = HTTPS_ENABLED === "true" ? true : false;

    cookies.delete("termini_email", { path: "/", domain: DOMAIN, secure });
    throw redirect(303, "/prijava");
}
