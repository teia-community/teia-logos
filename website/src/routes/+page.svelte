<script context="module">
  export const prerender = true;
</script>

<script>
  import LogoViewer from "$lib/LogoViewer.svelte";
  import { raw_url } from "$lib/constants";
</script>

<LogoViewer label="Main" theme_based fetch_url={`${raw_url}/logos.json`} />
