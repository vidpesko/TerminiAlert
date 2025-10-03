<script>
    import { onMount } from 'svelte';
    import { initFlowbite } from 'flowbite';
    import { enhance } from '$app/forms';

    import Breadcrumbs from "$lib/components/Breadcrumbs.svelte";

    import { locationOptions } from "$lib/options";
    import { toasts } from "$lib/stores/toast.js";
  import { goto } from '$app/navigation';

    let { data } = $props();
    
    let examType = $state();

    const structure = [
        {
            name: "Ustvari",
            link: "/ustvari"
        }
    ]

    var locationDisctrict = $state();

    onMount(() => {
        initFlowbite();
    });
</script>


<section class="bg-background dark:bg-background-dark py-10 min-h-[95vh]">
    <div class="pt-4 pb-8 px-4 mx-auto max-w-2xl bg-white dark:bg-gray-800 shadow rounded-lg dark:border dark:border-gray-700">
        <Breadcrumbs structure={structure} />

        <h2 class="mb-4 text-xl font-bold text-gray-900 dark:text-white mt-6">Ustvari opomnik</h2>
        <form method="POST" use:enhance={() => {
            return () => {
                goto('/domov');
                toasts.success("Opomnik je bil uspešno ustvarjen.");
            }
        }}>
            <div class="grid gap-4 sm:grid-cols-2 sm:gap-6">
                <div class="col-span-2">
                    <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Ime opomnika (ni obvezno)</label>
                    <input type="text" name="reminder_name" id="name" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500" placeholder="Vnesi ime opomnika">
                </div>

                <div class="">
                    <p class="text-sm font-medium text-gray-900 dark:text-white mb-2">Trenutni datum izpita</p>
                    <div class="relative max-w-sm">
                        <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
                            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                                <path d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"/>
                            </svg>
                        </div>
                        <input required datepicker id="default-datepicker" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Izberite datum" name="current_date">
                    </div>
                </div>
                <div class="">
                    <p class="text-sm font-medium text-gray-900 dark:text-white mb-2">Ura izpita</p>
                    <div class="relative">
                        <div class="absolute inset-y-0 end-0 top-0 flex items-center pe-3.5 pointer-events-none">
                            <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                                <path fill-rule="evenodd" d="M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z" clip-rule="evenodd"/>
                            </svg>
                        </div>
                        <input type="time" id="time" class="bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-3 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" name="time" value="00:00" required />
                    </div>
                </div>

                <div class="col-span-2">
                    <p class="text-sm font-medium text-gray-900 dark:text-white mb-2">Tip izpita</p>
                    <ul class="items-center w-full text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg sm:flex dark:bg-gray-700 dark:border-gray-600 dark:text-white">
                        <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                            <div class="flex items-center ps-3">
                                <input bind:group={examType} id="horizontal-list-radio-license" type="radio" value="2" name="exam_type" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" required>
                                <label for="horizontal-list-radio-license" class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Teorija (CPP)</label>
                            </div>
                        </li>
                        <li class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600">
                            <div class="flex items-center ps-3">
                                <input bind:group={examType} id="horizontal-list-radio-id" type="radio" value="1" name="exam_type" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500" required>
                                <label for="horizontal-list-radio-id" class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Vožnja</label>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="">
                    <label for="location-district" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Izberi obmocje</label>
                    <select bind:value={locationDisctrict} id="location-district" name="location_district" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        <option value="-1" selected>Vsa območja</option>
                        <option value="17">Območje 1: AJDOVŠČINA , IDRIJA , ILIRSKA BISTRICA , KOPER , NOVA GORICA , POSTOJNA EPIC , SEŽANA , TOLMIN , TOLMIN IIN</option>
                        <option value="18">Območje 2: DOMŽALE , IG , JESENICE , KRANJ , LJUBLJANA , VRHNIKA</option>
                        <option value="19">Območje 3: CELJE , LAŠKO , LOČICA OB SAVINJI , RAVNE NA KOROŠKEM , SLOVENSKE KONJICE , SLOVENJ GRADEC , ŠENTJUR , ŠMARJE PRI JELŠAH , TRBOVLJE , VELENJE</option>
                        <option value="20">Območje 4: BREŽICE , BREŽICE TEORIJA , ČRNOMELJ , KOČEVJE , KOČEVJE ŠD GAJ , KOČEVJE VADBENA POVRŠINA HERBBY , KRŠKO , NOVO MESTO BTC ČEŠČA VAS BE CE , NOVO MESTO UE , SEVNICA</option>
                        <option value="21">Območje 5: MARIBOR , MURSKA SOBOTA , ORMOŽ , PTUJ , PTUJ CCE KAT , PTUJ KAT , SLOVENSKA BISTRICA</option>
                    </select>
                </div>
                <div class="">
                    <label for="location" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Izberi kraj</label>
                    {#key locationDisctrict}
                    <select id="location" name="location" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                        <option value="-1" selected>Vse lokacije</option>
                        {#each locationOptions[locationDisctrict] as opt}
                        {#if examType == 2}
                            {#if opt[1].includes("TESTIRNICA")}
                            <option value={opt[0]}>{opt[1]}</option>
                            {/if}
                        {:else if examType == 1}
                            {#if !opt[1].includes("TESTIRNICA")}
                            <option value={opt[0]}>{opt[1]}</option>
                            {/if}
                        {:else}
                            <option value={opt[0]}>{opt[1]}</option>
                        {/if}
                        {/each}
                    </select>
                    {/key}
                </div>

                <div class="col-span-2">
                    <p class="text-sm font-medium text-gray-900 dark:text-white mb-2">Kategorije</p>
                    <div class="grid grid-cols-4 gap-2">
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-A" type="checkbox" value="4" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-A" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">A</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-A1" type="checkbox" value="2" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-A1" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">A1</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-A2" type="checkbox" value="3" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-A2" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">A2</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-AM" type="checkbox" value="1" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-AM" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">AM</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-B" type="checkbox" value="6" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600" checked>
                            <label for="category-B" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">B</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-B1" type="checkbox" value="5" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-B1" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">B1</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-BE" type="checkbox" value="7" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-BE" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">BE</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-C" type="checkbox" value="10" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-C" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">C</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-C1" type="checkbox" value="8" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-C1" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">C1</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-C1E" type="checkbox" value="9" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-C1E" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">C1E</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-CE" type="checkbox" value="11" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-CE" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">CE</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-D" type="checkbox" value="14" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-D" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">D</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-D1" type="checkbox" value="12" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-D1" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">D1</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-D1E" type="checkbox" value="13" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-D1E" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">D1E</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-DE" type="checkbox" value="15" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-DE" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">DE</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-F" type="checkbox" value="16" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-F" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">F</label>
                        </div>
                        <div class="flex items-center ps-4 border border-gray-200 rounded-sm dark:border-gray-700">
                            <input id="category-G" type="checkbox" value="17" name="cat" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded-sm focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                            <label for="category-G" class="w-full py-4 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">G</label>
                        </div>
                    </div>
                </div>
            </div>

            <button type="submit" class="inline-flex items-center px-5 py-2.5 mt-4 sm:mt-6 text-sm font-medium text-center text-white bg-primary-700 rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
                Ustvari
            </button>
            <a href="/domov" class="text-red-700 hover:text-white border border-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2 dark:border-red-500 dark:text-red-500 dark:hover:text-white dark:hover:bg-red-600 dark:focus:ring-red-900">Pojdi nazaj</a>
        </form>
    </div>
</section>