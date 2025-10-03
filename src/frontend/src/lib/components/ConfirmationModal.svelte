<script>
    import { onMount } from "svelte";
    import { fade } from "svelte/transition";
    import { initFlowbite } from "flowbite";

    import { modal } from "$lib/stores/modal";


    let { data, form } = $props();

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
</script>


<!-- Main modal -->
<div class="overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-screen md:h-full bg-gray-900/60" transition:fade={{duration: 100 }} style="scrollbar-gutter: stable;">
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div class="absolute h-full w-full" onclick={modal.close}></div>
    <!-- Modal content -->
    <div class="relative p-4 bg-white rounded-lg shadow dark:bg-gray-800 sm:p-5 left-1/2 top-1/2 -translate-1/2 w-full z-50 mb-32 max-w-96">
        <!-- Modal header -->
        <div class="flex justify-between items-center pb-4 mb-2 rounded-t border-b sm:mb-5 border-gray-200 dark:bg-gray-700">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">
                {@html data.title}
            </h3>
            <button onclick={modal.close} type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                <span class="sr-only">Zapri</span>
            </button>
        </div>
        <!-- Modal body -->
        <div class="">
            <p class="mb-4">Izbrisali boste opomnik <b>"{data.name}"</b>. Ali želite nadaljevati?</p>
            <button class="btn btn-danger" onclick={async () => {
                await data.execute()
                modal.close();
            }}>
                {data.confirmBtnText}
            </button>
            <button class="btn btn-outline btn-primary-outline" onclick={modal.close}>
                Prekliči
            </button>
        </div>
    </div>
</div>