<script>
    import { onMount } from "svelte";
    import { fade } from "svelte/transition";
    import { goto, invalidateAll } from "$app/navigation";
    import { initFlowbite } from "flowbite";

    import { modal } from "$lib/stores/modal";
    import { formatDate, refreshPage } from "$lib/utils";
    import { setSlotStatus } from "$lib/api";
    import { toasts } from "$lib/stores/toast";

    let { data, form } = $props();

    let editStatus = $state(false);

    onMount(async () => {
        const handleKeydown = (event) => {
            if (event.key === "Escape") {
                modal.close();
            }
        };
        initFlowbite();
        window.addEventListener("keydown", handleKeydown);
        return () => {
            window.removeEventListener("keydown", handleKeydown);
        };
    });

    async function _setSlotStatus(reminder_id, slot_id, action) {
        await setSlotStatus(reminder_id, slot_id, action);

        // Update reminder data
        data.reminder.reminder_name = "TEST 2"
        toasts.success("Uspešno posodobljeno.");
        await invalidateAll();
        modal.close();
        initFlowbite();
        // modal.open("reminder", data.backUrl, { reminder: data.reminder });
    }
</script>


<!-- Main modal -->
<div class="overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-screen md:h-full bg-gray-900/60" transition:fade={{duration: 100 }} style="scrollbar-gutter: stable;">
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div class="absolute h-full w-full" onclick={modal.close}></div>
    <!-- Modal content -->
    <div class="relative p-4 bg-white rounded-lg shadow dark:bg-gray-800 sm:p-5 left-1/2 top-1/2 -translate-1/2 w-full z-50 mb-32 max-w-xl min-h-72">
        <!-- Modal header -->
        <div class="flex justify-between items-center pb-1 rounded-t border-b border-gray-200 dark:bg-gray-700">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                Opomnik <b>{data.reminder.reminder_name}</b>
            </h3>
            <button onclick={modal.close} type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                <span class="sr-only">Zapri</span>
            </button>
        </div>
        <!-- Modal body -->
        <div class="">
            <div class="w-full">
                <!-- Current & latest accepted date -->
                <dl class="grid gap-8 mx-auto w-full text-gray-900 sm:grid-cols-3 dark:text-white my-4">
                    <div class="flex flex-col items-center justify-center">
                        <dt class="mb-1 text-xl text-center md:text-2xl font-extrabold">{formatDate(data.reminder.current_date)}</dt>
                        <dd class="font-light text-gray-500 dark:text-gray-400">trenutni datum</dd>
                    </div>
                    <div class="flex flex-col items-center justify-center">
                        {#if data.reminder.suggested_date}
                        <dt class="mb-1 text-xl md:text-2xl font-extrabold text-center">{formatDate(data.reminder.suggested_date)}</dt>
                        <dd class="font-light text-gray-500 dark:text-gray-400">predlagan datum</dd>
                        {:else}
                        <dt class="mb-1 text-xl md:text-2xl font-extrabold">Ni datuma</dt>
                        <dd class="font-light text-gray-500 dark:text-gray-400">predlagan datum</dd>
                        {/if}
                    </div>
                    <div class="flex flex-col items-center justify-center">
                        {#if data.reminder.suggested_date && data.reminder.current_date}
                        <dt class="mb-1 text-xl md:text-2xl font-extrabold text-center">
                            {((new Date(data.reminder.current_date).getTime() - new Date(data.reminder.suggested_date).getTime()) / 86400000).toFixed(0)} dni
                        </dt>
                        <dd class="font-light text-gray-500 dark:text-gray-400">razlika</dd>
                        {:else}
                        <dt class="mb-1 text-xl md:text-2xl font-extrabold">
                            /
                        </dt>
                        <dd class="font-light text-gray-500 dark:text-gray-400">razlika</dd>
                        {/if}
                    </div>
                </dl>
                <!-- Suggested dates -->
                <div class="mb-4">
                    <h3 class="text-lg font-semibold text-gray-900 dark:text-white mb-2">Predlagani datumi</h3>
                    <div class="max-h-48 overflow-y-auto pr-2 border border-gray-200 rounded-lg bg-gray-50 dark:bg-gray-700 dark:border-gray-600">
                        {#if data.reminder.found_dates}
                        <ul class="divide-y divide-gray-200 dark:divide-gray-600">
                            {#each data.reminder.found_dates as slot}
                            <li class="py-1 ps-4 pe-2 items-center text-sm text-gray-900 dark:text-white flex justify-between w-full">
                                <p>
                                    {slot.index + 1}
                                </p>
                                <p>
                                    {formatDate(slot.date)}
                                </p>
                                <div class="flex gap-2">
                                    {#if slot.status === "needs_action" || editStatus}
                                    <button class="btn btn-primary py-1.5 px-3" onclick={async () => await _setSlotStatus(data.reminder.reminder_id, slot.id, "accept")}>
                                        Potrdi
                                    </button>
                                    <button class="btn btn-danger py-1.5 px-3" onclick={async () => await _setSlotStatus(data.reminder.reminder_id, slot.id, "reject")}>
                                        Zavrni
                                    </button>
                                    {:else}
                                        {#if slot.status === 'accepted'}
                                        <span class="bg-green-100 text-green-800 text-xs font-medium px-2.5 py-1.5 rounded-sm dark:bg-green-900 dark:text-green-300">Sprejeto</span>
                                        {:else if slot.status === 'rejected'}
                                        <span class="bg-red-100 text-red-800 text-xs font-medium px-2.5 py-1.5 rounded-sm dark:bg-red-900 dark:text-red-300">Zavrnjeno</span>
                                        {/if}
                                        <button onclick={() => editStatus = true}>
                                            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5 text-gray-500 hover:text-black" viewBox="0 0 24 24"><!-- Icon from Material Symbols by Google - https://github.com/google/material-design-icons/blob/master/LICENSE --><path fill="currentColor" d="M5 19h1.425L16.2 9.225L14.775 7.8L5 17.575zm-1 2q-.425 0-.712-.288T3 20v-2.425q0-.4.15-.763t.425-.637L16.2 3.575q.3-.275.663-.425t.762-.15t.775.15t.65.45L20.425 5q.3.275.437.65T21 6.4q0 .4-.138.763t-.437.662l-12.6 12.6q-.275.275-.638.425t-.762.15zM19 6.4L17.6 5zm-3.525 2.125l-.7-.725L16.2 9.225z"/></svg>
                                        </button>
                                    {/if}
                                </div>
                            </li>
                            {/each}
                        </ul>
                        {:else}
                        <div class="p-4 text-sm text-gray-500 dark:text-gray-400">Vsi predlagani datumi bodo prikazani tukaj.</div>
                        {/if}
                    </div>
                </div>
            </div>
            <hr class="h-px w-full my-2 text-gray-200">
            <div class="flex gap-2">
                {#if data.reminder.service_url}
                <a class="btn btn-primary btn-flex gap-2" href={data.reminder.service_url.replace("/content/singleton.html", "")} target="_blank" rel="noopener noreferrer">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" viewBox="0 0 24 24"><!-- Icon from Material Symbols by Google - https://github.com/google/material-design-icons/blob/master/LICENSE --><path fill="currentColor" d="M7 17q-2.075 0-3.537-1.463T2 12t1.463-3.537T7 7h3q.425 0 .713.288T11 8t-.288.713T10 9H7q-1.25 0-2.125.875T4 12t.875 2.125T7 15h3q.425 0 .713.288T11 16t-.288.713T10 17zm2-4q-.425 0-.712-.288T8 12t.288-.712T9 11h6q.425 0 .713.288T16 12t-.288.713T15 13zm5 4q-.425 0-.712-.288T13 16t.288-.712T14 15h3q1.25 0 2.125-.875T20 12t-.875-2.125T17 9h-3q-.425 0-.712-.288T13 8t.288-.712T14 7h3q2.075 0 3.538 1.463T22 12t-1.463 3.538T17 17z"/></svg>
                    Odpri "e-uprava.si"
                </a>
                {/if}
                <button class="btn btn-outline btn-primary-outline" onclick={modal.close}>
                    Nazaj
                </button>
            </div>
        </div>
    </div>
</div>