const API_BASE = "http://localhost:8000/api/";


export async function getReminders(email) {
    const url = API_BASE + `avp/reminders?email=${email}`;

    const response = await fetch(url);
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