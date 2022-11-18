<script context="module">
  export const prerender = true;
</script>

<script>
  import LogoViewer from "$lib/LogoViewer.svelte";
  import { raw_url } from "$lib/constants";

  let current = "main";
</script>

<div class="top">
  <h1>logos rotation</h1>
  <div class="flex-cats">
    <button id="main" on:click={() => (current = "main")}>main</button>
    <button id="pride" on:click={() => (current = "pride")}>pride</button>
  </div>
</div>
{#if current === "main"}
  <LogoViewer theme_based fetch_url={`${raw_url}/logos.json`} />
{/if}
{#if current === "pride"}
  <LogoViewer root="pride" fetch_url={`${raw_url}/logos_pride.json`} />
{/if}

<style>
  h1 {
    margin: 0;
    padding: 0;
    font-size: 2em;
  }
  .top {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .flex-cats {
    display: flex;
    flex-direction: row;
    gap: 1em;
    padding-bottom: 2em;
  }
</style>
