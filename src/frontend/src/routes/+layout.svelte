<script>
    import LogoImg from "$lib/static/images/logo.svg";
    import LogoDarkImg from "$lib/static/images/logo dark.svg";

    import "../app.css";

    let { data, children } = $props();
</script>

<header class="antialiased">
    <nav class="bg-white border-gray-200 px-4 lg:px-6 py-2.5 dark:bg-gray-800">
        <div class="flex flex-wrap justify-between items-center">
            <!-- ! Logo -->
            <div class="flex justify-start items-center">
                <a href="/" class="flex mr-4 dark:hidden">
                <img src={LogoImg} class="mr-3 h-8" alt="Logo" />
                </a>
                <a href="/" class="mr-4 dark:flex hidden">
                <img src={LogoDarkImg} class="mr-3 h-8" alt="Logo" />
                </a>
            </div>

            <div class="flex items-center lg:order-2">
                <!-- ! If not logged -->
                {#if !data.email}
                <!-- Login button -->
                <a type="button" href="/prijava" class="hidden sm:inline-flex items-center justify-center text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-xs px-3 py-1.5 mr-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
                    <svg class="w-5 h-5 mr-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                        <path fill-rule="evenodd" d="M12 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8Zm-2 9a4 4 0 0 0-4 4v1a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-1a4 4 0 0 0-4-4h-4Z" clip-rule="evenodd"/>
                    </svg>
                    Prijava
                </a>
                {:else}
                <a href="/ustvari" type="button" class="hidden sm:inline-flex items-center justify-center text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-xs px-3 py-1.5 mr-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800">
                    <svg
                        aria-hidden="true"
                        class="mr-1 -ml-1 w-5 h-5"
                        fill="currentColor"
                        viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg"
                        ><path
                        fill-rule="evenodd"
                        d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"
                        clip-rule="evenodd"
                        ></path></svg
                        >
                        Dodaj opomnik
                </a>
                <a href="/domov" type="button" class="hidden sm:inline-flex items-center justify-center font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 py-1.5 px-3 text-sm mr-2">
                    <svg class="w-5 h-5 mr-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                        <path fill-rule="evenodd" d="M11.293 3.293a1 1 0 0 1 1.414 0l6 6 2 2a1 1 0 0 1-1.414 1.414L19 12.414V19a2 2 0 0 1-2 2h-3a1 1 0 0 1-1-1v-3h-2v3a1 1 0 0 1-1 1H7a2 2 0 0 1-2-2v-6.586l-.293.293a1 1 0 0 1-1.414-1.414l2-2 6-6Z" clip-rule="evenodd"/>
                    </svg>

                        Domov
                </a>
                <button type="button" class="py-1.5 px-3 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">
                    {data.email}
                </button>
                <!-- Dropdown menu -->
                <div
                class="hidden z-50 my-4 w-56 text-base list-none bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700 dark:divide-gray-600"
                id="dropdown"
                >
                <div class="py-3 px-4">
                    <span
                    class="block text-sm font-semibold text-gray-900 dark:text-white"
                    >Neil sims</span
                    >
                    <span
                    class="block text-sm text-gray-500 truncate dark:text-gray-400"
                    >name@flowbite.com</span
                    >
                </div>
                <ul
                    class="py-1 text-gray-500 dark:text-gray-400"
                    aria-labelledby="dropdown"
                >
                    <li>
                    <a
                        href="#"
                        class="block py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-400 dark:hover:text-white"
                        >My profile</a
                    >
                    </li>
                    <li>
                    <a
                        href="#"
                        class="block py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-400 dark:hover:text-white"
                        >Account settings</a
                    >
                    </li>
                </ul>
                <ul
                    class="py-1 text-gray-500 dark:text-gray-400"
                    aria-labelledby="dropdown"
                >
                    <li>
                    <a
                        href="#"
                        class="flex items-center py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                    >
                        <svg
                        class="mr-2 w-4 h-4 text-gray-400"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 20 18"
                        ><path
                            d="M17.947 2.053a5.209 5.209 0 0 0-3.793-1.53A6.414 6.414 0 0 0 10 2.311 6.482 6.482 0 0 0 5.824.5a5.2 5.2 0 0 0-3.8 1.521c-1.915 1.916-2.315 5.392.625 8.333l7 7a.5.5 0 0 0 .708 0l7-7a6.6 6.6 0 0 0 2.123-4.508 5.179 5.179 0 0 0-1.533-3.793Z"
                        /></svg
                        >
                        My likes
                    </a>
                    </li>
                    <li>
                    <a
                        href="#"
                        class="flex items-center py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                    >
                        <svg
                        class="mr-2 w-4 h-4 text-gray-400"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 20 20"
                        >
                        <path
                            d="m1.56 6.245 8 3.924a1 1 0 0 0 .88 0l8-3.924a1 1 0 0 0 0-1.8l-8-3.925a1 1 0 0 0-.88 0l-8 3.925a1 1 0 0 0 0 1.8Z"
                        />
                        <path
                            d="M18 8.376a1 1 0 0 0-1 1v.163l-7 3.434-7-3.434v-.163a1 1 0 0 0-2 0v.786a1 1 0 0 0 .56.9l8 3.925a1 1 0 0 0 .88 0l8-3.925a1 1 0 0 0 .56-.9v-.786a1 1 0 0 0-1-1Z"
                        />
                        <path
                            d="M17.993 13.191a1 1 0 0 0-1 1v.163l-7 3.435-7-3.435v-.163a1 1 0 1 0-2 0v.787a1 1 0 0 0 .56.9l8 3.925a1 1 0 0 0 .88 0l8-3.925a1 1 0 0 0 .56-.9v-.787a1 1 0 0 0-1-1Z"
                        />
                        </svg>
                        Collections
                    </a>
                    </li>
                    <li>
                    <a
                        href="#"
                        class="flex justify-between items-center py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                    >
                        <span class="flex items-center">
                        <svg
                            class="mr-2 w-4 h-4 text-primary-600 dark:text-primary-500"
                            aria-hidden="true"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="currentColor"
                            viewBox="0 0 20 20"
                            ><path
                            d="m7.164 3.805-4.475.38L.327 6.546a1.114 1.114 0 0 0 .63 1.89l3.2.375 3.007-5.006ZM11.092 15.9l.472 3.14a1.114 1.114 0 0 0 1.89.63l2.36-2.362.38-4.475-5.102 3.067Zm8.617-14.283A1.613 1.613 0 0 0 18.383.291c-1.913-.33-5.811-.736-7.556 1.01-1.98 1.98-6.172 9.491-7.477 11.869a1.1 1.1 0 0 0 .193 1.316l.986.985.985.986a1.1 1.1 0 0 0 1.316.193c2.378-1.3 9.889-5.5 11.869-7.477 1.746-1.745 1.34-5.643 1.01-7.556Zm-3.873 6.268a2.63 2.63 0 1 1-3.72-3.72 2.63 2.63 0 0 1 3.72 3.72Z"
                            /></svg
                        >
                        Pro version
                        </span>
                        <svg
                        class="w-2.5 h-2.5 text-gray-400"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 6 10"
                        ><path
                            stroke="currentColor"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="m1 9 4-4-4-4"
                        /></svg
                        >
                    </a>
                    </li>
                </ul>
                
                <ul
                class="py-1 text-gray-500 dark:text-gray-400"
                aria-labelledby="dropdown"
                >
                <li>
                    <a
                    href="#"
                    class="block py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white"
                    >Sign out</a
                    >
                </li>
                </ul>
                </div>
            {/if}
            </div>
        </div>
    </nav>
</header>

<div class="min-h-[95vh]">
    {@render children()}
</div>

<footer class="p-4 bg-white md:p-8 lg:p-10 dark:bg-gray-800">
    <div class="mx-auto max-w-screen-xl text-center">
        <a
        href="/"
        class="flex dark:hidden justify-center items-center text-2xl font-semibold text-gray-900 dark:text-white"
        >
        <img src={LogoImg} class="mr-3 h-8" alt="Logo" />
        </a>
        <a
        href="/"
        class="dark:flex hidden justify-center items-center text-2xl font-semibold text-gray-900 dark:text-white"
        >
        <img src={LogoDarkImg} class="mr-3 h-8" alt="Logo" />
        </a>
        <p class="my-6 text-gray-500 dark:text-gray-400">
        Brezplačna aplikacija za obveščanje o prostih terminih za opravljanje
        vozniškega izpita.
        </p>
        <ul
        class="flex flex-wrap justify-center items-center mb-6 text-gray-900 dark:text-white"
        >
        <li>
            <a href="#" class="mr-4 hover:underline md:mr-6">About</a>
        </li>
        <li>
            <a href="#" class="mr-4 hover:underline md:mr-6">Premium</a>
        </li>
        <li>
            <a href="#" class="mr-4 hover:underline md:mr-6">Campaigns</a>
        </li>
        <li>
            <a href="#" class="mr-4 hover:underline md:mr-6">Blog</a>
        </li>
        <li>
            <a href="#" class="mr-4 hover:underline md:mr-6">Affiliate Program</a>
        </li>
        <li>
            <a href="#" class="mr-4 hover:underline md:mr-6">FAQs</a>
        </li>
        <li>
            <a href="#" class="mr-4 hover:underline md:mr-6">Contact</a>
        </li>
        </ul>
        <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400"
        >© 2025 <a href="#" class="hover:underline">Termini™</a></span
        >
    </div>
</footer>
