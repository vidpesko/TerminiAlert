import { toasts } from "$lib/stores/toast";


const API_BASE = "http://localhost:8008/api/";


export async function getReminders(email) {
    const url = API_BASE + `avp/reminders?email=${email}`;

    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`API napaka! Status: ${response.status}`);
    }
    const json = await response.json();
    return json;
}

export async function delReminder(id) {
    const url = API_BASE + `avp/reminder/${id}`;
    
    const response = await fetch(url, {
        method: "DELETE"
    });
    const json = await response.json();
    return json;
}

export async function createReminder(data) {
    const url = API_BASE + `avp/reminder`;

    const response = await fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    });
    const json = await response.json();
    return json;
}

export async function setSlotStatus(reminderId, slotId, status) {
    const url = API_BASE + "avp/set-slot";

    const response = await fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "reminder_id": reminderId,
            "slot_id": slotId,
            "action": status
        }),
    });
    const json = await response.json();
    return json;
}