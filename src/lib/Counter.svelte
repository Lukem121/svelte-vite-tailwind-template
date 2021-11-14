<script>
  import { getStore } from './hmr-stores';
  export let id;
  const count = getStore(id, 0);
  export const increment = () => {
    $count += 1
  };
</script>

<button class="px-8 py-4 w-52 text-red-500 bg-red-200 rounded-full" {id} on:click={increment}>
  Clicks: {$count}
</button>