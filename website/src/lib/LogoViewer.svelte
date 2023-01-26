<script context="module">
  export const prerender = true;
</script>

<script>
  import Image from "$lib/Image.svelte";
  import { theme } from "$lib/store";
  import figlet from "figlet";
  import { onMount } from "svelte";
  import OpenGraph from "$lib/OpenGraph.svelte";
  import { page } from "$app/stores";
  import { raw_url, submission_form } from "$lib/constants";
  import Checkbox from "./components/Checkbox.svelte";

  let logos = [];
  let sync_date = "xx-xx-xx";
  let logos_dark = [];
  let logos_light = [];
  let current_logos = [];

  let selected = null;
  let label_index = "";
  let show_border = false;
  /* Properties */
  export let fetch_url;
  export let root = "";
  export let theme_based = false;
  export let loading = "eager";

  let lb_size = 200;

  const cycle = (count) => {
    if (selected == undefined) {
      return;
    }
    let id = current_logos.indexOf(selected_img);
    // label_index = `${id}/${current_logos.length}`;
    let new_id = (id + count) % current_logos.length;
    new_id = new_id == -1 ? current_logos.length - 1 : new_id;
    console.log(new_id);
    selected = current_logos[new_id].split("/").pop();
  };

  /* Reactive */
  $: label_name = selected ? selected.replace(raw_url, "") : null;
  $: selected_img = selected
    ? current_logos[current_logos.findIndex((e) => e.includes(selected))]
    : null;
  $: label_index = selected_img
    ? `${current_logos.indexOf(selected_img) + 1}/${current_logos.length}`
    : "";

  const deselect = () => (selected = null);

  function onKeyDown(e) {
    console.log(e.keyCode);
    switch (e.keyCode) {
      // left-arrow
      case 37:
        cycle(-1);
        break;
      //right-arrow
      case 39:
        cycle(1);
        break;
      // esc
      case 27:
        deselect();
        break;
      // up
      case 38:
        lb_size++;
        break;
      // down
      case 40:
        lb_size--;
        break;
      // b
      case 66:
        show_border = !show_border;
        break;
      // t
      case 84:
        break;
    }
  }

  onMount(async () => {
    let logos_fetch = await (await fetch(fetch_url)).json();
    logos = logos_fetch.logos;
    sync_date = logos_fetch.sync_date || "Unknown";

    if (theme_based) {
      logos_dark = logos.map(
        (logo) => `${raw_url}logos/${root ? root + "/" : ""}dark/${logo}`
      );
      logos_light = logos.map(
        (logo) => `${raw_url}logos/${root ? root + "/" : ""}light/${logo}`
      );
      current_logos = $theme === "light" ? logos_light : logos_dark;
    } else {
      current_logos = logos.map((logo) => {
        return `${raw_url}logos/${root ? root + "/" : ""}/${logo}`;
      });
    }

    figlet.text(
      "THEIA",
      {
        font: "Isometric1",
        horizontalLayout: "default",
        verticalLayout: "default",
        width: 80,
        whitespaceBreak: true,
      },
      function (err, data) {
        if (err) {
          console.log("Something went wrong...");
          console.dir(err);
          return;
        }
        console.log(data);
        console.log(`Submission form last synced on ${sync_date}`);
      }
    );
  });

  var date = new Date().toLocaleDateString();

  if (theme_based) {
    theme.subscribe((t) => {
      current_logos = t === "light" ? logos_light : logos_dark;
    });
  }
  console.log(`URL Origin: ${$page.url.origin}`);
</script>

<svelte:head>
  <title>Logo - Viewer</title>
  {#if selected}
    <style>
      body {
        overflow: hidden;
      }
    </style>
  {/if}
</svelte:head>

<OpenGraph
  siteTitle="teia - logo preview"
  siteUrl={$page.url.origin}
  lastUpdated={date}
  metadescription="View all the Teia logo submissions and previews"
  pageTitle="Logo - Viewer"
  image="https://raw.githubusercontent.com/teia-community/teia-logos/main/dist/contact-sheet/dark.png"
  datePublished={date}
  ogLanguage="en_US"
/>

<!-- LightBox -->
<svelte:window on:keydown|preventDefault={onKeyDown} />
{#if selected}
  <div class="lightbox_container">
    <p>{label_name}</p>
    <div class="lightbox">
      <button on:click={() => cycle(-1)}>{"<"}</button>
      <Image
        src={selected_img}
        alt={selected}
        {loading}
        bordered={show_border}
        largestBorder={lb_size}
      />
      <button on:click={() => cycle(1)}>{">"}</button>
    </div>
    <p>{label_index}</p>
  </div>
  <button id="close" on:click={deselect}>close [X]</button>
  <div id="lightbox_tools">
    <Checkbox label="Show Borders" bind:value={show_border} />
  </div>
{/if}

<!-- Logos Container -->
<div class="container">
  {#each current_logos as logo (logo)}
    <Image
      src={logo}
      alt={logo}
      on:click={(sel) => {
        selected = sel.target.src.split("/").pop();
      }}
      {loading}
      largestBorder="128"
    />
  {/each}
</div>

<footer>
  <p>
    list of logos <a href={submission_form}>submitted</a>
    for the <a href="https://teia.art">teia.art</a> tezos platform
  </p>
</footer>

<style>
  button {
    color: var(--text-color);
    background-color: transparent;
    border: none;
    padding: 1em;
  }
  #close {
    position: fixed;
    top: 0;
    right: 0;
  }
  .container {
    display: flex;
    width: 90%;
    /*margin: auto;*/
    margin-left: auto;
    margin-right: auto;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    height: 100%;
    overflow-y: auto;
  }
  .lightbox_container {
    position: fixed;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background-color: var(--bg-color);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
  }
  #lightbox_tools {
    position: fixed;
    bottom: 2em;
    left: 2em;
  }
  .lightbox {
    display: flex;
    width: 100%;

    align-items: center;
    justify-content: space-around;
  }

  footer {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 40px;
  }

  footer a {
    font-weight: 400;
  }

  @media (min-width: 480px) {
    footer {
      padding: 40px 0;
    }
  }
</style>
