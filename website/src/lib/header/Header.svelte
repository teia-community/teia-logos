<script>
  import { goto } from "$app/navigation";
  import { base } from "$app/paths";
  // import { page } from '$app/stores';
  import { theme } from "$lib/store";
  $: switchTheme = $theme === "dark" ? "light" : "dark";
</script>

<div class="flex_dark">
  <button id="dark_toggle" on:click={() => ($theme = switchTheme)}>
    {switchTheme}</button
  >
</div>
<header>
  <nav id="menu">
    <div>
      <div class="flex packs">
        <button id="main" on:click={() => goto(`${base}/press`)}>press</button>
      </div>
      <p id="pack">logo packs</p>
      <div class="flex packs">
        <button id="main" on:click={() => goto(`${base}/`)}
          >Logos Rotation</button
        >
        <button id="pride" on:click={() => goto(`${base}/pride`)}>
          Pride</button
        >
      </div>
    </div>
  </nav>
</header>

<style global>
  #menu {
    background-color: var(--bg-color);
  }
  .flex_dark {
    z-index: 100;
    position: fixed;
    display: flex;
    margin: 0;
    padding: 0;
    flex-direction: column;
    align-items: flex-start;
  }
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
    justify-content: flex-end;
    pointer-events: none;
  }
  .packs {
    margin: 1em;
  }
  button {
    pointer-events: all;
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
    z-index: 100;
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
