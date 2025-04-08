export function load({ params, cookies }) {
    const email = cookies.get("termini_email");

    return {
        email,
    }
}