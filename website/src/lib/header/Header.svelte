<script>
  // import { page } from '$app/stores';
  import { theme } from "$lib/store";
  $: switchTheme = $theme === "dark" ? "light" : "dark";
</script>

<header>
  <button id="dark_toggle" on:click={() => ($theme = switchTheme)}>
    {switchTheme}</button
  >
</header>

<style>
  header {
    display: flex;
    justify-content: space-between;
  }

  :global(#dark_toggle) {
    background: rgb(0, 0, 0);
    border: 0px solid #ccc;
    border-radius: 0px;
    color: rgb(250, 250, 250);
    cursor: pointer;
    font-size: 12px;
    font-weight: bold;
    padding: 5px 10px;
    margin: 10px;
  }
  :global(.dark #dark_toggle) {
    background: rgb(255, 255, 255);
    border: 0px solid #ccc;
    border-radius: 0px;
    color: rgb(0, 0, 0);
    cursor: pointer;
    font-size: 12px;
    font-weight: bold;
    padding: 5px 10px;
    margin: 10px;
  }
</style>
