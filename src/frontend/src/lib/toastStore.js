import { writable } from "svelte/store";

function createToastStore() {
    const { subscribe, update } = writable([]);
    let toastId = 0;

    function send(message, type = "info", duration = 3000) {
        const id = toastId++;
        update((toasts) => [...toasts, { id, message, type, duration }]);

        setTimeout(() => {
        update((toasts) => toasts.filter((t) => t.id !== id));
        }, duration);
    }

    return {
        subscribe,
        send,
        info: (msg, dur) => send(msg, "info", dur),
        success: (msg, dur) => send(msg, "success", dur),
        error: (msg, dur) => send(msg, "error", dur),
    };
}

export const toasts = createToastStore();
