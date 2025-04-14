<script>
    let { data } = $props();

    import { delReminder } from '$lib/api';

    let reminders = $derived(data.reminders);

    async function deleteReminder(event, id) {
        const response = await delReminder(id);

        reminders = reminders.filter(item => item.reminder_id !== id);
    }
</script>

<section class="bg-background dark:bg-background-dark py-10 min-h-[95vh]">
    <div class="flex justify-evenly gap-4 px-10">
        <div class="custom-container w-3/4">
            
            <div class="relative overflow-hidden">
                <div class="flex flex-col md:flex-row items-center justify-between p-4 pt-2 px-0 text-center">
                    <h2 class="text-2xl font-bold text-gray-900 dark:text-white text-center flex items-center gap-2">
                        <svg class="w-7 h-7 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z"/>
                        </svg>

                        Moji opomniki
                    </h2>
                    <div class="w-full md:w-auto flex flex-col md:flex-row items-stretch md:items-center justify-end md:space-x-3 flex-shrink-0">
                        <a href="/ustvari" type="button" class="flex items-center justify-center text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
                            <svg class="h-3.5 w-3.5 mr-2" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                                <path clip-rule="evenodd" fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" />
                            </svg>
                            Dodaj opomnik
                        </a>
                    </div>
                </div>
                <div class="overflow-x-auto">
                    {#key reminders}
                    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                            <tr>
                                <th scope="col" class="px-4 py-3">Ime</th>
                                <th scope="col" class="px-4 py-3">Tip</th>
                                <th scope="col" class="px-4 py-3">Trenutni datum</th>
                                <th scope="col" class="px-4 py-3">Predlagan datum</th>
                                <th scope="col" class="px-4 py-3">
                                    <span class="sr-only">Actions</span>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            {#each reminders as reminder}
                            <tr class="border-b dark:border-gray-700">
                                <th scope="row" class="px-4 py-3 font-medium text-gray-900 whitespace-nowrap dark:text-white">{reminder.reminder_name}</th>
                                <td class="px-4 py-3">{(reminder.filters.exam_type == 1) ? "Teorija" : "Vožnja"}</td>
                                <td class="px-4 py-3">{reminder.current_date}</td>
                                <td class="px-4 py-3">{reminder.suggested_date}</td>
                                <td class="px-4 py-3 flex items-center justify-end">
                                    <!-- svelte-ignore a11y_consider_explicit_label -->
                                    <button id="reminder-{reminder.reminder_id}-dropdown-button" data-dropdown-toggle="reminder-{reminder.reminder_id}-dropdown" class="inline-flex items-center p-0.5 text-sm font-medium text-center text-gray-500 hover:text-gray-800 rounded-lg focus:outline-none dark:text-gray-400 dark:hover:text-gray-100" type="button">
                                        <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewbox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z" />
                                        </svg>
                                    </button>
                                    <div id="reminder-{reminder.reminder_id}-dropdown" class="hidden z-10 w-44 bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700 dark:divide-gray-600">
                                        <ul class="py-1 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="reminder-{reminder.reminder_id}-dropdown-button">
                                            <li>
                                                <a href="/uredi?id={reminder.reminder_id}" class="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Uredi</a>
                                            </li>
                                        </ul>
                                        <div class="py-1">
                                            <button onclick={(event) => deleteReminder(event, reminder.reminder_id)} class="block py-2 px-4 text-sm text-gray-700 hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-200 dark:hover:text-white w-full text-start">Izbriši</button>
                                        </div>
                                    </div>
                                </td>
                            </tr>
                            {/each}
                        </tbody>
                    </table>
                    {/key}
                </div>
            </div>
        </div>

        <div class="custom-container w-1/4 ">
            <h2 class="my-2 text-2xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
                <svg class="w-7 h-7 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7.556 8.5h8m-8 3.5H12m7.111-7H4.89a.896.896 0 0 0-.629.256.868.868 0 0 0-.26.619v9.25c0 .232.094.455.26.619A.896.896 0 0 0 4.89 16H9l3 4 3-4h4.111a.896.896 0 0 0 .629-.256.868.868 0 0 0 .26-.619v-9.25a.868.868 0 0 0-.26-.619.896.896 0 0 0-.63-.256Z"/>
                </svg>

                Obvestila
            </h2>
            
            <div class="">
                <div class="rounded-lg shadow border border-gray-200 w-full p-2 text-black dark:text-white">
                    <div class="">
                        <h4 class="font-bold">Moj opomnik</h4>
                        <p>Najdel je bil termin za opomnik kategorije XY</p>
                    </div>
                    <div class="flex gap-2 justify-between my-4">
                        <!-- New date / suggested date -->
                        <div class="text-center text-red-800 dark:text-red-400 text-sm">
                            <p>Trenutno</p>
                            <p class="font-bold text-base">16.</p>
                            <p>April</p>
                        </div>
                        <div class="text-center text-green-800 dark:text-green-400 text-sm">
                            <p>Nov termin</p>
                            <p class="font-bold text-base">13.</p>
                            <p>Marec</p>
                        </div>
                        <div class="text-center text-sm">
                            <p>Razlika</p>
                            <p class="font-bold text-base">30</p>
                            <p>dni</p>
                        </div>
                    </div>
                    <div class="flex gap-2">
                        <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">Sprejmi</button>
                        <button type="button" class="text-red-700 hover:text-white border border-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-3 py-1.5 text-center dark:border-red-500 dark:text-red-500 dark:hover:text-white dark:hover:bg-red-600 dark:focus:ring-red-900">Opusti</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>