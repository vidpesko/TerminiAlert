import { redirect } from "@sveltejs/kit";

export const actions = {
    default: async ({ cookies, request }) => {
        const data = await request.formData();
        const email = data.get("email");

        cookies.set("termini_email", email, { path: "/" });

        throw redirect(303, "/domov")
    },
};
