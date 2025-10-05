import { goto } from "$app/navigation";
import { page } from "$app/state";

export function refreshPage() {
    goto(page.url.pathname, { invalidateAll: false });
}

export function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('sl-SI', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    }).replace(',', ' ob');
}