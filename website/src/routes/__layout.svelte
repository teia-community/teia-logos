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
</script>

<svelte:body />
<Header />
<main>
  <slot />
</main>

<footer>
  <p>
    list of logos <a
      href="https://docs.google.com/forms/d/1qEsPN5njEE9fNdSM1zjetIYGYTSuMpjPl446nG1FvNY/edit"
      >submitted</a
    >
    for the <a href="https://teia.art">teia.art</a> tezos platform
  </p>
</footer>

<style>
  :global(body) {
    background-color: #ffffff;
    color: #000000;
    transition: background-color 0.3s;
  }
  :global(body.dark) {
    background-color: #000000;
    color: #ffffff;
  }
  :global(p) {
    color: black;
  }
  :global(.dark p) {
    color: white;
  }
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
