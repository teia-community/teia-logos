<script>
  import { goto } from "$app/navigation";
  import { base } from "$app/paths";
  import { theme } from "$lib/store";
  import Pfp from "../../../../dist/teia-black.svg?component";

  $: switchTheme = $theme === "dark" ? "light" : "dark";
</script>

<div class="flex_dark">
  <svg
    on:click={() => ($theme = switchTheme)}
    viewBox="0 0 100 100"
    fill="var(--text-color)"
    width="32"
    xmlns="http://www.w3.org/2000/svg"
  >
    <circle cx="50" cy="50" r="50" />
  </svg>
  <!-- <button id="dark_toggle" on:click={() => ($theme = switchTheme)}>
    {switchTheme}</button
  > -->
</div>
<header>
  <nav id="menu">
    <div id="menu_cont">
      <Pfp fill="var(--text-color)" width="64" />
      <div class="flex packs">
        <button id="main" on:click={() => goto(`${base}/press`)}>press</button>
        <button id="main" on:click={() => goto(`${base}/`)}
          >Logos Rotation</button
        >
      </div>
    </div>
  </nav>
</header>

<style global>
  #menu_cont {
    display: flex;
    flex-wrap: nowrap;
    justify-content: flex-end;
  }
  .flex_dark {
    z-index: 100;
    position: fixed;
    bottom: 1em;
    right: 1em;
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
    width: 100%;
    display: flex;
    justify-content: flex-end;
    pointer-events: none;
    user-select: none;
  }
  .packs {
    margin: 1em;
  }
  button {
    pointer-events: all;
    user-select: none;
    border: 0px solid #ccc;
    border-radius: 0px;
    cursor: pointer;
    font-size: 12px;
    font-weight: 600;
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
    font-size: 0.5em;
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
