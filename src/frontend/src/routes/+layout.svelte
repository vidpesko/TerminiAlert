<script>
	import '../app.css';
	
	let { children } = $props();
</script>


<header class="antialiased">
    <nav class="bg-white border-gray-200 px-4 lg:px-6 py-2.5 dark:bg-gray-800">
        <div class="flex flex-wrap justify-between items-center">
            <div class="flex justify-start items-center">
                <a href="https://flowbite.com" class="flex mr-4">
                    <img src="https://flowbite.s3.amazonaws.com/logo.svg" class="mr-3 h-8" alt="FlowBite Logo" />
                    <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Flowbite</span>
                </a>
                </div>
            <div class="flex items-center lg:order-2">
                <button type="button" class="hidden sm:inline-flex items-center justify-center text-white bg-primary-700 hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 font-medium rounded-lg text-xs px-3 py-1.5 mr-2 dark:bg-primary-600 dark:hover:bg-primary-700 focus:outline-none dark:focus:ring-primary-800"><svg aria-hidden="true" class="mr-1 -ml-1 w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z" clip-rule="evenodd"></path></svg> New Widget</button>


                <!-- Notifications -->
                <button type="button" data-dropdown-toggle="notification-dropdown" class="p-2 mr-1 text-gray-500 rounded-lg hover:text-gray-900 hover:bg-gray-100 dark:text-gray-400 dark:hover:text-white dark:hover:bg-gray-700 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600">
                    <span class="sr-only">View notifications</span>
                    <!-- Bell icon -->
                    <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 14 20"><path d="M12.133 10.632v-1.8A5.406 5.406 0 0 0 7.979 3.57.946.946 0 0 0 8 3.464V1.1a1 1 0 0 0-2 0v2.364a.946.946 0 0 0 .021.106 5.406 5.406 0 0 0-4.154 5.262v1.8C1.867 13.018 0 13.614 0 14.807 0 15.4 0 16 .538 16h12.924C14 16 14 15.4 14 14.807c0-1.193-1.867-1.789-1.867-4.175ZM3.823 17a3.453 3.453 0 0 0 6.354 0H3.823Z"/></svg>
                </button>
                <!-- Dropdown menu -->
                <div class="hidden overflow-hidden z-50 my-4 max-w-sm text-base list-none bg-white rounded divide-y divide-gray-100 shadow-lg dark:divide-gray-600 dark:bg-gray-700" id="notification-dropdown">
                    <div class="block py-2 px-4 text-base font-medium text-center text-gray-700 bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                        Notifications
                    </div>
                    <div>
                    <a href="#" class="flex py-3 px-4 border-b hover:bg-gray-100 dark:hover:bg-gray-600 dark:border-gray-600">
                        <div class="flex-shrink-0">
                        <img class="w-11 h-11 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/bonnie-green.png" alt="Bonnie Green avatar">
                        <div class="flex absolute justify-center items-center ml-6 -mt-5 w-5 h-5 rounded-full border border-white bg-primary-700 dark:border-gray-700">
                            <svg class="w-2 h-2 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 18"><path d="M15.977.783A1 1 0 0 0 15 0H3a1 1 0 0 0-.977.783L.2 9h4.239a2.99 2.99 0 0 1 2.742 1.8 1.977 1.977 0 0 0 3.638 0A2.99 2.99 0 0 1 13.561 9H17.8L15.977.783ZM6 2h6a1 1 0 1 1 0 2H6a1 1 0 0 1 0-2Zm7 5H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Z"/><path d="M1 18h16a1 1 0 0 0 1-1v-6h-4.439a.99.99 0 0 0-.908.6 3.978 3.978 0 0 1-7.306 0 .99.99 0 0 0-.908-.6H0v6a1 1 0 0 0 1 1Z"/></svg>
                        </div>
                        </div>
                        <div class="pl-3 w-full">
                            <div class="text-gray-500 font-normal text-sm mb-1.5 dark:text-gray-400">New message from <span class="font-semibold text-gray-900 dark:text-white">Bonnie Green</span>: "Hey, what's up? All set for the presentation?"</div>
                            <div class="text-xs font-medium text-primary-700 dark:text-primary-400">a few moments ago</div>
                        </div>
                    </a>
                    <a href="#" class="flex py-3 px-4 border-b hover:bg-gray-100 dark:hover:bg-gray-600 dark:border-gray-600">
                        <div class="flex-shrink-0">
                        <img class="w-11 h-11 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/jese-leos.png" alt="Jese Leos avatar">
                        <div class="flex absolute justify-center items-center ml-6 -mt-5 w-5 h-5 bg-gray-900 rounded-full border border-white dark:border-gray-700">
                            <svg class="w-2 h-2 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18"><path d="M6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Zm11-3h-2V5a1 1 0 0 0-2 0v2h-2a1 1 0 1 0 0 2h2v2a1 1 0 0 0 2 0V9h2a1 1 0 1 0 0-2Z"/></svg>
                        </div>
                        </div>
                        <div class="pl-3 w-full">
                            <div class="text-gray-500 font-normal text-sm mb-1.5 dark:text-gray-400"><span class="font-semibold text-gray-900 dark:text-white">Jese leos</span> and <span class="font-medium text-gray-900 dark:text-white">5 others</span> started following you.</div>
                            <div class="text-xs font-medium text-primary-700 dark:text-primary-400">10 minutes ago</div>
                        </div>
                    </a>
                    <a href="#" class="flex py-3 px-4 border-b hover:bg-gray-100 dark:hover:bg-gray-600 dark:border-gray-600">
                        <div class="flex-shrink-0">
                        <img class="w-11 h-11 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/joseph-mcfall.png" alt="Joseph McFall avatar">
                        <div class="flex absolute justify-center items-center ml-6 -mt-5 w-5 h-5 bg-red-600 rounded-full border border-white dark:border-gray-700">
                            <svg class="w-2 h-2 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18"> <path d="M17.947 2.053a5.209 5.209 0 0 0-3.793-1.53A6.414 6.414 0 0 0 10 2.311 6.482 6.482 0 0 0 5.824.5a5.2 5.2 0 0 0-3.8 1.521c-1.915 1.916-2.315 5.392.625 8.333l7 7a.5.5 0 0 0 .708 0l7-7a6.6 6.6 0 0 0 2.123-4.508 5.179 5.179 0 0 0-1.533-3.793Z"/> </svg>                      
                        </div>
                        </div>
                        <div class="pl-3 w-full">
                            <div class="text-gray-500 font-normal text-sm mb-1.5 dark:text-gray-400"><span class="font-semibold text-gray-900 dark:text-white">Joseph Mcfall</span> and <span class="font-medium text-gray-900 dark:text-white">141 others</span> love your story. See it and view more stories.</div>
                            <div class="text-xs font-medium text-primary-700 dark:text-primary-400">44 minutes ago</div>
                        </div>
                    </a>
                    <a href="#" class="flex py-3 px-4 border-b hover:bg-gray-100 dark:hover:bg-gray-600 dark:border-gray-600">
                        <div class="flex-shrink-0">
                        <img class="w-11 h-11 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/roberta-casas.png" alt="Roberta Casas image">
                        <div class="flex absolute justify-center items-center ml-6 -mt-5 w-5 h-5 bg-green-400 rounded-full border border-white dark:border-gray-700">
                            <svg class="w-2 h-2 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18"><path d="M18 0H2a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h2v4a1 1 0 0 0 1.707.707L10.414 13H18a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm-5 4h2a1 1 0 1 1 0 2h-2a1 1 0 1 1 0-2ZM5 4h5a1 1 0 1 1 0 2H5a1 1 0 0 1 0-2Zm2 5H5a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Zm9 0h-6a1 1 0 0 1 0-2h6a1 1 0 1 1 0 2Z"/></svg>
                        </div>
                        </div>
                        <div class="pl-3 w-full">
                            <div class="text-gray-500 font-normal text-sm mb-1.5 dark:text-gray-400"><span class="font-semibold text-gray-900 dark:text-white">Leslie Livingston</span> mentioned you in a comment: <span class="font-medium text-primary-700 dark:text-primary-500">@bonnie.green</span> what do you say?</div>
                            <div class="text-xs font-medium text-primary-700 dark:text-primary-400">1 hour ago</div>
                        </div>
                    </a>
                    <a href="#" class="flex py-3 px-4 hover:bg-gray-100 dark:hover:bg-gray-600">
                        <div class="flex-shrink-0">
                        <img class="w-11 h-11 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/robert-brown.png" alt="Robert image">
                        <div class="flex absolute justify-center items-center ml-6 -mt-5 w-5 h-5 bg-purple-500 rounded-full border border-white dark:border-gray-700">
                            <svg class="w-2 h-2 text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 14"><path d="M11 0H2a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2Zm8.585 1.189a.994.994 0 0 0-.9-.138l-2.965.983a1 1 0 0 0-.685.949v8a1 1 0 0 0 .675.946l2.965 1.02a1.013 1.013 0 0 0 1.032-.242A1 1 0 0 0 20 12V2a1 1 0 0 0-.415-.811Z"/></svg>
                        </div>
                        </div>
                        <div class="pl-3 w-full">
                            <div class="text-gray-500 font-normal text-sm mb-1.5 dark:text-gray-400"><span class="font-semibold text-gray-900 dark:text-white">Robert Brown</span> posted a new video: Glassmorphism - learn how to implement the new design trend.</div>
                            <div class="text-xs font-medium text-primary-700 dark:text-primary-400">3 hours ago</div>
                        </div>
                    </a>
                    </div>
                    <a href="#" class="block py-2 text-base font-medium text-center text-gray-900 bg-gray-50 hover:bg-gray-100 dark:bg-gray-700 dark:text-white dark:hover:underline">
                        <div class="inline-flex items-center ">
                        <svg aria-hidden="true" class="mr-2 w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M10 12a2 2 0 100-4 2 2 0 000 4z"></path><path fill-rule="evenodd" d="M.458 10C1.732 5.943 5.522 3 10 3s8.268 2.943 9.542 7c-1.274 4.057-5.064 7-9.542 7S1.732 14.057.458 10zM14 10a4 4 0 11-8 0 4 4 0 018 0z" clip-rule="evenodd"></path></svg>
                        View all
                        </div>
                    </a>
                </div>


                <button type="button" class="flex mx-3 text-sm bg-gray-800 rounded-full md:mr-0 focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600" id="user-menu-button" aria-expanded="false" data-dropdown-toggle="dropdown">
                    <span class="sr-only">Open user menu</span>
                    <img class="w-8 h-8 rounded-full" src="https://flowbite.com/docs/images/people/profile-picture-5.jpg" alt="user photo">
                </button>
                <!-- Dropdown menu -->
                <div class="hidden z-50 my-4 w-56 text-base list-none bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700 dark:divide-gray-600" id="dropdown">
                    <div class="py-3 px-4">
                        <span class="block text-sm font-semibold text-gray-900 dark:text-white">Neil sims</span>
                        <span class="block text-sm text-gray-500 truncate dark:text-gray-400">name@flowbite.com</span>
                    </div>
                    <ul class="py-1 text-gray-500 dark:text-gray-400" aria-labelledby="dropdown">
                        <li>
                            <a href="#" class="block py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-400 dark:hover:text-white">My profile</a>
                        </li>
                        <li>
                            <a href="#" class="block py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:text-gray-400 dark:hover:text-white">Account settings</a>
                        </li>
                    </ul>
                    <ul class="py-1 text-gray-500 dark:text-gray-400" aria-labelledby="dropdown">
                            <li>
                            <a href="#" class="flex items-center py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                                <svg class="mr-2 w-4 h-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18"><path d="M17.947 2.053a5.209 5.209 0 0 0-3.793-1.53A6.414 6.414 0 0 0 10 2.311 6.482 6.482 0 0 0 5.824.5a5.2 5.2 0 0 0-3.8 1.521c-1.915 1.916-2.315 5.392.625 8.333l7 7a.5.5 0 0 0 .708 0l7-7a6.6 6.6 0 0 0 2.123-4.508 5.179 5.179 0 0 0-1.533-3.793Z"/></svg>
                                My likes
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex items-center py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                                <svg class="mr-2 w-4 h-4 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20"> <path d="m1.56 6.245 8 3.924a1 1 0 0 0 .88 0l8-3.924a1 1 0 0 0 0-1.8l-8-3.925a1 1 0 0 0-.88 0l-8 3.925a1 1 0 0 0 0 1.8Z"/> <path d="M18 8.376a1 1 0 0 0-1 1v.163l-7 3.434-7-3.434v-.163a1 1 0 0 0-2 0v.786a1 1 0 0 0 .56.9l8 3.925a1 1 0 0 0 .88 0l8-3.925a1 1 0 0 0 .56-.9v-.786a1 1 0 0 0-1-1Z"/> <path d="M17.993 13.191a1 1 0 0 0-1 1v.163l-7 3.435-7-3.435v-.163a1 1 0 1 0-2 0v.787a1 1 0 0 0 .56.9l8 3.925a1 1 0 0 0 .88 0l8-3.925a1 1 0 0 0 .56-.9v-.787a1 1 0 0 0-1-1Z"/> </svg> 
                                Collections
                            </a>
                        </li>
                        <li>
                            <a href="#" class="flex justify-between items-center py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">
                                <span class="flex items-center">
                                    <svg class="mr-2 w-4 h-4 text-primary-600 dark:text-primary-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20"><path d="m7.164 3.805-4.475.38L.327 6.546a1.114 1.114 0 0 0 .63 1.89l3.2.375 3.007-5.006ZM11.092 15.9l.472 3.14a1.114 1.114 0 0 0 1.89.63l2.36-2.362.38-4.475-5.102 3.067Zm8.617-14.283A1.613 1.613 0 0 0 18.383.291c-1.913-.33-5.811-.736-7.556 1.01-1.98 1.98-6.172 9.491-7.477 11.869a1.1 1.1 0 0 0 .193 1.316l.986.985.985.986a1.1 1.1 0 0 0 1.316.193c2.378-1.3 9.889-5.5 11.869-7.477 1.746-1.745 1.34-5.643 1.01-7.556Zm-3.873 6.268a2.63 2.63 0 1 1-3.72-3.72 2.63 2.63 0 0 1 3.72 3.72Z"/></svg>
                                    Pro version
                                </span>
                                <svg class="w-2.5 h-2.5 text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/></svg>
                            </a>
                        </li>
                    </ul>
                    <ul class="py-1 text-gray-500 dark:text-gray-400" aria-labelledby="dropdown">
                        <li>
                            <a href="#" class="block py-2 px-4 text-sm hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Sign out</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </nav>
</header>


{@render children()}


<footer class="p-4 bg-white md:p-8 lg:p-10 dark:bg-gray-800">
	<div class="mx-auto max-w-screen-xl text-center">
		<a href="#" class="flex justify-center items-center text-2xl font-semibold text-gray-900 dark:text-white">
			<svg class="mr-2 h-8" viewBox="0 0 33 33" fill="none" xmlns="http://www.w3.org/2000/svg">
				<path d="M25.2696 13.126C25.1955 13.6364 24.8589 14.3299 24.4728 14.9328C23.9856 15.6936 23.2125 16.2264 22.3276 16.4114L18.43 17.2265C17.8035 17.3575 17.2355 17.6853 16.8089 18.1621L14.2533 21.0188C13.773 21.5556 13.4373 21.4276 13.4373 20.7075C13.4315 20.7342 12.1689 23.9903 15.5149 25.9202C16.8005 26.6618 18.6511 26.3953 19.9367 25.6538L26.7486 21.7247C29.2961 20.2553 31.0948 17.7695 31.6926 14.892C31.7163 14.7781 31.7345 14.6639 31.7542 14.5498L25.2696 13.126Z" fill="url(#paint0_linear_11430_22515)"/><path d="M23.5028 9.20133C24.7884 9.94288 25.3137 11.0469 25.3137 12.53C25.3137 12.7313 25.2979 12.9302 25.2694 13.1261L28.0141 14.3051L31.754 14.5499C32.2329 11.7784 31.2944 8.92561 29.612 6.65804C28.3459 4.9516 26.7167 3.47073 24.7581 2.34097C23.167 1.42325 21.5136 0.818599 19.8525 0.486816L17.9861 2.90382L17.3965 5.67918L23.5028 9.20133Z" fill="url(#paint1_linear_11430_22515)"/><path d="M1.5336 11.2352C1.5329 11.2373 1.53483 11.238 1.53556 11.2358C1.67958 10.8038 1.86018 10.3219 2.08564 9.80704C3.26334 7.11765 5.53286 5.32397 8.32492 4.40943C11.117 3.49491 14.1655 3.81547 16.7101 5.28323L17.3965 5.67913L19.8525 0.486761C12.041 -1.07341 4.05728 3.51588 1.54353 11.2051C1.54233 11.2087 1.53796 11.2216 1.5336 11.2352Z" fill="url(#paint2_linear_11430_22515)"/><path d="M19.6699 25.6538C18.3843 26.3953 16.8003 26.3953 15.5147 25.6538C15.3402 25.5531 15.1757 25.4399 15.0201 25.3174L12.7591 26.8719L10.8103 30.0209C12.9733 31.821 15.7821 32.3997 18.589 32.0779C20.7013 31.8357 22.7995 31.1665 24.7582 30.0368C26.3492 29.1191 27.7 27.9909 28.8182 26.7195L27.6563 23.8962L25.7762 22.1316L19.6699 25.6538Z" fill="url(#paint3_linear_11430_22515)"/><path d="M15.0201 25.3175C14.0296 24.5373 13.4371 23.3406 13.4371 22.0588V21.931V11.2558C13.4371 10.6521 13.615 10.5494 14.1384 10.8513C13.3323 10.3864 11.4703 8.79036 9.17118 10.1165C7.88557 10.858 6.8269 12.4949 6.8269 13.978V21.8362C6.8269 24.775 8.34906 27.8406 10.5445 29.7966C10.6313 29.874 10.7212 29.9469 10.8103 30.0211L15.0201 25.3175Z" fill="url(#paint4_linear_11430_22515)"/><path d="M28.6604 5.49565C28.6589 5.49395 28.6573 5.49532 28.6589 5.49703C28.9613 5.83763 29.2888 6.23485 29.6223 6.68734C31.3648 9.05099 32.0158 12.0447 31.4126 14.9176C30.8093 17.7906 29.0071 20.2679 26.4625 21.7357L25.7761 22.1316L28.8181 26.7195C34.0764 20.741 34.09 11.5388 28.6815 5.51929C28.6789 5.51641 28.67 5.50622 28.6604 5.49565Z" fill="url(#paint5_linear_11430_22515)"/><path d="M7.09355 13.978C7.09354 12.4949 7.88551 11.1244 9.17113 10.3829C9.34564 10.2822 9.52601 10.1965 9.71002 10.1231L9.49304 7.38962L7.96861 4.26221C5.32671 5.23364 3.1897 7.24125 2.06528 9.83067C1.2191 11.7793 0.75001 13.9294 0.75 16.1888C0.75 18.0243 1.05255 19.7571 1.59553 21.3603L4.62391 21.7666L7.09355 21.0223V13.978Z" fill="url(#paint6_linear_11430_22515)"/><path d="M9.71016 10.1231C10.8817 9.65623 12.2153 9.74199 13.3264 10.3829L13.4372 10.4468L22.3326 15.5777C22.9566 15.9376 22.8999 16.2918 22.1946 16.4392L22.7078 16.332C23.383 16.1908 23.9999 15.8457 24.4717 15.3428C25.2828 14.4782 25.5806 13.4351 25.5806 12.5299C25.5806 11.0468 24.7886 9.67634 23.503 8.93479L16.6911 5.00568C14.1436 3.53627 11.0895 3.22294 8.29622 4.14442C8.18572 4.18087 8.07756 4.2222 7.96875 4.26221L9.71016 10.1231Z" fill="url(#paint7_linear_11430_22515)"/><path d="M20.0721 31.8357C20.0744 31.8352 20.0739 31.8332 20.0717 31.8337C19.6252 31.925 19.1172 32.0097 18.5581 32.0721C15.638 32.3978 12.7174 31.4643 10.5286 29.5059C8.33986 27.5474 7.09347 24.7495 7.09348 21.814L7.09347 21.0222L1.59546 21.3602C4.1488 28.8989 12.1189 33.5118 20.0411 31.8421C20.0449 31.8413 20.0582 31.8387 20.0721 31.8357Z" fill="url(#paint8_linear_11430_22515)"/>
				<defs>
				<linearGradient id="paint0_linear_11430_22515" x1="20.8102" y1="23.9532" x2="23.9577" y2="12.9901" gradientUnits="userSpaceOnUse"><stop stop-color="#1724C9"/><stop offset="1" stop-color="#1C64F2"/></linearGradient>
				<linearGradient id="paint1_linear_11430_22515" x1="28.0593" y1="10.5837" x2="19.7797" y2="2.33321" gradientUnits="userSpaceOnUse"><stop stop-color="#1C64F2"/><stop offset="1" stop-color="#0092FF"/></linearGradient>
				<linearGradient id="paint2_linear_11430_22515" x1="16.9145" y1="5.2045" x2="4.42432" y2="5.99375" gradientUnits="userSpaceOnUse"><stop stop-color="#0092FF"/><stop offset="1" stop-color="#45B2FF"/></linearGradient>
				<linearGradient id="paint3_linear_11430_22515" x1="16.0698" y1="28.846" x2="27.2866" y2="25.8192" gradientUnits="userSpaceOnUse"><stop stop-color="#1C64F2"/><stop offset="1" stop-color="#0092FF"/></linearGradient>
				<linearGradient id="paint4_linear_11430_22515" x1="8.01881" y1="15.8661" x2="15.9825" y2="24.1181" gradientUnits="userSpaceOnUse"><stop stop-color="#1724C9"/><stop offset="1" stop-color="#1C64F2"/></linearGradient>
				<linearGradient id="paint5_linear_11430_22515" x1="26.2004" y1="21.8189" x2="31.7569" y2="10.6178" gradientUnits="userSpaceOnUse"><stop stop-color="#0092FF"/><stop offset="1" stop-color="#45B2FF"/></linearGradient>
				<linearGradient id="paint6_linear_11430_22515" x1="6.11387" y1="9.31427" x2="3.14054" y2="20.4898" gradientUnits="userSpaceOnUse"><stop stop-color="#1C64F2"/><stop offset="1" stop-color="#0092FF"/></linearGradient>
				<linearGradient id="paint7_linear_11430_22515" x1="21.2932" y1="8.78271" x2="10.4278" y2="11.488" gradientUnits="userSpaceOnUse"><stop stop-color="#1724C9"/><stop offset="1" stop-color="#1C64F2"/></linearGradient>
				<linearGradient id="paint8_linear_11430_22515" x1="7.15667" y1="21.5399" x2="14.0824" y2="31.9579" gradientUnits="userSpaceOnUse"><stop stop-color="#0092FF"/><stop offset="1" stop-color="#45B2FF"/></linearGradient>
				</defs>
			</svg>
			Flowbite    
		</a>
		<p class="my-6 text-gray-500 dark:text-gray-400">Open-source library of over 400+ web components and interactive elements built for better web.</p>
		<ul class="flex flex-wrap justify-center items-center mb-6 text-gray-900 dark:text-white">
			<li>
				<a href="#" class="mr-4 hover:underline md:mr-6 ">About</a>
			</li>
			<li>
				<a href="#" class="mr-4 hover:underline md:mr-6">Premium</a>
			</li>
			<li>
				<a href="#" class="mr-4 hover:underline md:mr-6 ">Campaigns</a>
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
		<span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2021-2022 <a href="#" class="hover:underline">Flowbite™</a>. All Rights Reserved.</span>
	</div>
</footer>