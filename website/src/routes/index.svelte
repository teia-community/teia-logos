<script context="module">
  export const prerender = true;
</script>

<script>
  import Image from "$lib/Image.svelte";
  import { theme } from "$lib/store";
  import figlet from "figlet";
  import { onMount } from "svelte";
  import Gallery from "$lib/Gallery.svelte";
  import OpenGraph from "$lib/OpenGraph.svelte";
  import { page } from "$app/stores";
  let logos = [];
  let sync_date = "xx-xx-xx";

  onMount(async () => {
    let logos_fetch = await (
      await fetch(
        "https://raw.githubusercontent.com/teia-community/teia-logos/main/dist/logos.json"
      )
    ).json();
    logos = logos_fetch.logos;
    sync_date = logos_fetch.sync_date || "Unknown";

    current_logos = logos.map((logo) => {
      return `https://raw.githubusercontent.com/teia-community/teia-logos/main/dist/logos/${$theme}/${logo}`;
    });

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

  let current_logos = [];
  theme.subscribe((t) => {
    current_logos = logos.map((logo) => {
      return `https://raw.githubusercontent.com/teia-community/teia-logos/main/dist/logos/${$theme}/${logo}`;
    });
  });
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
  image="https://teia.vercel.app/dark.png"
  datePublished={date}
  ogLanguage="en_US"
/>

<section>
  <Gallery maxColumnWidth={128} gap={50} loading="eager">
    {#each current_logos as logo (logo)}
      <img src={logo} alt={logo} />
    {/each}
  </Gallery>
</section>

<style>
  section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex: 1;
  }
</style>
