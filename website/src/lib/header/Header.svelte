<script>
  import { goto } from "$app/navigation";
  import { base } from "$app/paths";
  // import { page } from '$app/stores';
  import { theme } from "$lib/store";
  $: switchTheme = $theme === "dark" ? "light" : "dark";
</script>

<header>
  <div class="flex">
    <button id="dark_toggle" on:click={() => ($theme = switchTheme)}>
      {switchTheme}</button
    >
  </div>
  <nav>
    <div>
      <p id="pack">packs</p>
      <div class="flex packs">
        <button id="main" on:click={() => goto(`${base}/`)}>Main</button>
        <button id="pride" on:click={() => goto(`${base}/pride`)}>
          Pride</button
        >
      </div>
    </div>
  </nav>
</header>

<style global>
  .flex {
    display: flex;
    margin: 0;
    padding: 0;
    flex-direction: column;
  }

  #pack {
    font-size: 0.75em;
    text-align: center;
  }
  header {
    position: fixed;
    width: 100vw;
    display: flex;
    justify-content: space-between;
  }
  .packs {
    margin: 1em;
  }
  button {
    border: 0px solid #ccc;
    border-radius: 0px;
    cursor: pointer;
    font-size: 12px;
    font-weight: bold;
    padding: 0;
    margin: 0;
  }
  #pride,
  #main {
    font-size: 0.75em;
    padding: 0.25em;
    margin: 0.2em 0;
  }
  #dark_toggle {
    padding: 1em;
  }

  button {
    background: rgb(0, 0, 0);
    color: rgb(250, 250, 250);
  }
  .dark button {
    background: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
  }
</style>
