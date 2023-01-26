<script>
  import Header from "$lib/header/Header.svelte";
  import "../app.css";
  import { theme } from "$lib/store";
  import { onMount } from "svelte";

  let document;

  onMount(() => {
    document = document || window.document;
  });

  theme.subscribe((t) => {
    if (document) {
      if (t === "dark") {
        document.body.classList.add("dark");
      } else {
        document.body.classList.remove("dark");
      }
    }
  });

  function onKeyDown(e) {
    console.log(e.keyCode);
    switch (e.keyCode) {
      // t
      case 84:
        $theme = $theme === "dark" ? "light" : "dark";
        break;
    }
  }
</script>

<svelte:window on:keydown|preventDefault={onKeyDown} />

<Header />
<main>
  <slot />
</main>

<style>
  main {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 1rem;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    margin-top: 1em;
    box-sizing: border-box;
    align-items: center;
    justify-content: space-between;
  }
</style>
