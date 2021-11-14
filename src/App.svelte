<script>
  import logo from './assets/svelte.png'
  import Counter from './lib/Counter.svelte'
  import './lib/TailwindCSS.svelte'
  let increment;
</script>

<section class="text-gray-600 body-font">
  <div class="container mx-auto flex px-5 py-24 items-center justify-center flex-col">
    <img class="lg:w-2/6 md:w-3/6 w-5/6 mb-10 object-cover object-center rounded" alt="hero" src={logo}>
    <div class="text-center lg:w-2/3 w-full">
      <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Svelte + Vite + TailwindCSS = 🌸🌸🌸</h1>
      <p class="mb-8 leading-relaxed">Meggings kinfolk echo park stumptown DIY, kale chips beard jianbing tousled. Chambray dreamcatcher trust fund, kitsch vice godard disrupt ramps hexagon mustache umami snackwave tilde chillwave ugh. Pour-over meditation PBR&amp;B pickled ennui celiac mlkshk freegan photo booth af fingerstache pitchfork.</p>
      <a class="my-8 bg-red-600 text-white p-4 px-8 underline rounded-3xl" href="https://github.com/Lukem121/svelte-vite-tailwind-template">Please ⭐ on GitHub</a>
      <div class="my-8">
        <Counter bind:increment={increment} id="0" />
      </div>
      <div class="flex justify-center">
        <button class="inline-flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg" on:click={increment}>Button</button>
        <button class="ml-4 inline-flex text-gray-700 bg-gray-100 border-0 py-2 px-6 focus:outline-none hover:bg-gray-200 rounded text-lg" on:click={increment}>Button</button>
      </div>
    </div>
  </div>
</section>