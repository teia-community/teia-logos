<script>
  import Header from "$lib/header/Header.svelte";
  import "../../app.css";
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
</script>

<svelte:body />
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
    max-width: 1024px;
    margin: 0 auto;
    box-sizing: border-box;
  }

  footer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 40px;
  }

  footer a {
    font-weight: bold;
  }

  @media (min-width: 480px) {
    footer {
      padding: 40px 0;
    }
  }
</style>
