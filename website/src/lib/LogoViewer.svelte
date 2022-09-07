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
  import { raw_url } from "$lib/constants";
  let logos = [];
  let sync_date = "xx-xx-xx";

  export let label = "";
  export let fetch_url;
  export let root = "";
  export let theme_based = false;
  export let loading = "eager";

  let logos_dark = [];
  let logos_light = [];

  let current_logos = [];

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

<h1>{label}</h1>
<div class="container">
  {#each current_logos as logo (logo)}
    <Image src={logo} alt={logo} {loading} largestBorder="128" />
  {/each}
</div>

<style>
  h1 {
    font-size: 2em;
    font-weight: 800;
  }
  .container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
  }
</style>
