import { goto } from "$app/navigation";
import { page } from "$app/state";

export function refreshPage() {
    goto(page.url.pathname, { invalidateAll: false });
}
