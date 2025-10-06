import { goto } from '$app/navigation';
import { writable } from 'svelte/store';

function createModalStore() {
    const { subscribe, update } = writable({});

    function open(modalName, backUrl = null, data = {}) {
        data.backUrl = backUrl;
        update((modal) => modal = {
            modalName,
            backUrl,
            state: "open",
            data,
        });
    }

    function close() {
        let backUrl;
        const unsubscribe = subscribe(modal => {
            backUrl = modal.backUrl;
        });
        unsubscribe(); // Immediately unsubscribe to avoid memory leaks

        update((modal) => modal = {
            modalName: null,
            backUrl: null,
            state: "close",
            data: {},
        });

        if (backUrl) {
            goto(backUrl);
        }
    }

    return {
        subscribe,
        close,
        open,
    };
}

export const modal = createModalStore();
