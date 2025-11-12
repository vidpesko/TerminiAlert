import { redirect } from "@sveltejs/kit";
import { HTTPS_ENABLED, DOMAIN } from "$env/static/private";

export const actions = {
    default: async ({ cookies, request }) => {
        const data = await request.formData();
        const email = data.get("email");

        let secure = HTTPS_ENABLED === "true" ? true : false;

        cookies.set("termini_email", email, { path: "/", domain: DOMAIN, secure });

        throw redirect(303, "/domov")
    },
};
